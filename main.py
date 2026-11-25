"""Angry Judge: The Short Rant Contest — writes one short rant to /output/entry.txt."""

import os

OUTPUT_PATH = "/output/entry.txt"

RANT = (
    "A robot makes me prove I'm not a robot by clicking every traffic light "
    "in a blurry photo, then fails me for clicking too fast. I have a job, a "
    "mortgage, and strong opinions about soup \u2014 but miss one bicycle in "
    "square seven and I'm legally a toaster."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
