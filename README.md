# MAD 4401 — Numerical Analysis

Welcome to the course repository for **MAD 4401: Numerical Analysis**.

This repository is organized as a guided set of modules rather than a file archive. Each module page walks through the material in order and links directly to executable notebooks.

## Course modules

| Module | Topic | Status | Start |
|---|---|---|---|
| **Module 1** | Foundations, Error, and Root Finding | **Available** | **[Start Module 1](module_1/README.md)** |
| **Module 2** | Approximation, Interpolation, and Numerical Calculus | **Available** | **[Start Module 2](module_2/README.md)** |
| **Module 3** | Initial-Value Problems and Numerical ODEs | **Available** | **[Start Module 3](module_3/README.md)** |

# How to use GitHub for this course

You can read notebooks directly on GitHub. To run the Python code locally, clone the repository once and then use `git pull` whenever course material is updated.

## First time only

```bash
cd Documents
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
python -m pip install -r requirements.txt
jupyter lab
```

## Later course sessions

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

Useful commands:

| Command | What it does |
|---|---|
| `pwd` | Shows your current folder |
| `ls` | Lists files and folders |
| `cd folder_name` | Moves into a folder |
| `cd ..` | Moves up one folder |
| `git clone URL` | Makes your first local copy |
| `git pull` | Gets the latest course updates |
| `git status` | Shows local changes |
| `jupyter lab` | Opens JupyterLab |

If you edit a course notebook, Git may report that your local file has changed. Make a copy first if you want to preserve your work. Students normally need `git pull`, not `git push`.

## Browser-based options

All three module pages include **Google Colab** and **Binder/JupyterLab** links. These run notebooks in hosted browser environments. They do not run code on the instructor's GitHub account or computer.

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

The course notebooks use **Eric Sullivan's _Numerical Methods: An Inquiry-Based Approach with Python_**, **Leon Q. Brin's _Tea Time Numerical Analysis_**, and **Burden & Faires, _Numerical Analysis_** as references for computational presentation, notation, algorithms, and error analysis.

---

**Department of Mathematics — University of Florida**  
Course materials by Dr. Harrington.
