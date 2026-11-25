#!/usr/bin/env python3
"""The 3AM Fridge Text (make.fun).

Writes the entry -- one line a smart fridge would text its owner at 3am, written to /output/entry.txt by a small Python program. -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'It is 3am. The leftover pizza is still here. I have been awake all night thinking about it, and frankly, so should you.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
