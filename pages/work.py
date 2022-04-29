from PySide6.QtCore import Signal, Slot

from src.components.work import WorkWidget


class Work(WorkWidget):
    createHjSignal = Signal()

    def __init__(self, main):
        super().__init__(main)

        self.createHjSignal.connect(self._createHj)

    @Slot()
    def _createHj(self):
        self._addWorkListItem()
        self._addWorkStackedItem()

    def _addWorkListItem(self):
        self.workList.addList()

    def _addWorkStackedItem(self):
        pass