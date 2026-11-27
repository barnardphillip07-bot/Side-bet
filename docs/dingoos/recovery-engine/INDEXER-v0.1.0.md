# DingoOS source indexer v0.1.0

Status: **IMPLEMENTED — CI VERIFIED ON FIXTURE CORPUS; NOT YET RUN AS A COMPLETE LIBRARY SCAN**

Implementation: `src/dingoos_recovery/indexer.py`

## Supported inputs

- Python `.py` files: whole-file record plus AST class/function records.
- Markdown/text/RST: fenced blocks; Python AST parsing for `python`/`py` fences; heuristic declaration-line candidates outside fenced blocks.
- JSON: parse and index top-level object keys.
- TLA+: recognize a `---- MODULE Name` header.
- ZIP: enumerate member entries in-memory, index supported members, and preserve the archive parent hash and member path.

Unsupported suffixes and parse failures produce explicit records rather than silently disappearing.

## Byte-offset rules

- Original file offsets are zero-based, inclusive start and exclusive end.
- AST `col_offset` / `end_col_offset` values are UTF-8 byte offsets, and are applied to byte-based line starts.
- Markdown fenced block offsets include only code bytes, excluding opening/closing fence lines.
- ZIP-member offsets are relative to the uncompressed member byte stream. The parent archive SHA-256 and exact `archive_entry_path` are retained to identify that byte domain.
- Every record's `content_sha256` is computed from the exact byte slice represented by its offsets.

## Limits and honest failure states

- Default whole-file limit: 50 MiB.
- Default ZIP-member limit: 20 MiB.
- Default ZIP-entry limit: 10,000.
- No extraction to disk; archive members are read in memory.
- Nested ZIPs are currently recorded as unsupported rather than recursively expanded.
- Python AST parsing is performed only on complete `.py` files and explicitly labelled Python fenced blocks.
- Unfenced declarations in mixed prose are heuristic candidates with status `partial`; they are not claimed to be complete function bodies or valid syntax.
- No parser for arbitrary binary formats, notebook files, PDF embedded code, shell, Rust, Go, TypeScript or other languages is implemented in v0.1.0. Such inputs return explicit unsupported/partial outcomes or are handled only by supported text extraction.
- The indexer does not authenticate source origin, determine canonical lineage, or prove that an effecting target invokes a guard.

## API

```python
from dingoos_recovery.indexer import index_bytes, index_path, index_zip_bytes

records = index_path("path/to/source.py", coverage_receipt_ref="receipt-id")
records = index_bytes("notes.txt", raw_bytes, coverage_receipt_ref="receipt-id")
records = index_zip_bytes("bundle.zip", archive_bytes, coverage_receipt_ref="receipt-id")
```

The caller is responsible for enumerating the search universe, creating and validating a SEARCH_COVERAGE_RECEIPT, preserving raw source bytes, and persisting returned records. The indexer must not independently claim that a search is complete.

## Verification

Fixture tests cover Python AST extraction, exact offsets and hashes, fenced Markdown blocks, malformed code, unfenced mixed-text candidates, JSON keys, TLA+ headers, ZIP member traversal, unsupported formats and size limits.

Latest CI result at implementation increment: **27 passed**. This is fixture-level verification only; no complete Library or DingoOS archive scan has yet been run by this module.
