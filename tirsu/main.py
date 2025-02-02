from pathlib import Path

from language.tir import TirError
from write import write_tirsu

while True:
    p = input("Path to save to: ")
    path = Path(p).with_suffix(".svg").resolve()
    if path.parent.exists():
        break
    print("Invalid path!")

while True:
    s = input("Image scale (must be positive): ")
    try:
        scale = float(s)
        if scale <= 0:
            raise ValueError
    except (TypeError, ValueError):
        print("Invalid scale!")
        continue
    break

while True:
    dialect = input("Githyanki (Y) or githzerai (Z) script? ").lower().strip()
    if dialect in ["y", "z"]:
        break
    print("Invalid entry!")

orientation = 1 if dialect == "y" else -1

while True:
    text = input("Text to write in Tir'su: ")
    try:
        write_tirsu(path, text, orientation, scale)
    except TirError:
        print("Invalid characters found in text!")
    else:
        break
