# Information Preservation in Non-Equilibrium Spin Networks Under Rotating Magnetic Fields

[![DOI](https://shields.io)](https://zenodo.org/uploads/21210709)

## Overview
This repository contains the manuscript and full simulation source code for a non-equilibrium statistical mechanics study on how structured information (orientational order) is sustained in driven, dissipative environments. 

Using a substrate-free two-dimensional rotor model (an XY-like spin network), we investigate a system subjected to order-dependent degradation and an active, localized repair mechanism. This framework directly maps onto real-world physical systems, such as magnetic domain storage under active error correction and phase synchronization in active colloidal spinner arrays driven by rotating magnetic fields.

## Key Scientific Contributions

1. **Exact Order–Entropy Bridge:** We prove an analytical bijection mapping directional order directly to configurational entropy ($\frac{dS}{dU_\chi} = -\kappa$), demonstrating that the final increments toward perfect alignment become logarithmically expensive.
2. **Feedback-Driven Bistability:** We introduce nonlinear feedback where disordered local neighborhoods accelerate decay. A mean-field reduction reveals saddle-node bifurcations and a robust hysteresis window where ordered and collapsed steady states coexist.
3. **BKT-Driven Phase Transitions:** Through finite-size scaling ($L = 32–64$) and the Nelson–Kosterlitz criterion, we prove that field-free order loss is thermally driven by Berezinskii–Kosterlitz–Thouless (BKT) fluctuations ($f_{\text{KT}} \approx 0.22$) rather than geometric site percolation ($1 - p_c \approx 0.407$).
4. **Thermodynamic Cost of Preservation:** Utilizing Schnakenberg network theory, we quantify the non-zero entropy production rate ($\sigma > 0$) of the maintenance cycle, proving that the energetic cost scales directly with the amount of preserved directional information.

All analytical findings are validated to a high degree of precision via kinetic Monte Carlo (KMC) simulations.

## Repository Contents
* `manuscript.pdf`: The complete pre-print paper.
* `/src`: Self-contained Python scripts (`NumPy`, `SciPy`, `Matplotlib`) containing the kinetic Monte Carlo engine and complete data-plotting routines used to generate the manuscript figures.

## Citation & Archival
The persistent record for this work can be found on Zenodo: [Deposit #21210709](https://zenodo.org/uploads/21210709).
