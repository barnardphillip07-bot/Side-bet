# Independent Physics Reference PoC

A small, standard-library-only Python reference implementation for two established benchmark models:

1. Analytic free response and basic parameters of a linear damped oscillator.
2. Snell refraction and Fresnel **power** reflectance/transmittance for lossless, isotropic, non-magnetic dielectrics with real positive refractive indices.

This is independent educational/reference software. It is not a DingoOS implementation, not a reconstruction of proprietary theory, and not a scientific certification or production engineering tool.

## Requirements

- Python 3.11 or newer.
- No third-party runtime or test dependencies.
- No network access, credentials, API keys, containers, or bootstrap script required.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Run demonstration

```bash
python physics_reference.py
```

## Model scope

### Damped oscillator

```
m*x'' + c*x' + k*x = 0, with m > 0, k > 0, c >= 0.
```

The implementation gives omega0=sqrt(k/m), f0=omega0/(2*pi), damping ratio zeta=c/(2*sqrt(m*k)), and Q=sqrt(m*k)/c, with the undamped limit Q=infinity. The transient is evaluated analytically for underdamped, critically damped, and overdamped cases. A separate fixed-step RK4 method supplies a numerical cross-check against the analytic solution. This is not a forced-response solver, nonlinear model, or experimental digital twin.

### Optics

Snell's law and s/p Fresnel **power** coefficients are evaluated for a single planar interface. Angles are in radians measured from the surface normal. Total internal reflection is handled for the lossless dielectric case. Power transmittance must not be confused with the squared magnitude of an electric-field amplitude coefficient without the refractive-index/cosine power factor.

## Assurance limits

- Unit tests check specified functions and domains; they do not prove general theorems or validate physical instruments.
- No generalized dimensional-analysis engine, symbolic algebra, interval arithmetic, uncertainty propagation, experimental acquisition chain, graph store, ledger, authentication, policy engine, or production API is included.
- Floating-point results use standard Python float; no directed-rounding error enclosure is claimed.
- The model assumptions must be checked before using outputs in a real engineering decision.
