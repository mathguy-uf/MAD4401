# Runge–Kutta lecture notes

[← Module 3](../README.md)

Dr. Harrington's geometric introduction builds on Euler, Improved Euler, and
higher-order Taylor methods, then develops RK2 weights and the four stages of RK4.

- [Read the lecture slides (PDF)](M12_RK_Geometric_Introduction.pdf)
- [Download or inspect the LaTeX source](M12_RK_Geometric_Introduction.tex)
- [Practice RK2 and RK3 in Python](../05_rk2_rk3.ipynb)
- [Practice classical RK4 in Python](../06_rk4.ipynb)
- [Continue separately to adaptive RK2(3)](../07_rk23_and_method_comparison.ipynb)

The examples start with $y'=1+2t$ and $y'=y$, then work a full RK4 step for
$y'=-2ty^2$. The slides distinguish slopes from increments, trial points from the
final update, and one-step error from local truncation error divided by $h$.

## Compile the slides

Use a LaTeX installation containing Beamer, the Madrid theme, AMS packages,
Booktabs, and TikZ. All diagrams are drawn in TikZ; no external images are needed.
From this directory, run twice:

```bash
pdflatex M12_RK_Geometric_Introduction.tex
pdflatex M12_RK_Geometric_Introduction.tex
```
