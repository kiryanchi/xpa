import os

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QFileDialog

from src.components.work import WorkWidget
from src.tools.log import Log
from src.xlsx import HJ


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Work(WorkWidget):
    createHjSignal = Signal()
    loadHjSignal = Signal()

    def __init__(self, main):
        super().__init__(main)

        self.createHjSignal.connect(self._createHj)
        self.loadHjSignal.connect(self._loadHj)

    @Slot()
    def _createHj(self):
        if not (fileName := self._saveFileName()):
            Log.info(self, "한전 만들기 취소")
            return
        Log.info(self, "한전 새로 만들기")
        self._goToWork(HJ.createNewFile(fileName))

    @Slot()
    def _loadHj(self):
        if not (fileName := self._loadFileName()):
            Log.info(self, "한전 불러오기 취소")
            return
        Log.info(self, "한전 불러오기")
        self._goToWork(HJ(fileName))

    def _addWorkListItem(self, excel):
        self.workList.addWork(excel)

    def _addWorkStackedItem(self, excel):
        self.workStacked.addWork(excel)

    def _goToWork(self, excel):
        self.main.workButton.click()
        self._addWorkListItem(excel)
        self._addWorkStackedItem(excel)

    def _loadFileName(self):
        fileName, _ = QFileDialog.getOpenFileName(self, '불러올 엑셀 파일 이름', BASE_DIR, 'Excel File (*.xlsx)')
        return fileName

    def _saveFileName(self):
        fileName, _ = QFileDialog.getSaveFileName(self, '저장할 파일 이름', BASE_DIR, 'Excel File (*.xlsx)')
        return fileName
