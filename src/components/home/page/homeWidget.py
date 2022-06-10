from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QWidget, QMenu

from src.components.home import Ui_HomeWidget


class HomeWidget(QWidget, Ui_HomeWidget):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
        self.gjButton.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.gjButton:
            print(event, source)
            menu = QMenu()
            menu.addAction('새로 만들기')
            menu.addAction('열기')

            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                print(item.text())
            return True

        return super().eventFilter(source, event)