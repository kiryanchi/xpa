import os
import shutil
import string

import openpyxl
from openpyxl.styles import NamedStyle, Alignment, Side, Border

from src.tools.log import Log


class MyStyle(NamedStyle):
    def __init__(self):
        super().__init__(name="style")
        self.alignment = Alignment(horizontal="center", vertical="center")
        bd = Side(style="thin", color="000000")
        self.border = Border(left=bd, top=bd, right=bd, bottom=bd)


class HJ:
    def __init__(self, file):
        self.root, self.name = os.path.split(file)
        self.wb = None
        self.sheet = None
        self.height = 0
        self.images = {}
        self.row = 0

        try:
            self.wb = openpyxl.load_workbook(file)
        except FileNotFoundError as e:
            Log.warning(self, f"{e}")
        else:
            self.sheet = self.wb.active
            self.height = self.sheet.row_dimensions[3].height

            for i in range(3, self.sheet.max_row + 1):
                self.images[f"E{i}"] = None
                self.images[f"F{i}"] = None
                self.images[f"G{i}"] = None

            Log.debug(self, self.sheet._images)

            for image in self.sheet._images:
                Log.debug(self, f"images: {image}")

    def _indexToLine(self, index):
        return index + 3

    def _setLineStyle(self, row, style):
        for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            self.sheet[f"{col}{row}"].style = style

    def addLine(self):
        Log.debug(self, f"addLine 전 max_row: {self.sheet.max_row}")
        self.sheet.row_dimensions[self.sheet.max_row + 1].height = self.height
        self._setLineStyle(self.sheet.max_row + 1, MyStyle())
        Log.debug(self, f"addLine 후 max_row: {self.sheet.max_row}")

    def removeLine(self):
        Log.debug(self, f"removeLine 전 max_row: {self.sheet.max_row}")
        self.sheet.row_dimensions[self.sheet.max_row].height = self.sheet.row_dimensions[self.sheet.max_row + 1].height
        self._setLineStyle(self.sheet.max_row, "Normal")
        self.sheet.delete_rows(self.sheet.max_row, 1)
        Log.debug(self, f"removeLine 후 max_row: {self.sheet.max_row}")

    def getLine(self, index):
        return {
                   "작업내역": str(self.sheet[f"B{self._indexToLine(index)}"].value),
                   "선로번호": str(self.sheet[f"C{self._indexToLine(index)}"].value),
                   "전산화번호": str(self.sheet[f"D{self._indexToLine(index)}"].value),
               }, self.images[f"E{self._indexToLine(index)}"], self.images[f"F{self._indexToLine(index)}"], self.images[
                   f"G{self._indexToLine(index)}"]

    def save(self, dest):
        self.wb.save(dest)

    @staticmethod
    def createNewFile(dest):
        NEW_FILE = "./static/hj.xlsx"
        shutil.copyfile(NEW_FILE, dest)
        return HJ(dest)
