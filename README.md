# MAD 4401 — Numerical Analysis

This repository contains student-facing course resources for **MAD 4401: Numerical Analysis** at the University of Florida.

The repository is organized as a guided set of modules rather than a file archive. Each module page walks through the material in order and links directly to executable notebooks.

## Course website

The primary student interface is the GitHub Pages course site:

**https://mathguy-uf.github.io/MAD4401/**

Students should normally begin there rather than browsing the repository file tree.

## Start here

New to Git, GitHub, Jupyter, Colab, or Binder?

See **[START_HERE.md](START_HERE.md)** for the short course setup and **[GITHUB_GUIDE.md](GITHUB_GUIDE.md)** for the detailed student Git guide.

## Course modules

| Module | Topic | Status | Start |
|---|---|---|---|
| **Module 1** | Foundations, Error, and Root Finding | **Available** | **[Start Module 1](module_1/README.md)** |
| **Module 2** | Approximation, Interpolation, and Numerical Calculus | **Available** | **[Start Module 2](module_2/README.md)** |
| **Module 3** | Initial-Value Problems and Numerical ODEs | **Available** | **[Start Module 3](module_3/README.md)** |

## Three ways to use notebooks

Every module offers the same three options:

1. **View on GitHub** — read the notebook and saved output.
2. **Run in Colab** — execute one notebook in Google Colab.
3. **Launch Binder** — open the repository in a temporary JupyterLab environment.

For repeated local use, clone the repository once:

```bash
cd Documents
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
python -m pip install -r requirements.txt
jupyter lab
```

Later:

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

For normal course use, the most important Git commands are:

```bash
git clone https://github.com/mathguy-uf/MAD4401.git
git pull
git status
```

Students normally need `git pull`, not `git push`.

## Current material

### Module 1

1. Taylor Series and Error
2. Numerical Error and Floating-Point Arithmetic
3. Bisection Method and Supporting Theorems
4. Fixed-Point Iteration and Cobweb Diagrams
5. Newton's Method
6. Big-O, Order, and Rate of Convergence

### Module 2

1. Lagrange Interpolation, Uniqueness, and Error
2. Degree-10 LIP vs. Degree-10 Taylor
3. Newton Divided Differences
4. Neville's Method
5. Least-Squares Best Fit and Normal Equations
6. Numerical Differentiation
7. Riemann Sums
8. Trapezoidal and Simpson's Rules

### Module 3

0. IVP Foundations: Lipschitz, Existence/Uniqueness, and Well-Posedness
1. Direction Fields and Autonomous ODEs
2. Euler's Method
3. Error in Euler's Method
4. Taylor Methods of Orders 2, 3, and 4
5. Runge–Kutta Methods: RK2 and RK3
6. Classical RK4
7. Adaptive RK23 and Comparison of All Methods

## References

The course notebooks use **Eric Sullivan's _Numerical Methods: An Inquiry-Based Approach with Python_**, **Leon Q. Brin's _Tea Time Numerical Analysis_**, and **Burden & Faires, _Numerical Analysis_** as references for computational presentation, notation, algorithms, and error analysis.

---

**Department of Mathematics — University of Florida**  
Course materials by Dr. Harrington.
