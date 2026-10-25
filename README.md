# MAD 4401 — Numerical Analysis

Welcome to the course repository for **MAD 4401: Numerical Analysis**.

This repository is organized as a guided set of modules rather than a file archive. Each module page walks through the material in order and links directly to executable notebooks.

## Course modules

| Module | Topic | Status | Start |
|---|---|---|---|
| **Module 1** | Foundations, Error, and Root Finding | **Available** | **[Start Module 1](module_1/README.md)** |
| **Module 2** | Approximation, Interpolation, and Numerical Calculus | **Available** | **[Start Module 2](module_2/README.md)** |
| **Module 3** | Initial-Value Problems and Numerical ODEs | **Available** | **[Start Module 3](module_3/README.md)** |

# New to GitHub?

You do **not** need to know advanced Git to use this course repository.

Start with the **[Student Guide to Git and GitHub](GITHUB_GUIDE.md)**. It explains:

- what Git, GitHub, and JupyterLab each do;
- how to clone the course repository;
- how to use `git pull` to get new material;
- how to use `git status` to see local changes;
- how to protect work you have done in a notebook;
- what to do when `git pull` reports a conflict with local changes;
- how to use Colab or Binder instead of installing Python locally.

For normal course use, the most important Git commands are:

```bash
git clone https://github.com/mathguy-uf/MAD4401.git
git pull
git status
```

## First-time local setup

```bash
cd Documents
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
python -m pip install -r requirements.txt
jupyter lab
```

If your system does not recognize `python`, try `python3` or `py`.

## Normal class-day workflow

After the repository has been cloned once:

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

Do **not** clone the repository again every time new material is posted.

## Useful commands

| Command | What it does |
|---|---|
| `pwd` | Shows your current folder |
| `ls` | Lists files and folders |
| `cd folder_name` | Moves into a folder |
| `cd ..` | Moves up one folder |
| `git clone URL` | Makes your first local copy |
| `git pull` | Gets the latest course updates |
| `git status` | Shows local changes |
| `git restore FILE` | Restores the instructor version of a file; use carefully |
| `jupyter lab` | Opens JupyterLab |

If you edit a course notebook, Git may report that your local file has changed. That is normal. The safest habit is to make a personal copy before experimenting with a course notebook. Students normally need `git pull`, not `git push`.

## Browser-based options

All three module pages include **Google Colab** and **Binder/JupyterLab** links.

- **View notebook** — read the notebook on GitHub.
- **Run in Colab** — execute it in a Google-hosted browser session.
- **Launch Binder** — execute it in a temporary JupyterLab environment.

These services do **not** run code on the instructor's GitHub account or computer, and they do not modify the course repository.

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
