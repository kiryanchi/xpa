import os
import sys


def _convert(ui):
    print(f"Convert {ui}.ui to {ui}.py")
    os.system(f"pyside6-uic {ui}.ui -o {ui}.py")


def convert(uis):
    DIR = './src/pages/'

    for (root, _, files) in os.walk(DIR):
        if len(files) > 0:
            for file in files:
                if file[-2:] == "ui":
                    ui = f"{root}/{file[:-3]}"
                    if uis[0] == '.':
                        _convert(ui)
                    elif file[:-3] in uis:
                        _convert(ui)


if __name__ == "__main__":
    uis = sys.argv[1:] if len(sys.argv) > 1 else None

    if not uis:
        print("Need at least one .ui file")
        sys.exit(1)

    convert(uis)
