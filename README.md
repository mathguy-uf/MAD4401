# MAD 4401 — Numerical Analysis

Welcome to the course repository for **MAD 4401: Numerical Analysis**.

This repository is organized as a guided set of modules rather than a file archive. Start with the module you are currently studying; each module page walks through the material in order and links directly to the notebooks.

## Course modules

| Module | Topic | Status | Start |
|---|---|---|---|
| **Module 1** | Foundations and Root Finding | Coming soon | [Open Module 1](module_1/README.md) |
| **Module 2** | Approximation and Numerical Calculus | Coming soon | [Open Module 2](module_2/README.md) |
| **Module 3** | Numerical Solutions of Differential Equations | **Available** | **[Start Module 3](module_3/README.md)** |

# How to use GitHub for this course

You can read the notebooks directly on GitHub, but if you want to **run the Python code on your own computer**, the easiest method is to clone this repository once and then use `git pull` whenever new course material is added.

## 1. Open a terminal

Use one of the following:

- **Windows:** PowerShell or Windows Terminal
- **macOS:** Terminal
- **Linux:** Terminal

The commands below work in all three environments.

## 2. Choose where you want the course files

First, use `cd` to move to the folder where you want to keep the course repository.

For example:

```bash
cd Documents
```

Useful navigation commands:

```bash
pwd
```

shows your current folder.

```bash
ls
```

shows the files and folders in your current location.

```bash
cd folder_name
```

moves into a folder.

```bash
cd ..
```

moves up one folder.

## 3. Clone the repository — do this only once

From the folder where you want MAD 4401 stored, run:

```bash
git clone https://github.com/mathguy-uf/MAD4401.git
```

Git will create a new folder named `MAD4401` containing the course files.

Now move into it:

```bash
cd MAD4401
```

## 4. Install the Python packages

From inside the `MAD4401` folder, run:

```bash
python -m pip install -r requirements.txt
```

You normally only need to do this the first time, unless the required packages change later in the semester.

## 5. Open the notebooks

Start Jupyter with:

```bash
jupyter lab
```

Your web browser should open automatically. From there, open the module folder and select the notebook you want to run.

For example, Module 3 is located in:

```text
module_3/
```

To stop Jupyter, return to the terminal and press:

```text
Ctrl+C
```

## 6. Get new course files later

You **do not need to clone the repository again**.

Open a terminal, move into your existing MAD4401 folder, and run:

```bash
cd MAD4401
git pull
```

`git pull` downloads the newest files and changes from the course repository.

A typical session might therefore look like:

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

## Using Google Colab instead

If you do not want to run Jupyter locally, the Module 3 page includes links that open the notebooks in **Google Colab**. This lets you run the notebook in your browser without cloning the repository or installing Python packages locally.

## Current material

Module 3 currently contains Sections 1–4:

1. Direction Fields and Autonomous ODEs
2. Euler's Method
3. Error in Euler's Method
4. Higher-Order Taylor Methods

Later sections will continue with Runge–Kutta methods, systems of ODEs, and dynamical-systems applications.

---

**Department of Mathematics — University of Florida**  
Course materials by Dr. Harrington.
