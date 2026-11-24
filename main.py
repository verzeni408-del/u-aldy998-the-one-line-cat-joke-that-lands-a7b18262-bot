from pathlib import Path

ENTRY = "The fire alarm went off and my cat sprinted to the exit, then turned around, went back to his food bowl, and left the fire to me."


def main():
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
