import sys

from PySide6.QtWidgets import QApplication

from pages.main import Main


def main(env):
    app = QApplication()
    main = Main()
    main.show()
    app.exec()


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else "prod"
    main(env)
