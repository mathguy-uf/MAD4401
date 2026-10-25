# Start Here — MAD 4401 Numerical Analysis

Welcome to **MAD 4401: Numerical Analysis**.

The easiest way to use the course material is the student website:

**https://mathguy-uf.github.io/MAD4401/**

The site organizes the course into three modules and gives you three ways to use each notebook:

1. **View on GitHub** — read the notebook and its saved output.
2. **Run in Colab** — execute one notebook in your browser.
3. **Launch Binder** — open the course in a temporary JupyterLab environment.

## Course modules

- **Module 1 — Foundations, Error, and Root Finding**
- **Module 2 — Approximation, Interpolation, and Numerical Calculus**
- **Module 3 — Initial-Value Problems and Numerical ODEs**

## If you want the course on your computer

Clone the repository once:

```bash
cd Documents
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
python -m pip install -r requirements.txt
jupyter lab
```

On later class days, do **not** clone it again. Update your copy instead:

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

The three Git commands you will use most often are:

```bash
git clone <repository-url>
git pull
git status
```

## Need more Git help?

See the **[Student Guide to Git and GitHub](GITHUB_GUIDE.md)** for:

- Git, GitHub, JupyterLab, Colab, and Binder;
- terminal navigation;
- first-time setup;
- `git pull` and `git status`;
- protecting work you have done in a notebook;
- what to do when local changes prevent a pull;
- `git stash` and `git restore`;
- common troubleshooting.

## A useful habit

Before experimenting heavily with a course notebook, make a personal copy. This keeps your work separate from the instructor copy that Git updates.

For example:

```text
04_fixed_point_cobwebs.ipynb
04_fixed_point_cobwebs_yourname.ipynb
```

## Where to go next

- [Open Module 1](module_1/README.md)
- [Open Module 2](module_2/README.md)
- [Open Module 3](module_3/README.md)
- [Back to the repository README](README.md)

---

**Department of Mathematics — University of Florida**  
MAD 4401 course materials by Dr. Harrington.
