"""Content-addressable source indexing for local files, text dumps and ZIP archives."""
from __future__ import annotations

import ast
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from typing import Any

INDEXER_NAME = "dingoos-recovery-indexer"
INDEXER_VERSION = "0.1.0"
DEFAULT_MAX_FILE_BYTES = 50 * 1024 * 1024
DEFAULT_MAX_ARCHIVE_ENTRY_BYTES = 20 * 1024 * 1024
DEFAULT_MAX_ARCHIVE_ENTRIES = 10_000

_FENCE = re.compile(rb"(?m)^[ \t]*```([A-Za-z0-9_+.-]*)[^\r\n]*\r?\n")
_DECLARATION = re.compile(rb"(?m)(?:^|[ \t])(?:class|def|async[ \t]+def)[ \t]+([A-Za-z_][A-Za-z0-9_]*)")


class IndexingError(ValueError):
    """Raised for invalid input or unsafe indexing parameters."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _line_starts(data: bytes) -> list[int]:
    starts = [0]
    for match in re.finditer(b"\n", data):
        starts.append(match.end())
    return starts


def _byte_offset(starts: list[int], line: int, column: int) -> int:
    if line < 1 or line > len(starts):
        raise IndexingError(f"line number out of range: {line}")
    return starts[line - 1] + column


def _record(
    *,
    artifact_id: str,
    parent_path: str,
    parent_sha: str,
    parent_size: int,
    region_bytes: bytes,
    start: int,
    end: int,
    line_start: int | None,
    line_end: int | None,
    classification: str,
    symbols: list[dict[str, Any]],
    status: str,
    grammar: str,
    tags: list[str] | None = None,
    errors: list[str] | None = None,
    archive_entry_path: str | None = None,
    coverage_receipt_ref: str | None = None,
) -> dict[str, Any]:
    return {
        "schema_id": "SOURCE_ARTIFACT_INDEX_RECORD",
        "schema_version": "0.1.0",
        "artifact_id": artifact_id,
        "parent_artifact": {
            "path": parent_path,
            "archive_entry_path": archive_entry_path,
            "sha256": parent_sha,
            "size_bytes": parent_size,
        },
        "region": {
            "byte_offset_start": start,
            "byte_offset_end": end,
            "line_start": line_start,
            "line_end": line_end,
            "content_sha256": sha256_bytes(region_bytes),
        },
        "classification": classification,
        "tags": tags or [],
        "symbols": symbols,
        "extractor": {
            "name": INDEXER_NAME,
            "version": INDEXER_VERSION,
            "grammar": grammar,
            "canonicalization_profile": None,
        },
        "status": status,
        "errors": errors or [],
        "coverage_receipt_ref": coverage_receipt_ref,
    }


def _python_symbol_records(
    *,
    code: bytes,
    parent_path: str,
    parent_sha: str,
    parent_size: int,
    base_offset: int,
    base_line: int,
    archive_entry_path: str | None,
    coverage_receipt_ref: str | None,
    prefix: str,
) -> list[dict[str, Any]]:
    try:
        source = code.decode("utf-8")
        tree = ast.parse(source, filename=parent_path)
    except (UnicodeDecodeError, SyntaxError) as exc:
        return [_record(
            artifact_id=f"{prefix}:python-parse-failed",
            parent_path=parent_path, parent_sha=parent_sha, parent_size=parent_size,
            region_bytes=code, start=base_offset, end=base_offset + len(code),
            line_start=base_line, line_end=base_line + max(code.count(b"\n"), 0),
            classification="other_embedded_source", symbols=[], status="parse_failed",
            grammar="Python AST; syntax/UTF-8 parse attempted",
            tags=["CONTAINS_EMBEDDED_SOURCE", "PARSE_INCOMPLETE"],
            errors=[str(exc)], archive_entry_path=archive_entry_path,
            coverage_receipt_ref=coverage_receipt_ref,
        )]

    starts = _line_starts(code)
    records: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not getattr(node, "end_lineno", None) or not getattr(node, "end_col_offset", None):
            continue
        local_start = _byte_offset(starts, node.lineno, node.col_offset)
        local_end = _byte_offset(starts, node.end_lineno, node.end_col_offset)
        region = code[local_start:local_end]
        kind = "class" if isinstance(node, ast.ClassDef) else "function"
        records.append(_record(
            artifact_id=f"{prefix}:{kind}:{node.name}:{node.lineno}",
            parent_path=parent_path, parent_sha=parent_sha, parent_size=parent_size,
            region_bytes=region, start=base_offset + local_start, end=base_offset + local_end,
            line_start=base_line + node.lineno - 1, line_end=base_line + node.end_lineno - 1,
            classification="python_ast_symbol",
            symbols=[{"kind": kind, "identifier": node.name, "signature": None}],
            status="complete", grammar="Python AST",
            tags=["SOURCE_FILE"] if archive_entry_path is None and parent_path.endswith(".py") else ["CONTAINS_EMBEDDED_SOURCE"],
            archive_entry_path=archive_entry_path, coverage_receipt_ref=coverage_receipt_ref,
        ))
    return records


def _fenced_blocks(
    data: bytes,
    *,
    parent_path: str,
    parent_sha: str,
    coverage_receipt_ref: str | None,
) -> tuple[list[dict[str, Any]], list[tuple[int, int]]]:
    records: list[dict[str, Any]] = []
    covered: list[tuple[int, int]] = []
    position = 0
    index = 0
    while True:
        opening = _FENCE.search(data, position)
        if not opening:
            break
        closing = re.search(rb"(?m)^[ \\t]*```[ \\t]*\\r?$", data[opening.end():])
        if not closing:
            records.append(_record(
                artifact_id=f"{parent_path}:fence:{index}:unclosed",
                parent_path=parent_path, parent_sha=parent_sha, parent_size=len(data),
                region_bytes=data[opening.start():], start=opening.start(), end=len(data),
                line_start=data[:opening.start()].count(b"\\n") + 1, line_end=data.count(b"\\n") + 1,
                classification="fenced_code_block", symbols=[], status="partial",
                grammar="Markdown fenced block",
                tags=["CONTAINS_EMBEDDED_SOURCE", "PARSE_INCOMPLETE"],
                errors=["Opening fence has no matching closing fence"],
                coverage_receipt_ref=coverage_receipt_ref,
            ))
            covered.append((opening.start(), len(data)))
            break
        close_start = opening.end() + closing.start()
        close_end = opening.end() + closing.end()
        code_start, code_end = opening.end(), close_start
        code = data[code_start:code_end]
        covered.append((opening.start(), close_end))
        start_line = data[:code_start].count(b"\\n") + 1
        end_line = start_line + code.count(b"\\n")
        language = opening.group(1).decode("ascii", errors="ignore").lower()
        if language in ("python", "py"):
            parsed = _python_symbol_records(
                code=code, parent_path=parent_path, parent_sha=parent_sha, parent_size=len(data),
                base_offset=code_start, base_line=start_line, archive_entry_path=None,
                coverage_receipt_ref=coverage_receipt_ref,
                prefix=f"{parent_path}:fence:{index}",
            )
            if parsed:
                records.extend(parsed)
            else:
                records.append(_record(
                    artifact_id=f"{parent_path}:fence:{index}:python-block",
                    parent_path=parent_path, parent_sha=parent_sha, parent_size=len(data),
                    region_bytes=code, start=code_start, end=code_end,
                    line_start=start_line, line_end=end_line,
                    classification="fenced_code_block", symbols=[], status="complete",
                    grammar="Python fenced block; no class/function symbols",
                    tags=["CONTAINS_EMBEDDED_SOURCE"], coverage_receipt_ref=coverage_receipt_ref,
                ))
        else:
            records.append(_record(
                artifact_id=f"{parent_path}:fence:{index}:{language or 'unlabelled'}",
                parent_path=parent_path, parent_sha=parent_sha, parent_size=len(data),
                region_bytes=code, start=code_start, end=code_end,
                line_start=start_line, line_end=end_line,
                classification="fenced_code_block", symbols=[], status="complete",
                grammar=f"Markdown fenced block language={language or 'unlabelled'}",
                tags=["CONTAINS_EMBEDDED_SOURCE"], coverage_receipt_ref=coverage_receipt_ref,
            ))
        position = close_end
        index += 1
    return records, covered


def _unfenced_declaration_candidates(
    data: bytes, *, parent_path: str, parent_sha: str,
    coverage_receipt_ref: str | None,
    covered_ranges: list[tuple[int, int]] | None = None,
) -> list[dict[str, Any]]:
    """Index declaration-bearing lines in mixed prose without claiming AST validity."""
    records = []
    starts = _line_starts(data)
    covered_ranges = covered_ranges or []
    for match in _DECLARATION.finditer(data):
        if any(left <= match.start() < right for left, right in covered_ranges):
            continue
        line = data[:match.start()].count(b"\\n") + 1
        line_start = starts[line - 1]
        line_end = data.find(b"\\n", line_start)
        if line_end < 0:
            line_end = len(data)
        raw_line = data[line_start:line_end]
        identifier = match.group(1).decode("ascii", errors="replace")
        declaration = data[match.start():match.end()]
        kind = "class" if re.search(rb"\\bclass\\s+", declaration) else "function"
        records.append(_record(
            artifact_id=f"{parent_path}:unfenced:{kind}:{identifier}:{line}",
            parent_path=parent_path, parent_sha=parent_sha, parent_size=len(data),
            region_bytes=raw_line, start=line_start, end=line_end,
            line_start=line, line_end=line,
            classification="other_embedded_source",
            symbols=[{"kind": kind, "identifier": identifier, "signature": None}],
            status="partial", grammar="Heuristic declaration-line detector; no AST boundary proof",
            tags=["CONTAINS_EMBEDDED_SOURCE", "PARSE_INCOMPLETE"],
            errors=["Unfenced mixed-text candidate; exact logical code-block boundary is not inferred"],
            coverage_receipt_ref=coverage_receipt_ref,
        ))
    return records


def index_bytes(
    path: str,
    data: bytes,
    *,
    coverage_receipt_ref: str | None = None,
    max_file_bytes: int = DEFAULT_MAX_FILE_BYTES,
) -> list[dict[str, Any]]:
    """Index one file's bytes. Offsets refer to original bytes or uncompressed ZIP-entry bytes."""
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    parent_sha = sha256_bytes(data)
    if len(data) > max_file_bytes:
        return [_record(
            artifact_id=f"{path}:size-limit",
            parent_path=path, parent_sha=parent_sha, parent_size=len(data),
            region_bytes=b"", start=0, end=1, line_start=None, line_end=None,
            classification="other_embedded_source", symbols=[], status="unsupported",
            grammar="size limit", tags=["PARSE_INCOMPLETE"],
            errors=[f"File exceeds configured max_file_bytes={max_file_bytes}"],
            coverage_receipt_ref=coverage_receipt_ref,
        )]
    suffix = Path(path).suffix.lower()
    if suffix == ".py":
        ast_records = _python_symbol_records(
            code=data, parent_path=path, parent_sha=parent_sha, parent_size=len(data),
            base_offset=0, base_line=1, archive_entry_path=None,
            coverage_receipt_ref=coverage_receipt_ref, prefix=path,
        )
        symbols = [symbol for record in ast_records for symbol in record["symbols"]]
        status = "parse_failed" if any(record["status"] == "parse_failed" for record in ast_records) else "complete"
        file_record = _record(
            artifact_id=f"{path}:source-file", parent_path=path, parent_sha=parent_sha,
            parent_size=len(data), region_bytes=data, start=0, end=len(data),
            line_start=1, line_end=data.count(b"\\n") + 1,
            classification="source_file", symbols=symbols, status=status,
            grammar="Python AST", tags=["SOURCE_FILE"] + (["PARSE_INCOMPLETE"] if status != "complete" else []),
            errors=[e for record in ast_records for e in record["errors"]],
            coverage_receipt_ref=coverage_receipt_ref,
        ) if data else None
        return ([file_record] if file_record else []) + ast_records
    if suffix in (".md", ".markdown", ".txt", ".rst"):
        records, covered = _fenced_blocks(data, parent_path=path, parent_sha=parent_sha,
                                          coverage_receipt_ref=coverage_receipt_ref)
        records.extend(_unfenced_declaration_candidates(
            data, parent_path=path, parent_sha=parent_sha,
            coverage_receipt_ref=coverage_receipt_ref, covered_ranges=covered))
        return records
    if suffix == ".json":
        try:
            obj = json.loads(data.decode("utf-8"))
            keys = list(obj.keys()) if isinstance(obj, dict) else []
            return [_record(
                artifact_id=f"{path}:json-root",
                parent_path=path, parent_sha=parent_sha, parent_size=len(data),
                region_bytes=data, start=0, end=len(data), line_start=1,
                line_end=data.count(b"\\n") + 1, classification="json_structure",
                symbols=[{"kind":"json_key","identifier":str(k),"signature":None} for k in keys],
                status="complete", grammar="JSON parser",
                tags=["STRUCTURED_SCHEMA"], coverage_receipt_ref=coverage_receipt_ref,
            )]
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            return [_record(
                artifact_id=f"{path}:json-parse-failed",
                parent_path=path, parent_sha=parent_sha, parent_size=len(data),
                region_bytes=data, start=0, end=len(data), line_start=1,
                line_end=data.count(b"\\n") + 1, classification="json_structure",
                symbols=[], status="parse_failed", grammar="JSON parser",
                tags=["STRUCTURED_SCHEMA","PARSE_INCOMPLETE"], errors=[str(exc)],
                coverage_receipt_ref=coverage_receipt_ref,
            )]
    if suffix == ".tla":
        matches=list(re.finditer(rb"(?m)^\\s*----\\s*MODULE\\s+([A-Za-z0-9_]+)",data))
        if matches:
            m=matches[0]; line=data[:m.start()].count(b"\\n")+1
            return [_record(
                artifact_id=f"{path}:tla-module:{m.group(1).decode()}",
                parent_path=path,parent_sha=parent_sha,parent_size=len(data),
                region_bytes=data[m.start():m.end()],start=m.start(),end=m.end(),
                line_start=line,line_end=line,classification="tla_module",
                symbols=[{"kind":"tla_module","identifier":m.group(1).decode(),"signature":None}],
                status="complete",grammar="TLA+ module-header recognizer",
                tags=["STRUCTURED_SCHEMA"],coverage_receipt_ref=coverage_receipt_ref)]
        return [_record(
            artifact_id=f"{path}:tla-header-missing",parent_path=path,parent_sha=parent_sha,parent_size=len(data),
            region_bytes=data,start=0,end=len(data),line_start=1,line_end=data.count(b"\\n")+1,
            classification="tla_module",symbols=[],status="partial",grammar="TLA+ module-header recognizer",
            tags=["STRUCTURED_SCHEMA","PARSE_INCOMPLETE"],errors=["No MODULE header found"],
            coverage_receipt_ref=coverage_receipt_ref)]
    return [_record(
        artifact_id=f"{path}:unsupported-language",parent_path=path,parent_sha=parent_sha,parent_size=len(data),
        region_bytes=data,start=0,end=len(data),line_start=1,line_end=data.count(b"\\n")+1,
        classification="other_embedded_source",symbols=[],status="unsupported",grammar=f"No parser registered for {suffix or 'extensionless file'}",
        tags=["PARSE_INCOMPLETE"],errors=["Content type not handled by this indexer version"],
        coverage_receipt_ref=coverage_receipt_ref)] if data else []

