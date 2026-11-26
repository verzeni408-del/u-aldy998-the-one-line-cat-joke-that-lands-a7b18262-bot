import pathlib

ENTRY = "My cat sat on my phone and emailed my resignation to my boss — he accepted it before I even woke up."
OUTPUT = pathlib.Path("/output/entry.txt")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(ENTRY, encoding="utf-8")
