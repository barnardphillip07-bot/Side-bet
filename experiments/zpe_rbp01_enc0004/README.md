# ZPE-RBP-01 ENC-0004 candidate implementation

Files:
- `zpe_rbp01_labframe.py`: independent laboratory-frame closed-system propagator.
- `test_zpe_rbp01_labframe.py`: 10 acceptance tests.
- `run_zpe_rbp01_labframe.py`: reproducible RWA sweep and numerical refinement.
- `zpe_rbp01_labframe_results.json`: recorded numerical output.
- Full derivation, provenance and limitations: [ENC-0004 Rev 0.1](../../docs/zpe/ZPE-RBP-01-ENC-0004_Rev0.1.md).

Requirements: Python 3.10+, NumPy, SciPy.

```bash
python -m unittest -v test_zpe_rbp01_labframe.py
python run_zpe_rbp01_labframe.py
```

Scope: isolated, closed, single-mode lumped resonator with externally prescribed
positive time-varying capacitance. No damping, baths, transmission-line coupling,
mechanical quantization, PZT dynamics or physical hardware validation.

ENC-0003 is used only as an RWA comparison candidate. Its source files are not
modified and its physical architecture is not promoted or owner-approved by this
work. Numerical values are computational test inputs, not hardware selections.
