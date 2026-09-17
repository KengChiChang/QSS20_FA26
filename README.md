# QSS 20, Fall 2026: course materials

Data, problem sets, in-class activities, and lecture notebooks for QSS 20,
Modern Statistical Computing (Dartmouth, Fall 2026). You pull from this
repository to get each week's files. It is public, so you can clone it without
signing in.

## What you need first

- Git installed.
- The `qss20` conda environment from the software setup guide.

New to the shell and the setup? See the course website's System Setup guide.

## Get the materials once

In a terminal, from the folder where you keep coursework:

```bash
cd ~/Desktop
git clone https://github.com/KengChiChang/QSS20_FA26.git
cd QSS20_FA26
```

## Update before each class

```bash
git pull
```

This downloads the new and changed files. Run it before every class and before
you start a problem set.

## Work on a copy, so updates never clash

Before you edit a notebook from this repository, copy it and edit the copy:

```bash
cp problemsets/ps0/ps0.ipynb problemsets/ps0/ps0_mywork.ipynb
```

Edit the copy. The original stays unchanged, so `git pull` always succeeds. If a
pull ever stops because you changed a tracked file, run `git stash`, then
`git pull`, then `git stash pop`.

## How you submit

You do not push to this repository. Submit your work on **Gradescope**, as each
assignment says, usually a PDF plus the notebook.

## Layout

- `data/`: shared datasets used in class and on problem sets
- `problemsets/`: problem set files (start with `ps0/`)
- `activity_solutions/`: in-class activity notebooks
- `lectures/`: lecture notebooks
