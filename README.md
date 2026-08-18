# Qubit-efficient variational algorithm for nuclear structure

[![arXiv](https://img.shields.io/badge/arXiv-2605.30261-b31b1b.svg)](https://doi.org/10.48550/arXiv.2605.30261)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the code and supporting material for:

> **Qubit-efficient variational algorithm for nuclear structure**
> Chandan Sarma and P. D. Stevenson
> arXiv:2605.30261 (2026)

The work investigates qubit-efficient mappings for applying the **Variational Quantum Eigensolver (VQE)** to nuclear shell-model calculations and demonstrates their implementation on contemporary quantum hardware.

## Overview

Quantum simulation of nuclear many-body systems is challenging because the dimension of the underlying Hilbert space grows rapidly with the number of particles.

In this work, we investigate three mappings of nuclear many-particle configurations to qubit degrees of freedom:

1. **Slater determinant (SD) mapping**
2. **Proton-neutron Slater determinant (pnSD) mapping**
3. **Compact Slater determinant (cSD) mapping**

The mappings are compared in terms of qubit requirements, circuit depth, gate counts, Hamiltonian complexity, and performance under realistic noise.

The methods are benchmarked for the ground states of (^{10}\mathrm{B}) and (^{12}\mathrm{C}).


## Workflow

The calculations follow the general workflow:

```text
Nuclear shell-model Hamiltonian
            │
            ▼
   Many-particle / SD basis
            │
            ▼
     Qubit mapping
   ┌────────┼────────┐
   │        │        │
  SD      pnSD     cSD
   │        │        │
   └────────┼────────┘
            ▼
      Qubit Hamiltonian
            │
            ▼
       VQE ansatz
            │
            ▼
     Classical optimization
            │
            ▼
    Noisy simulation / IBM
            │
            ▼
      Error mitigation
            │
            ▼
      Ground-state energy
```

## Citation

If you use this code or the methods described here, please cite:

```bibtex
@article{SarmaStevenson2026,
  title         = {Qubit-efficient variational algorithm for nuclear structure},
  author        = {Sarma, Chandan and Stevenson, Paul},
  journal       = {arXiv preprint arXiv:2605.30261},
  year          = {2026},
  doi           = {10.48550/arXiv.2605.30261},
  eprint        = {2605.30261},
  archivePrefix = {arXiv},
  primaryClass  = {nucl-th}
}
```

## Authors

**Chandan Sarma**
School of Mathematics and Physics
University of Surrey, Guildford, UK

**P. D. Stevenson**
School of Mathematics and Physics
University of Surrey, Guildford, UK


## Acknowledgements

This work was supported by the UK Science and Technology Facilities Council (STFC) and the UK National Quantum Computing Centre (NQCC), part of the UK National Quantum Technologies Programme.
