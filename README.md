# Theory of the Static Monolith (v1.9)
**A Mechanical Framework for Gravity and Quantum Vacuum Capacity**

[![Zenodo](https://img.shields.io/badge/Zenodo-DOI%2010.5281%2Fzenodo.19435163-blue)](https://doi.org/10.5281/zenodo.19435163)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌌 Abstract
The Static Monolith Theory proposes that space-time is not a void but a high-tension medium (Quantum Foam). Gravity is redefined as a mechanical gradient of the local vacuum capacity ($\Phi$), where mass represents an energy "debt" that locally depletes this capacity.

## 🚀 Key Benchmarks (Verified Predictions)
All predictions are calculated using a single, universal stress constant $\kappa = 7.42 \times 10^{-28} \, \text{m/kg}$, derived from Earth's GPS time dilation data.

| Phenomenon | Monolith Prediction | Observed Value | Verification Script |
| :--- | :--- | :--- | :--- |
| **Mercury Perihelion Drift** | **42.98''** / century | 43.1'' (Standard) | `mercury_precession.py` |
| **Light Deflection (Sun)** | **1.7499''** | 1.75'' (Eddington) | `sun_light_bending.py` |
| **Lunar Time Dilation*** | **56.02 mus** / day | 56.4 mus (NASA/LTC) | `moon_time_dilation.py` |

*\*Calculation includes Earth's rotation, Moon's orbital velocity, and the mass of all three bodies.*
### 🎥 New: Interactive Simulation of the "Dark Matter Illusion"
Standard cosmology uses Dark Matter to explain flat galactic rotation curves. The Static Monolith Theory (v1.9) predicts that this flat curve is not caused by invisible mass, but is an **optical-metric illusion** caused by the observer's position within a gravitational debt.

I have created an N-body simulation (`monolith_v4_dynamic_observer.py`) that models this exact effect without using any Dark Matter.

* **Left panel (Physical Reality):** Stars orbit exclusively according to Newton's laws. The observer (Earth) is moving in an elliptical orbit deep within the central energy debt.
* **Right panel (Observed Rotation Curve):** The model calculates the Coefficient of Relative Perception ($S = \Phi_{source} / \Phi_{observer}$). As our local time and meter deform, the observed speeds of peripheral stars optically decouple from the Newtonian curve, perfectly simulating the flat curve conventionally attributed to Dark Matter.

[**Watch the video proof here (dark_matter_illusion_sim.mp4)**](./dark_matter_illusion_sim.mp4)

*Try it yourself by running the Python script in this repository.*
## 🛠 How to Verify
This repository provides independent Python scripts to verify each benchmark. No complex libraries are required, only standard `numpy`.

1. **Clone the repo:** `git clone https://github.com/karelpichler-lang/static-monolith-theory.git`
2. **Run verification:** `python mercury_precession.py`

## 🧪 Core Mechanics
The local vacuum capacity $\Phi$ follows a non-linear exponential decay based on the mass distribution:
$$\Phi_{local} = \exp\left(-\sum \frac{\kappa \cdot m_i}{r_i}\right)$$

In this model, the effective gravitational acceleration is modified by the vacuum capacity:
$$\vec{a} = \vec{a}_{newton} \cdot \frac{1}{\Phi^3}$$

## 🤝 Call for Collaboration
I am seeking developers and physicists to help implement this $\Phi$ gradient-based gravity law into:
* **N-Body Simulators** (to test galactic rotation curves without Dark Matter).
* **Relativistic Hydrodynamics** simulations.

---
**Full Documentation:** [Project Website](https://sites.google.com/view/61plusminus)  
**Contact:** karelpichler@gmail.com
 
