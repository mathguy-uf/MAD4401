# Student Guide to Git and GitHub for MAD 4401

[← Back to the MAD 4401 home page](README.md)

This course repository is designed so that you can either **read/run notebooks in your browser** or keep a local copy on your own computer.

You do **not** need to become a Git expert for MAD 4401. For normal course use, the three most important commands are:

```bash
git clone <repository-url>
git pull
git status
```

## 1. Git, GitHub, and Jupyter are different things

- **Git** tracks changes to files on your computer.
- **GitHub** stores a copy of a Git repository online.
- **JupyterLab** opens and runs the `.ipynb` notebooks.
- **Google Colab** and **Binder** can run course notebooks in a browser without a local Python setup.

The MAD 4401 repository lives on GitHub. When you **clone** it, Git makes a local copy on your computer. Later, **pull** gets new material from the instructor repository.

## 2. First-time setup

### Step A — Make sure Git is installed

Open a terminal and type:

```bash
git --version
```

If you see a version number, Git is installed.

### Step B — Choose a folder for the course

For example:

```bash
cd Documents
```

Useful navigation commands are:

```bash
pwd
ls
cd folder_name
cd ..
```

- `pwd` shows your current location.
- `ls` lists files and folders.
- `cd folder_name` moves into a folder.
- `cd ..` moves up one folder.

### Step C — Clone the repository

Do this **once**:

```bash
git clone https://github.com/mathguy-uf/MAD4401.git
cd MAD4401
```

You now have a local folder named `MAD4401` containing the course files.

### Step D — Install the Python packages

From inside the `MAD4401` folder:

```bash
python -m pip install -r requirements.txt
```

If your computer does not recognize `python`, try one of these instead:

```bash
python3 -m pip install -r requirements.txt
```

or on some Windows systems:

```bash
py -m pip install -r requirements.txt
```

### Step E — Open JupyterLab

```bash
jupyter lab
```

Your browser should open JupyterLab. Navigate to the module and notebook you want.

To stop JupyterLab, return to the terminal and press `Ctrl+C`.

## 3. What to do on a normal class day

Once you have cloned the repository, **do not clone it again**.

A normal session is:

```bash
cd Documents/MAD4401
git pull
jupyter lab
```

If your `MAD4401` folder is somewhere else, change the `cd` command accordingly.

### What does `git pull` do?

`git pull` asks GitHub for changes made since the last time you updated your local copy and brings those changes onto your computer.

It does **not** upload your work to the instructor repository.

## 4. Check the state of your local copy

At any time, type:

```bash
git status
```

If you have not edited any course files, Git will usually report that your working tree is clean.

If you have run or edited a notebook, Git may report that the `.ipynb` file has been modified. That is normal.

## 5. Protect your own notebook work

The safest habit is to make a copy before experimenting with a course notebook.

For example, instead of editing:

```text
04_fixed_point_cobwebs.ipynb
```

make a copy such as:

```text
04_fixed_point_cobwebs_jane.ipynb
```

Git can then update the original course notebook while your personal copy remains separate.

## 6. What if `git pull` says you have local changes?

Git may refuse to update a file that you have edited because it does not want to erase your work.

### Safest beginner method

1. Make a copy of any notebook containing work you want to keep.
2. Check the changed files:

```bash
git status
```

3. Restore the instructor version of a particular course file:

```bash
git restore path/to/notebook.ipynb
```

4. Then update:

```bash
git pull
```

Do **not** use `git restore` on a file containing work you have not copied elsewhere. `git restore` discards your local changes to that file.

### Another useful option: stash

If you understand what Git is doing, you can temporarily set your changes aside:

```bash
git stash
git pull
git stash pop
```

For this course, making a personal notebook copy is usually simpler.

## 7. You normally do not need `git push`

For MAD 4401, students mainly **receive** material from this repository.

- `git pull` downloads instructor updates.
- `git push` uploads commits to a remote repository.

You normally do **not** need `git push`, and students do not have permission to modify the instructor repository simply by cloning it.

## 8. Browser-only option: Google Colab

Each module page has a **Run in Colab** link.

Use this if you want to run a notebook without installing Python or Jupyter locally.

Important: running the notebook in Colab does not alter the instructor repository. If you want to keep your changes, save your own copy from Colab.

## 9. Browser-only option: Binder / JupyterLab

Each module page also has a **Launch Binder** link.

Binder creates a temporary Jupyter environment from this GitHub repository. It is useful for experimenting without installing anything.

Binder sessions are temporary. Download any work you want to keep before closing the session.

## 10. A five-minute Git practice exercise

After cloning the repository, try these commands:

```bash
cd MAD4401
git status
ls
cd module_1
ls
cd ..
git pull
```

You have now practiced the Git commands you will use most often in this course.

## 11. Vocabulary

| Term | Meaning |
|---|---|
| **repository** | A folder whose files are tracked by Git |
| **GitHub repository** | The online copy of a Git repository |
| **clone** | Make your first local copy of a repository |
| **pull** | Bring new changes from GitHub to your local copy |
| **status** | Show which local files have changed |
| **commit** | A recorded snapshot of changes in Git |
| **push** | Send local commits to a remote repository |
| **branch** | A separate line of development in Git |
| **working tree** | The files currently present in your local repository folder |

For ordinary MAD 4401 use, you mostly need **clone**, **pull**, and **status**.

## 12. Quick troubleshooting

### `git: command not found`
Git is not installed or is not available in your terminal.

### `python: command not found`
Try `python3` or `py` depending on your operating system.

### `jupyter: command not found`
Run the package installation command again from the repository folder:

```bash
python -m pip install -r requirements.txt
```

### `git pull` refuses because files were modified
Use `git status`, copy any work you want to preserve, restore the instructor version of the affected course file, and then pull again.

### I only want to read or run one notebook
Use the **View notebook**, **Run in Colab**, or **Launch Binder** links on the module page. You do not need to clone the repository.

---

[← Back to the MAD 4401 home page](README.md)
