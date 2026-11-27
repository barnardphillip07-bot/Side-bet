# SW-ZPE-01 SECE-004A Rev 0.6 — Archive Pointer

- Record: `ZPE-04A-ENC-0002 Rev 0.6`
- Date: 2026-11-28
- Governing baseline: SW-ZPE-01 Rev 2.3
- Status: DERIVED FOCUSED TRANSIENT SCREEN / STATIC AUDIT PASS / ODE SCREEN PASS / SPICE NOT RUN / NOT RELEASED
- Parent Rev 0.5 package SHA-256: `6547a554170effdf346e43c67634546e75a9216a9eb0ec8439ac43a841e40f5f`
- Rev 0.6 package SHA-256: `04b47cb456bfc98559fd44d92394ab056e7d8b14b2b55c7bc650b8f1b28743eb`
- T2.4 focused testbench SHA-256: `f2392b73dec6430baf781c9279f1001fbca2b480468181e9ad3b01360b447b4b`

## Engineering change

Rev 0.6 identifies that the T2.3 0.5 ns maximum timestep cannot resolve its own idealized S_VL turn-on RC transient: with 20 mΩ and 10 pF / 100 pF / 1 nF, the nominal time constants are 0.2 ps / 2 ps / 20 ps. A focused T2.4 testbench therefore adds explicit series loop R/L placeholders and a 10 ps maximum timestep.

The 27-case reduced-order RLC screen produced 0.0992–9.4764 A peak-current sensitivity, up to 99.44 V/ns dv/dt, and a maximum normalized energy residual of 4.142e-9. These are linear analytical screening values, not selected-device predictions.

## Evidence boundary

- T2.4 is a focused turn-on parasitic-discharge subtest, not a replacement for T2.3 recovery commutation.
- All 25 S_VL requirements remain OPEN.
- LTspice/ngspice execution: NOT RUN.
- Hardware validation: NOT PERFORMED.
- MOSFET selection and design release: NONE.
- TEST-001 Rev 1.0 and Rev03B native KiCad source remain UNRETRIEVED.
- P0–P6 and SECE-001 through SECE-009 remain OPEN; E07-5/E07-6 remain HOLD.

The full controlled Rev 0.6 package and individual engineering artifacts are preserved in the project's persistent Library archive. This public repository branch contains this pointer only; no SPICE source or binary package is copied here.
