# count_whilst.py: how many Federalist essays contain the word "whilst"?
from pathlib import Path

files = sorted(Path("data/raw/federalist").glob("fp*.txt"))
hits = [f.name for f in files
        if "whilst" in f.read_text(encoding="utf-8").lower()]

print(len(hits), "of", len(files), "essays contain 'whilst'")
