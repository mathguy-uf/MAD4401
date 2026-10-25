# Module 2 — Approximation, Interpolation, and Numerical Calculus

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)

Module 2 develops methods for approximating functions, data, derivatives, and integrals. The sequence follows the material emphasized in the course lectures, homework, review, and Exam 2.

The presentation uses **Eric Sullivan, _Numerical Methods: An Inquiry-Based Approach with Python_** for the computational viewpoint, together with **Leon Q. Brin, _Tea Time Numerical Analysis_** and **Burden & Faires, _Numerical Analysis_** for standard interpolation formulas, notation, and error analysis.

## Start here

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **1** | Lagrange Interpolation, Uniqueness, and Error | [View notebook](01_lagrange_interpolation.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/01_lagrange_interpolation.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/01_lagrange_interpolation.ipynb) |
| **2** | Degree-10 LIP vs. Degree-10 Taylor | [View notebook](02_lip_vs_taylor.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/02_lip_vs_taylor.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/02_lip_vs_taylor.ipynb) |
| **3** | Newton Divided Differences | [View notebook](03_newton_divided_differences.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/03_newton_divided_differences.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/03_newton_divided_differences.ipynb) |
| **4** | Neville's Method | [View notebook](04_neville_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/04_neville_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/04_neville_method.ipynb) |
| **5** | Least-Squares Best Fit and Normal Equations | [View notebook](05_least_squares_best_fit.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/05_least_squares_best_fit.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/05_least_squares_best_fit.ipynb) |
| **6** | Numerical Differentiation | [View notebook](06_numerical_differentiation.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/06_numerical_differentiation.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/06_numerical_differentiation.ipynb) |
| **7** | Riemann Sums | [View notebook](07_riemann_sums.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/07_riemann_sums.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/07_riemann_sums.ipynb) |
| **8** | Trapezoidal and Simpson's Rules | [View notebook](08_trapezoidal_simpson.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_2/08_trapezoidal_simpson.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_2/08_trapezoidal_simpson.ipynb) |

## Learning path

### Section 1 — Lagrange Interpolation, Uniqueness, and Error

Construct the Lagrange interpolating polynomial (LIP), evaluate it directly from the basis functions, prove uniqueness of the degree-at-most-$n$ interpolant, see why the actual degree can be smaller than $n$, and use the interpolation remainder to obtain a rigorous error bound.

### Section 2 — Degree-10 LIP vs. Degree-10 Taylor

Compare two degree-10 approximations to

$$
f(x)=\frac{1}{1+x^2},\qquad -1\le x\le1.
$$

The Taylor polynomial is centered at zero. The LIP uses 11 equally spaced nodes throughout the interval. The notebook compares both approximations and their errors, emphasizing that equal degree does not imply equal approximation quality.

### Section 3 — Newton Divided Differences

Build a divided-difference table and use its first row as the coefficients of the Newton interpolating polynomial. The worked example mirrors the type of table used on Exam 2.

### Section 4 — Neville's Method

Neville's Method is developed recursively, with the full triangular table explained entry by entry. It evaluates the same unique interpolating polynomial as Lagrange/Newton at a requested point without first constructing a symbolic polynomial.

### Section 5 — Least-Squares Best Fit and Normal Equations

Following Sullivan's optimization viewpoint, define residuals and minimize

$$
SS_{\mathrm{res}}=\sum_i(y_i-\hat y_i)^2.
$$

The notebook develops normal equations for linear and quadratic least-squares models, constrained course-style models, and the relationships among $SS_{\mathrm{res}}$, $SS_{\mathrm{reg}}$, $SS_{\mathrm{tot}}$, and $R^2$.

### Section 6 — Numerical Differentiation

Compare forward, backward, and centered finite differences. Taylor's theorem explains the formulas and their error orders. The notebook also connects interpolation back to differentiation by constructing a Newton polynomial and using $P'(x)$ to approximate a derivative.

### Section 7 — Riemann Sums

Use left, right, and midpoint rectangles to approximate definite integrals and compare first- and second-order behavior.

### Section 8 — Trapezoidal and Simpson's Rules

Move from piecewise constants to piecewise linear and quadratic approximations. Implement single and composite trapezoidal and Simpson rules, apply the course error formulas, compare convergence orders, and solve for the number of subintervals needed to guarantee a requested tolerance.

## Exam 2 / review checklist

Students should be comfortable with:

- Lagrange interpolation and interpolation error;
- uniqueness of the degree-at-most-$n$ interpolating polynomial;
- the distinction between degree $n$ and degree **at most** $n$;
- Newton divided differences and divided-difference tables;
- Neville's Method and its recursive table;
- least-squares normal equations for lines and quadratics;
- constrained best-fit models;
- residuals, $SS_{\mathrm{res}}$, $SS_{\mathrm{reg}}$, $SS_{\mathrm{tot}}$, and $R^2$;
- forward, backward, and centered finite differences;
- differentiating an interpolation polynomial;
- Riemann sums;
- trapezoidal and composite trapezoidal rules;
- Simpson's and composite Simpson's rules;
- theoretical error bounds;
- choosing $n$ from an integration error tolerance;
- observed convergence order.

---

[← MAD 4401 home](../README.md) · [Student Git/GitHub Guide](../GITHUB_GUIDE.md)
