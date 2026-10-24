# Module 3 — Numerical Solutions of Differential Equations

[← MAD 4401 home](../README.md)

Module 3 develops numerical methods for initial-value problems in ordinary differential equations. The sequence begins with the geometry of an ODE, then builds Euler's method, studies its error, and improves accuracy with Taylor and Runge–Kutta methods. The final section introduces adaptive RK23.

## Start here

Work through the sections in order. Each notebook contains explanations, executable Python, plots, and short experiments.

| Section | Topic | View | Run in Colab | Launch JupyterLab |
|---|---|---|---|---|
| **1** | Direction Fields and Autonomous ODEs | [View notebook](01_direction_fields_autonomous_odes.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/01_direction_fields_autonomous_odes.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/01_direction_fields_autonomous_odes.ipynb) |
| **2** | Euler's Method | [View notebook](02_euler_method.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/02_euler_method.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/02_euler_method.ipynb) |
| **3** | Error in Euler's Method | [View notebook](03_euler_error.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/03_euler_error.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/03_euler_error.ipynb) |
| **4** | Higher-Order Taylor Methods | [View notebook](04_taylor_methods.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/04_taylor_methods.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/04_taylor_methods.ipynb) |
| **5** | Runge–Kutta Methods: RK2 and RK3 | [View notebook](05_rk2_rk3.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/05_rk2_rk3.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/05_rk2_rk3.ipynb) |
| **6** | Classical RK4 | [View notebook](06_rk4.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/06_rk4.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/06_rk4.ipynb) |
| **7** | Adaptive RK23 + Comparison of All Methods | [View notebook](07_rk23_and_method_comparison.ipynb) | [Run in Colab](https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/module_3/07_rk23_and_method_comparison.ipynb) | [Launch Binder](https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/module_3/07_rk23_and_method_comparison.ipynb) |

### Which option should I use?

- **View notebook** — read the notebook on GitHub without running code.
- **Run in Colab** — opens the notebook in Google Colab, where you can run the cells in your browser. If you want to save your changes, use **File → Save a copy in Drive**.
- **Launch Binder** — creates a temporary JupyterLab environment in your browser using the files and packages from this repository. Binder sessions are temporary, so download anything you want to keep before closing the session.

> **Where does the code run?** GitHub only stores the course files. Running a notebook in Colab or Binder does **not** run code on Dr. Harrington's GitHub account or computer, and it does not modify the course repository.

## Learning path

### Section 1 — Direction Fields and Autonomous ODEs
Interpret first-order ODEs, direction fields, autonomous equations, equilibria, and stability.

### Section 2 — Euler's Method
Build the first numerical IVP solver from the tangent-line idea.

### Section 3 — Error in Euler's Method
Study local and global error, convergence, and error bounds.

### Section 4 — Higher-Order Taylor Methods
Use additional Taylor terms to increase order, and see why derivative calculations become cumbersome.

### Section 5 — Runge–Kutta Methods: RK2 and RK3
Implement Improved Euler, midpoint RK2, and Heun's three-stage RK3. Compare error and observed convergence order.

### Section 6 — Classical RK4
Implement the four-stage classical Runge–Kutta method, reproduce the lecture example, and verify fourth-order convergence.

### Section 7 — Adaptive RK23 and Comparison of All Methods
Implement **Brin's adaptive RK2(3)** method from Section 6.5 of _Tea Time Numerical Analysis_. The notebook ends with one common-IVP comparison of Euler, Taylor 2/3, RK2, RK3, RK4, and adaptive RK23.

## References

The ODE sequence is organized using:

- Leon Q. Brin, _Tea Time Numerical Analysis_, Chapter 6, especially Sections 6.2–6.5.
- Richard L. Burden and J. Douglas Faires, _Numerical Analysis_, for standard Runge–Kutta notation, order, and error analysis.
- The course lecture notes in this repository/course site.

## Coming later

- Systems of ODEs
- Numerical methods and dynamical systems

---

[← MAD 4401 home](../README.md)
