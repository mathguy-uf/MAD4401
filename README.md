# MAD 4401 — Numerical Analysis

Welcome to the course repository for **MAD 4401: Numerical Analysis**.

This repository is organized as a guided set of modules rather than a file archive. Start with the module you are currently studying; each module page walks through the material in order and links directly to the notebooks.

## Course modules

| Module | Topic | Status | Start |
|---|---|---|---|
| **Module 1** | Foundations, Error, and Root Finding | **Available** | **[Start Module 1](module_1/README.md)** |
| **Module 2** | Approximation, Interpolation, and Numerical Calculus | **Available** | **[Start Module 2](module_2/README.md)** |
| **Module 3** | Numerical Solutions of Differential Equations | **Available** | **[Start Module 3](module_3/README.md)** |

# How to use GitHub for this course

You can read the notebooks directly on GitHub, but if you want to **run the Python code on your own computer**, the easiest method is to clone this repository once and then use `git pull` whenever new course material is added.

## 1. Open a terminal

- **Windows:** PowerShell or Windows Terminal
- **macOS:** Terminal
- **Linux:** Terminal

## 2. Choose where you want the course files

```bash
cd Documents
```

Useful navigation commands:

```bash
pwd
ls
cd folder_name
cd ..
```

## 3. Clone the repository — do this only once

```bash
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
```

## 4. Install the Python packages

```bash
python -m pip install -r requirements.txt
```

## 5. Open the notebooks

```bash
jupyter lab
```

To stop Jupyter, return to the terminal and press `Ctrl+C`.

## 6. Get new course files later

You **do not need to clone the repository again**.

```bash
cd MAD4401
git pull
```

A typical session might look like:

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

## Important Git commands for this course

| Command | What it does |
|---|---|
| `git clone URL` | Makes your first local copy of the repository |
| `git pull` | Gets the latest course updates |
| `git status` | Shows whether files in your local copy have been changed |
| `pwd` | Shows your current folder |
| `ls` | Lists files and folders |
| `cd folder_name` | Moves into a folder |
| `cd ..` | Moves up one folder |
| `jupyter lab` | Opens Jupyter Lab |

### A note about changing notebooks

If you experiment with a notebook, Git may report that your local file has been modified. That is normal. If you want to preserve your work, make a copy of the notebook before editing it.

You do **not** need to use `git push` for this course. `git pull` is the command you will normally use to receive new material from the instructor repository.

## Browser-based options

All three module pages include **Google Colab** and **Binder/JupyterLab** launch links. These let you run notebooks in the browser without running code on the instructor's GitHub account or computer.

## Current material

### Module 1

1. Taylor Series and Error
2. Numerical Error and Floating-Point Arithmetic
3. Bisection Method
4. Fixed-Point Iteration and Cobweb Diagrams
5. Newton's Method
6. Order and Rate of Convergence

### Module 2

1. Lagrange Interpolation and Error
2. Degree-10 LIP vs. Degree-10 Taylor
3. Newton Divided Differences
4. Neville's Method
5. Least-Squares Best Fit
6. Numerical Differentiation
7. Riemann Sums
8. Trapezoidal and Simpson's Rules

### Module 3

1. Direction Fields and Autonomous ODEs
2. Euler's Method
3. Error in Euler's Method
4. Higher-Order Taylor Methods
5. Runge–Kutta Methods: RK2 and RK3
6. Classical RK4
7. Adaptive RK23 and Comparison of All Methods

The course notebooks use **Eric Sullivan's _Numerical Methods: An Inquiry-Based Approach with Python_**, **Leon Q. Brin's _Tea Time Numerical Analysis_**, and **Burden & Faires, _Numerical Analysis_** as references for computational presentation, notation, algorithms, and error analysis.

---

**Department of Mathematics — University of Florida**  
Course materials by Dr. Harrington.
