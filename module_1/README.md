# Module 1 — Foundations, Error, and Root Finding

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)

Module 1 develops the mathematical and computational foundations used throughout numerical analysis. The sequence follows the material emphasized in the course lectures and Exam 1: Taylor approximation and error, finite-precision arithmetic, root finding, fixed-point iteration, Newton's method, and convergence.

The presentation follows **Leon Q. Brin, _Tea Time Numerical Analysis_** and **Burden & Faires, _Numerical Analysis_**. The algorithms use the course notation $p_n$, `TOL`, and iteration histories, and the Python code is written in PEP 8 style.

## Start here

Work through the sections in order. Each notebook can be read on GitHub or run directly in a browser.

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **1** | Taylor Series and Error | [View notebook](01_taylor_series.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/01_taylor_series.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/01_taylor_series.ipynb) |
| **2** | Numerical Error and Floating-Point Arithmetic | [View notebook](02_floating_point_and_error.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/02_floating_point_and_error.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/02_floating_point_and_error.ipynb) |
| **3** | Bisection Method and Supporting Theorems | [View notebook](03_bisection_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/03_bisection_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/03_bisection_method.ipynb) |
| **4** | Fixed-Point Iteration and Cobweb Diagrams | [View notebook](04_fixed_point_cobwebs.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/04_fixed_point_cobwebs.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/04_fixed_point_cobwebs.ipynb) |
| **5** | Newton's Method | [View notebook](05_newton_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/05_newton_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/05_newton_method.ipynb) |
| **6** | Big-O, Order, and Rate of Convergence | [View notebook](06_order_of_convergence.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_1/06_order_of_convergence.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_1/06_order_of_convergence.ipynb) |

## Learning path

### Section 1 — Taylor Series and Error

This notebook is deliberately **only about Taylor approximation**. It develops $P_n(x)$, the Lagrange remainder, approximation of $\ln(x)$, rigorous error bounds, and the question of how many terms are required for a specified tolerance.

### Section 2 — Numerical Error and Floating-Point Arithmetic

Begin with the **Burden & Faires finite-digit machine model** before moving to IEEE-754. The notebook introduces normalized decimal machine numbers and $\operatorname{fl}(x)$, shows chopping and rounding after every operation, and demonstrates that associativity and distributivity can fail in finite arithmetic. It then develops IEEE-754 binary64, the next representable machine number, ULP spacing, absolute/relative error, loss of significance, and algebraic reformulation to reduce numerical error.

### Section 3 — Bisection Method and Supporting Theorems

Use the Intermediate Value Theorem to establish root existence, distinguish existence from uniqueness, use monotonicity/Rolle-style arguments when appropriate, implement bisection, track $a_n$, $b_n$, and $p_n$, and use the bisection error bound to determine the number of iterations needed for a tolerance.

### Section 4 — Fixed-Point Iteration and Cobweb Diagrams

This notebook emphasizes the geometry of fixed-point iteration. It uses the course example

$$
g(x)=\frac{5}{x+4}
$$

with $p_0=1.5$, builds the iteration table, draws the cobweb diagram, checks the hypotheses of the Fixed-Point Theorem, and uses the contraction estimate to predict the number of iterations.

### Section 5 — Newton's Method

Derive Newton's method from tangent lines, implement the iteration, visualize the first tangent steps, and discuss why Newton's method can fail even though it is usually much faster than bisection near a simple root.

### Section 6 — Big-O, Order, and Rate of Convergence

Begin with Big-$O$ descriptions for sequences and functions, then use actual iteration errors to distinguish linear from quadratic convergence. The fixed-point example demonstrates linear convergence and its asymptotic constant, while Newton's method demonstrates quadratic convergence.

## Exam 1 / review checklist

Students should be comfortable with:

- Taylor polynomials and Lagrange remainder/error bounds;
- choosing a Taylor degree for a required tolerance;
- absolute and relative error;
- normalized finite-digit floating-point notation and $\operatorname{fl}(x)$;
- chopping and rounding after **each** operation;
- examples where finite arithmetic changes algebraic identities;
- IEEE-754 binary64 and the next representable machine number;
- ULP spacing and loss of significance;
- reorganizing formulas to reduce numerical error;
- relative-error interval problems;
- the Intermediate Value Theorem, root existence, and uniqueness arguments;
- bisection and its error/iteration bound;
- the Fixed-Point Theorem and its convergence bound;
- cobweb diagrams;
- Newton's method and possible failure modes;
- Big-$O$ rate of convergence;
- order of convergence and asymptotic error constants.

---

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)
