# Module 3 — Numerical Solutions of Differential Equations

[← MAD 4401 home](../README.md)

Module 3 develops numerical methods for initial-value problems in ordinary differential equations. The sequence begins with the geometry of an ODE, then builds Euler's method, studies its error, and improves accuracy with higher-order Taylor methods.

## Start here

Work through the sections in order. Each notebook contains explanations, executable Python, plots, and short experiments.

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **1** | Direction Fields and Autonomous ODEs | [View notebook](01_direction_fields_autonomous_odes.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/01_direction_fields_autonomous_odes.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/01_direction_fields_autonomous_odes.ipynb) |
| **2** | Euler's Method | [View notebook](02_euler_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/02_euler_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/02_euler_method.ipynb) |
| **3** | Error in Euler's Method | [View notebook](03_euler_error.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/03_euler_error.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/03_euler_error.ipynb) |
| **4** | Higher-Order Taylor Methods | [View notebook](04_taylor_methods.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/04_taylor_methods.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/04_taylor_methods.ipynb) |

### Which option should I use?

- **View notebook** — read the notebook on GitHub without running code.
- **Run in Colab** — opens the notebook in Google Colab, where you can run the cells in your browser. If you want to save your changes, use **File → Save a copy in Drive**.
- **Launch Binder** — creates a temporary JupyterLab environment in your browser using the files and packages from this repository. Binder sessions are temporary, so download anything you want to keep before closing the session.

> **Where does the code run?** GitHub only stores the course files. Running a notebook in Colab or Binder does **not** run code on Dr. Harrington's GitHub account or computer, and it does not modify the course repository. Colab runs code in a Google-hosted virtual machine associated with your session. Binder creates a temporary cloud environment from the public repository.

## Learning path

### Section 1 — Direction Fields and Autonomous ODEs

Start with the qualitative picture. You will interpret a first-order ODE, construct a direction field, identify equilibria of an autonomous equation, and classify equilibria as stable or unstable. The notebook uses

\[
y' = y-y^3
\]

to show two attracting equilibria and one repelling equilibrium in a single example. It also introduces the one-dimensional stable/unstable sets that lead to stable and unstable manifolds for systems.

### Section 2 — Euler's Method

Turn the geometric tangent-line idea into an algorithm:

\[
w_{n+1}=w_n+h f(t_n,w_n).
\]

You will implement Euler's method from scratch and compare the numerical approximation with an exact solution.

### Section 3 — Error in Euler's Method

Study how one-step errors accumulate. You will distinguish the one-step defect from the scaled local truncation error, measure global error numerically, estimate convergence order, and compare actual error with the theoretical global error bound.

### Section 4 — Higher-Order Taylor Methods

Use additional terms from the Taylor expansion to improve accuracy. You will implement second- and third-order Taylor methods, compare them with Euler's method, and see why Runge–Kutta methods are the natural next step.

## Coming next

- Section 5 — Runge–Kutta Methods
- Section 6 — Systems of ODEs
- Section 7 — Numerical Methods Meet Dynamical Systems

---

[← MAD 4401 home](../README.md)
