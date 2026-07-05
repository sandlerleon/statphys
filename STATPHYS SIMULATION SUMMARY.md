# Simulation Summary — *Information Maintenance in Non-Equilibrium Rotational Lattices* (v4, JSP)

All simulations are self-contained Python (NumPy/SciPy/Matplotlib). k_BT = 1 in reduced units unless noted; XY exchange J₀ = 1.

## Model
2D XY rotors θ_i with binary site integrity g_i ∈ {1, g₀}. Energy
H = −J₀ Σ_⟨ij⟩ g_i g_j cos(θ_i−θ_j) − h₀ Σ_i g_i cos θ_i.
Reversible Metropolis rotor relaxation + non-conservative, **order-dependent** site process:
kill rate λ_i = λ₀[1 + β·𝒟_i^h/(K^h+𝒟_i^h)], 𝒟_i = 1 − |¼ Σ_neighbors e^{iθ}| (local disorder); repair rate R.
Control group ρ = R/λ₀. Order parameter U_χ = |mean e^{iθ}|, I = 1 − U_χ.

## Figures and scripts

| Fig | Script | Result |
|---|---|---|
| 1 Entropy bridge | `statphys_figs.py` → `sp_fig1_bridge.png` | S(U_χ) strictly ↓; dS/dU_χ = −κ; H_χ ≈ −½ln(1−U_χ)+½(lnπ−1), asymptote confirmed (H_χ(0.95)=1.57 vs exact 1.56) |
| 2 Linear baseline (β=0) | `statphys_figs.py` → `sp_fig2_ips.png` | site process exact 2-state chain; I*=1/(1+ρ); NESS + relaxation vs catastrophe |
| 3 Nonlinear bistability | `statphys_v2_figs.py` → `sp2_fig_bistable.png` | μ(I)=1+βI^h/(K^h+I^h); saddle-node folds; **bistable window ρ∈[3.9,11.3]** for (h,K,β)=(6,0.5,20) |
| 4 Lattice validation | `validate_sim.py` → `sp3_fig_validate.png` | KMC hysteresis gap 0.02 (slow/warm) → 0.18 (cold/fast), straddling MF window; **NESS balance J_kill=J_rep to <0.2%/site/sweep** |
| 5 FSS phase analysis | `fss_sim.py` → `sp4_fig_fss.png` | **helicity modulus crosses 2T/π at f_KT≈0.22 ≪ 1−p_c=0.407 → BKT-driven** |
| 6 Entropy production | `statphys_v2_figs.py` → `sp2_fig_epr.png` | Schnakenberg σ(ρ)>0 ∀ρ; σ→0 as ρ→0; throughput J=λU_χ* |

Cover: `cover_statphys.py` → `cover_statphys.png`. Superseded exploratory figure: `sp_fig3_fss.png` (collapse), `sp2_fig_corr.png` (G(r), replaced by the FSS study).

## Finite-size-scaling study (Figure 5) — the new validation

**Setup:** site-diluted XY at h₀ = 0, T = 0.45 (so Nelson–Kosterlitz line 2T/π = 0.286); L = 32, 48, 64; 3 seeds; 260 equilibration + 260 measurement sweeps, sampled every 5. Measured order parameter U_χ, Binder cumulant U₄ = 1 − ⟨m⁴⟩/(3⟨m²⟩²), and helicity modulus Υ = (1/L²)⟨Σ_b J cos Δθ⟩ − (1/L²T)⟨(Σ_b J sin Δθ)²⟩ (x/y averaged). Runtime ≈ 43 s.

**Helicity modulus Υ(f)** (crosses 2T/π = 0.286 at):
- L=32: [0.875, 0.581, 0.353, 0.180, 0.046, 0.033, −0.016, −0.005] → f_KT = 0.231
- L=48: [0.874, 0.588, 0.387, 0.159, −0.035, 0.081, 0.030, −0.008] → f_KT = 0.235
- L=64: [0.873, 0.620, 0.293, 0.106, 0.087, −0.038, 0.038, 0.009] → f_KT = 0.203

**f_KT ≈ 0.22, essentially size-independent, well below the site-percolation value 1 − p_c ≈ 0.407.**

**Interpretation (and a correction to earlier drafts):** the field-free transition is **thermally (BKT) driven**, not percolation-controlled. Dilution lowers the effective BKT temperature below the operating T at f_KT ≈ 0.22, while the intact sub-lattice still percolates (percolation only fails at f = 0.407). The order parameter U_χ(f) steepens with L in the same range; the earlier G(r)-based estimate (f* ≈ 0.38) measured where residual correlations become small, a higher crossover than the true BKT point, and is superseded by this helicity-modulus determination. A precise Nelson–Kosterlitz extrapolation with logarithmic corrections (more sizes/seeds) remains as refinement.

## Status of claims
- Proved analytically: Theorem 1 (entropy bridge, with A′(κ) > (1−A²)/2 > 0 via Turán inequality).
- Exact: linear reduction I* = 1/(1+ρ) (β = 0), two-state master equation.
- Exact in mean-field / fluctuation-rounded in lattice: bistability (Prop 2 + Fig 4A).
- Validated numerically: NESS current balance (Fig 4B); BKT-driven transition f_KT ≈ 0.22 (Fig 5).
- Analytic on a modeled cycle: Schnakenberg EPR (Fig 6), reverse rate ε a regularization.

Single approximation: annealed mean-field closure 𝒟 ≐ I (finite-N breakdown quantified by Fig 4A).
