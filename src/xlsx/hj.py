import os
import string

import openpyxl
import shutil

from openpyxl.styles import NamedStyle, Border, Side, Font, Alignment

from src.tools.log import Log


class HJ:

    def __init__(self, file):
        self.root, self.name = os.path.split(file)
        self.wb = None
        self.sheet = None
        self.height = 0
        self.images = {}
        self.row = 0

        self.style = NamedStyle(name="style")
        self.style.alignment = Alignment(horizontal='center', vertical='center')
        bd = Side(style='thin', color='000000')
        self.style.border = Border(left=bd, top=bd, right=bd, bottom=bd)

        try:
            self.wb = openpyxl.load_workbook(file)
        except FileNotFoundError as e:
            Log.warning(self, f"{e}")
        else:
            self.sheet = self.wb.active
            self.row = self.sheet.max_row - 2
            self.height = self.sheet.row_dimensions[3].height
            Log.debug(self, self.height)

            for i in range(self.row):
                self.images[f"E{i + 3}"] = None
                self.images[f"F{i + 3}"] = None
                self.images[f"G{i + 3}"] = None

            for image in self.sheet._images:
                r = image.anchor._from.row + 1
                c = string.ascii_uppercase[image.anchor._from.col]
                cell = f'{c}{r}'

                self.images[cell] = image

            Log.debug(self, f"{self.images}")

    def _calculatedRow(self, row):
        return row + 3

    def getLine(self, index):
        return {
                   "작업내역": str(self.sheet[f"B{self._calculatedRow(index)}"].value),
                   "선로번호": str(self.sheet[f"C{self._calculatedRow(index)}"].value),
                   "전산화번호": str(self.sheet[f"D{self._calculatedRow(index)}"].value),
               }, self.images[f"E{self._calculatedRow(index)}"], self.images[f"F{self._calculatedRow(index)}"], \
               self.images[f"G{self._calculatedRow(index)}"]

    def addLine(self):
        # 맨 마지막 줄의 높이를 셀과 동일하게 한다.
        self.row += 1
        self.sheet.row_dimensions[self.row] = self.height

        for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            self.sheet[f"{col}{self.row}"].style = self.style

    def save(self, dest):
        self.wb.save(dest)

    @staticmethod
    def createNewFile(dest):
        NEW_FILE = "./static/hj.xlsx"
        shutil.copyfile(NEW_FILE, dest)
        return HJ(dest)
