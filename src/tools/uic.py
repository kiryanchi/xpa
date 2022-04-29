import os
import sys


def convert(files):
    for file in files:
        if os.path.isfile(f"{file}.ui"):
            os.system(f"pyside6-uic {file}.ui -o {file}.py")
            print(f"Convert {file}.ui to {file}.py")
        else:
            print(f"{file}.ui doesn't exist")


if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else None

    if not files:
        print("Need at least one .ui file")
        sys.exit(1)

    convert(files)