def index_zip_bytes(
    archive_path: str,
    archive_bytes: bytes,
    *,
    coverage_receipt_ref: str | None = None,
    max_entries: int = DEFAULT_MAX_ARCHIVE_ENTRIES,
    max_entry_bytes: int = DEFAULT_MAX_ARCHIVE_ENTRY_BYTES,
) -> list[dict[str, Any]]:
    """Index each supported ZIP member without extracting or modifying the archive."""
    archive_sha = sha256_bytes(archive_bytes)
    records: list[dict[str, Any]] = []
    try:
        zf = zipfile.ZipFile(io.BytesIO(archive_bytes))
    except zipfile.BadZipFile as exc:
        return [_record(
            artifact_id=f"{archive_path}:bad-zip",parent_path=archive_path,parent_sha=archive_sha,
            parent_size=len(archive_bytes),region_bytes=archive_bytes,start=0,end=len(archive_bytes),
            line_start=None,line_end=None,classification="other_embedded_source",symbols=[],
            status="parse_failed",grammar="ZIP central directory",tags=["PARSE_INCOMPLETE"],
            errors=[str(exc)],coverage_receipt_ref=coverage_receipt_ref)]
    with zf:
        infos=zf.infolist()
        if len(infos)>max_entries:
            infos=infos[:max_entries]
            records.append(_record(
                artifact_id=f"{archive_path}:entry-limit",parent_path=archive_path,parent_sha=archive_sha,
                parent_size=len(archive_bytes),region_bytes=b"",start=0,end=1,line_start=None,line_end=None,
                classification="other_embedded_source",symbols=[],status="partial",grammar="ZIP entry limit",
                tags=["PARSE_INCOMPLETE"],errors=[f"Archive has more than max_entries={max_entries}; remaining entries not inspected"],
                coverage_receipt_ref=coverage_receipt_ref))
        for info in infos:
            if info.is_dir():
                continue
            if info.file_size>max_entry_bytes:
                records.append(_record(
                    artifact_id=f"{archive_path}!{info.filename}:size-limit",parent_path=archive_path,
                    parent_sha=archive_sha,parent_size=len(archive_bytes),region_bytes=b"",start=0,end=1,
                    line_start=None,line_end=None,classification="other_embedded_source",symbols=[],
                    status="unsupported",grammar="ZIP entry size limit",tags=["PARSE_INCOMPLETE"],
                    errors=[f"Entry exceeds max_entry_bytes={max_entry_bytes}"],
                    archive_entry_path=info.filename,coverage_receipt_ref=coverage_receipt_ref))
                continue
            try:
                member=zf.read(info)
            except (RuntimeError, zipfile.BadZipFile, OSError) as exc:
                records.append(_record(
                    artifact_id=f"{archive_path}!{info.filename}:read-failed",parent_path=archive_path,
                    parent_sha=archive_sha,parent_size=len(archive_bytes),region_bytes=b"",start=0,end=1,
                    line_start=None,line_end=None,classification="other_embedded_source",symbols=[],
                    status="parse_failed",grammar="ZIP member reader",tags=["PARSE_INCOMPLETE"],
                    errors=[str(exc)],archive_entry_path=info.filename,coverage_receipt_ref=coverage_receipt_ref))
                continue
            member_path=f"{archive_path}!{info.filename}"
            member_records=index_bytes(member_path,member,coverage_receipt_ref=coverage_receipt_ref,
                                       max_file_bytes=max_entry_bytes)
            for rec in member_records:
                rec["parent_artifact"]["path"]=archive_path
                rec["parent_artifact"]["archive_entry_path"]=info.filename
                rec["parent_artifact"]["sha256"]=archive_sha
                rec["parent_artifact"]["size_bytes"]=len(archive_bytes)
                records.append(rec)
    return records


def index_path(path: str | Path, *, coverage_receipt_ref: str | None = None) -> list[dict[str, Any]]:
    """Index one local file. Directories must be enumerated explicitly by the caller."""
    file_path=Path(path)
    data=file_path.read_bytes()
    if file_path.suffix.lower()==".zip":
        return index_zip_bytes(str(file_path),data,coverage_receipt_ref=coverage_receipt_ref)
    return index_bytes(str(file_path),data,coverage_receipt_ref=coverage_receipt_ref)
