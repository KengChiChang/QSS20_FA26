# Lecture 3 activity: your first repository

QSS 20 · Fall 2026 · about 30 minutes. Work alone, help your neighbor.

You will make a small repository of your own, save two snapshots, move them
between your computer and GitHub in both directions, and keep a junk file out.
Every step uses one of the commands from the slides: `git status`, `git diff`,
`git add`, `git commit`, `git push`, `git pull`, `git init`, and `.gitignore`.

## Before you start

1. You need a GitHub account and a way to sign in from your computer. The
   easiest is GitHub Desktop; `gh auth login` also works. The course site's
   **GitHub** page walks through both. If you have neither yet, do that first.
2. Check that Git knows who you are:

   ```bash
   git config --global user.name
   git config --global user.email
   ```

   If either prints nothing, set it:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@dartmouth.edu"
   ```

## Part 1: GitHub first, then your computer

### 1. Create a repository on GitHub

1. Go to <https://github.com/new>.
2. Name it `git-demo-1`. Choose **Private**.
3. Check **Add a README file**.
4. Click **Create repository**.

### 2. Clone it to your computer

Open a terminal and move to the folder where you keep coursework, for example
`cd ~/Desktop`. Do **not** do this inside `QSS20_FA26`. Then:

```bash
git clone https://github.com/<your-username>/git-demo-1.git
cd git-demo-1
ls -a
git status
```

**Check.** `ls -a` shows a `.git` folder and `README.md`. `git status` says
`nothing to commit, working tree clean`.

### 3. Add a file and save a snapshot

```bash
echo "print('Hello from my laptop')" > hello.py
git status
```

**Question.** Which list is `hello.py` in, and why?

```bash
git add hello.py
git status
git commit -m "Add hello.py"
git status
```

**Check.** After `git add`, the file moved to *Changes to be committed*. After
`git commit`, the tree is clean again. Run `git log --oneline`: you have two
commits, yours and GitHub's README commit.

### 4. Push, and confirm on GitHub

```bash
git push
```

Reload the repository page on GitHub. `hello.py` is there.

**Question.** Before `git push`, was `hello.py` on GitHub? How do you know?

### 5. Edit on GitHub, then pull

1. On GitHub, open `README.md` and click the pencil icon.
2. Add a line such as `Edited on the website.` and click **Commit changes**.
3. Back in the terminal:

```bash
git pull
cat README.md
git log --oneline
```

**Check.** The new line is in your local `README.md`, and `git log` shows the
website commit on top.

### 6. See a change before you save it

```bash
echo "print('Second line')" >> hello.py
git diff
```

**Question.** What does the `+` line show? Now save and push it:

```bash
git add hello.py
git commit -m "Print a second line"
git push
```

### 7. Keep junk out with `.gitignore`

Make a junk file, then tell Git to ignore it:

```bash
echo "scratch" > temp.txt
git status                      # temp.txt is untracked
echo "temp.txt" > .gitignore
git status                      # temp.txt is gone; .gitignore is untracked
git add .gitignore
git commit -m "Ignore temp files"
git push
```

**Check.** `temp.txt` is still on your disk (`ls`), but Git no longer lists
it. Add these three lines to `.gitignore` too, since every Python project
needs them:

```text
.ipynb_checkpoints/
__pycache__/
.DS_Store
```

Commit and push that change.

## Part 2: your computer first, then GitHub (if you finish early)

Sometimes the folder exists before the GitHub repository does.

```bash
cd ~/Desktop
mkdir git-demo-2
cd git-demo-2
git init
echo "# Git Demo 2" > notes.md
git add notes.md
git commit -m "Start notes"
git status
```

Now create an **empty** repository on GitHub named `git-demo-2` (no README
this time). GitHub then shows the two lines you need. They look like:

```bash
git remote add origin https://github.com/<your-username>/git-demo-2.git
git push -u origin main
```

Reload the GitHub page. Your `notes.md` is there. From now on, plain
`git push` and `git pull` work in this folder too.

## Hand in nothing, but check three things

- `git log --oneline` in `git-demo-1` shows at least four commits.
- Your GitHub page for `git-demo-1` shows `hello.py` and `.gitignore`.
- You can say, in one sentence each, what `add`, `commit`, `push`, and `pull`
  did today.
