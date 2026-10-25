# Module 3 — Numerical Solutions of Differential Equations

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)

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

- **View notebook** — read the explanation, code, and saved output on GitHub.
- **Run in Colab** — run or modify the notebook in Google Colab.
- **Launch Binder** — create a temporary JupyterLab environment in the browser.

> GitHub stores the files. Colab and Binder execute code in their own hosted environments; they do not run code on the instructor's GitHub account or computer.

## Learning path

### Section 0 — IVP Foundations

Check continuity, Lipschitz conditions, Lipschitz constants, existence and uniqueness, perturbations, and well-posedness before applying a numerical solver.

### Section 1 — Direction Fields and Autonomous ODEs

Interpret direction fields, autonomous equations, equilibria, stability, and basins of attraction. This provides the qualitative picture that numerical methods will later approximate.

### Section 2 — Euler's Method

Build the tangent-line method, implement Euler's method from scratch, and connect Euler-generated data back to interpolation.

### Section 3 — Error in Euler's Method

Study one-step defects, local truncation error, global error, convergence, and theoretical error bounds.

### Section 4 — Higher-Order Taylor Methods

Use Taylor methods of orders 2, 3, and 4, compute Taylor-2 local truncation error, and compare observed convergence orders.

### Section 5 — RK2 and RK3

Implement Improved Euler, midpoint RK2, and Heun's three-stage RK3, with convergence comparisons.

### Section 6 — Classical RK4

Implement the four-stage classical Runge–Kutta method, reproduce a lecture-style example, and verify fourth-order convergence.

### Section 7 — Adaptive RK23 and Method Comparison

Implement **Brin's adaptive RK2(3)** method and compare Euler, Taylor 2/3/4, RK2, RK3, RK4, and adaptive RK23 on a common IVP. This final notebook is intended to show the tradeoff among order, error, work, and adaptive step size.

## Exam 3 / review checklist

Students should be comfortable with:

- identifying an IVP and its initial condition;
- continuity and Lipschitz conditions;
- estimating a Lipschitz constant;
- existence, uniqueness, perturbations, and well-posedness;
- reading direction fields;
- autonomous equations, equilibrium solutions, and stability;
- Euler's method;
- using Euler-generated values as interpolation data;
- one-step defects, local truncation error, and global error;
- Euler error bounds;
- Taylor methods of orders 2, 3, and 4;
- Taylor-2 local truncation error;
- Improved Euler / Heun RK2;
- midpoint RK2;
- Heun's three-stage RK3;
- classical RK4;
- adaptive RK23;
- comparing methods by error and observed order of convergence.

## References

- Leon Q. Brin, _Tea Time Numerical Analysis_, Chapter 6.
- Richard L. Burden and J. Douglas Faires, _Numerical Analysis_.
- MAD 4401 lecture notes and Exam 3 review.

---

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)
