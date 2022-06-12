import os
import sys

from PySide6.QtWidgets import QApplication

from pages.main import Main
from src.tools.config import Config


def main(env):
    app = QApplication()
    main = Main()
    main.show()

    # TEST
    if env == 'dev':
        main.home.gjButton.click()

    app.exec()


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else "prod"
    main(env)
