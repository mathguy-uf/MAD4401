# Module 3 — Numerical Solutions of Differential Equations

[← MAD 4401 home](../README.md)

Module 3 begins with the theory that makes an initial-value problem meaningful, then moves from qualitative geometry to Euler, Taylor, Runge–Kutta, and adaptive methods.

## Start here

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **0** | IVP Foundations: Existence, Uniqueness, and Well-Posedness | [View notebook](00_ivp_foundations.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/00_ivp_foundations.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/00_ivp_foundations.ipynb) |
| **1** | Direction Fields and Autonomous ODEs | [View notebook](01_direction_fields_autonomous_odes.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/01_direction_fields_autonomous_odes.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/01_direction_fields_autonomous_odes.ipynb) |
| **2** | Euler's Method | [View notebook](02_euler_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/02_euler_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/02_euler_method.ipynb) |
| **3** | Error in Euler's Method | [View notebook](03_euler_error.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/03_euler_error.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/03_euler_error.ipynb) |
| **4** | Taylor Methods: Orders 2, 3, and 4 | [View notebook](04_taylor_methods.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/04_taylor_methods.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/04_taylor_methods.ipynb) |
| **5** | Runge–Kutta Methods: RK2 and RK3 | [View notebook](05_rk2_rk3.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/05_rk2_rk3.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/05_rk2_rk3.ipynb) |
| **6** | Classical RK4 | [View notebook](06_rk4.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/06_rk4.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/06_rk4.ipynb) |
| **7** | Adaptive RK23 + Comparison of All Methods | [View notebook](07_rk23_and_method_comparison.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/07_rk23_and_method_comparison.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/07_rk23_and_method_comparison.ipynb) |

### Which option should I use?

- **View notebook** — read the notebook on GitHub without running code.
- **Run in Colab** — run the notebook in Google Colab.
- **Launch Binder** — create a temporary JupyterLab environment in the browser.

> GitHub stores the files. Colab and Binder execute code in their own hosted environments; they do not run code on the instructor's GitHub account or computer.

## Learning path

### Section 0 — IVP Foundations
Check continuity, Lipschitz conditions, existence and uniqueness, perturbations, and well-posedness before applying a numerical solver.

### Section 1 — Direction Fields and Autonomous ODEs
Interpret direction fields, autonomous equations, equilibria, stability, and basins of attraction.

### Section 2 — Euler's Method
Build the tangent-line method and connect Euler-generated data back to interpolation.

### Section 3 — Error in Euler's Method
Study one-step defects, local truncation error, global error, and error bounds.

### Section 4 — Higher-Order Taylor Methods
Use Taylor methods of orders 2, 3, and 4 and compute Taylor-2 local truncation error.

### Section 5 — RK2 and RK3
Implement Improved Euler, midpoint RK2, and Heun's three-stage RK3.

### Section 6 — Classical RK4
Implement the four-stage classical Runge–Kutta method and verify fourth-order convergence.

### Section 7 — Adaptive RK23 and Method Comparison
Implement Brin's adaptive RK2(3) method and compare Euler, Taylor 2/3/4, RK2, RK3, RK4, and adaptive RK23 on a common IVP.

## References

- Leon Q. Brin, _Tea Time Numerical Analysis_, Chapter 6.
- Richard L. Burden and J. Douglas Faires, _Numerical Analysis_.
- MAD 4401 lecture notes and Exam 3 review.

---

[← MAD 4401 home](../README.md)
