# Module 1 — Foundations, Error, and Root Finding

[← MAD 4401 home](../README.md)

Module 1 develops the mathematical and computational foundations used throughout numerical analysis. The sequence follows the material emphasized in the course lectures and Exam 1: Taylor approximation and error, finite-precision arithmetic, root finding, fixed-point iteration, Newton's method, and order of convergence.

The presentation follows **Leon Q. Brin, _Tea Time Numerical Analysis_** and **Burden & Faires, _Numerical Analysis_**. The algorithms use the course notation $p_n$, `TOL`, and iteration histories, and the Python code is written in PEP 8 style.

## Start here

Work through the sections in order. Each notebook can be read on GitHub or run directly in a browser.

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **1** | Taylor Series and Error | [View notebook](01_taylor_series.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/01_taylor_series.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/01_taylor_series.ipynb) |
| **2** | Numerical Error and Floating-Point Arithmetic | [View notebook](02_floating_point_and_error.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/02_floating_point_and_error.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/02_floating_point_and_error.ipynb) |
| **3** | Bisection Method | [View notebook](03_bisection_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/03_bisection_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/03_bisection_method.ipynb) |
| **4** | Fixed-Point Iteration and Cobweb Diagrams | [View notebook](04_fixed_point_cobwebs.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/04_fixed_point_cobwebs.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/04_fixed_point_cobwebs.ipynb) |
| **5** | Newton's Method | [View notebook](05_newton_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/05_newton_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/05_newton_method.ipynb) |
| **6** | Order and Rate of Convergence | [View notebook](06_order_of_convergence.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/06_order_of_convergence.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/06_order_of_convergence.ipynb) |

## Learning path

### Section 1 — Taylor Series and Error

This notebook is deliberately **only about Taylor approximation**. It develops $P_n(x)$, the Lagrange remainder, approximation of $\ln(x)$, rigorous error bounds, and the question of how many terms are required for a specified tolerance.

### Section 2 — Numerical Error and Floating-Point Arithmetic

Study absolute and relative error, decimal chopping and rounding, IEEE-754 binary64 representation, and loss of significance. The cancellation example shows why algebraically equivalent formulas can behave very differently on a computer.

### Section 3 — Bisection Method

Use the Intermediate Value Theorem to bracket a root, implement bisection, track $a_n$, $b_n$, and $p_n$, and use the bisection error bound to determine the number of iterations needed for a tolerance.

### Section 4 — Fixed-Point Iteration and Cobweb Diagrams

This notebook emphasizes the geometry of fixed-point iteration. It uses the course example

$$
g(x)=\frac{5}{x+4}
$$

with $p_0=1.5$, builds the iteration table, draws the cobweb diagram, checks the hypotheses of the Fixed-Point Theorem, and uses the contraction estimate to predict the number of iterations.

### Section 5 — Newton's Method

Derive Newton's method from tangent lines, implement the iteration, visualize the first tangent steps, and discuss why Newton's method can fail even though it is usually much faster than bisection near a simple root.

### Section 6 — Order and Rate of Convergence

Use actual iteration errors to distinguish linear from quadratic convergence. The fixed-point example demonstrates linear convergence and its asymptotic constant, while Newton's method demonstrates quadratic convergence.

## Course alignment

These notebooks are intended to support—not replace—the lecture notes. In particular, students should be comfortable with:

- Taylor polynomials and remainder/error bounds;
- absolute and relative error;
- chopping, rounding, and IEEE-754 binary64;
- the Intermediate Value Theorem and bisection;
- the Fixed-Point Theorem and its convergence bound;
- cobweb diagrams;
- Newton's method and possible failure modes;
- order of convergence and asymptotic error constants.

---

[← MAD 4401 home](../README.md)
