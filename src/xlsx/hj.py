import os
import string

import openpyxl
import shutil

from src.tools.log import Log


class HJ:

    def __init__(self, file):
        self.root, self.name = os.path.split(file)
        self.wb = None
        self.sheet = None
        self.images = {}
        self.row = 0

        try:
            self.wb = openpyxl.load_workbook(file)
        except FileNotFoundError as e:
            Log.warning(self, f"{e}")
        else:
            self.sheet = self.wb.active
            self.row = self.sheet.max_row - 2

            for i in range(self.row):
                self.images[f"E{i+3}"] = None
                self.images[f"F{i+3}"] = None
                self.images[f"G{i+3}"] = None

            for image in self.sheet._images:
                c = string.ascii_uppercase[image.anchor._from.col]
                r = image.anchor._from.row + 1
                cell = f"{c}{r}"
                Log.debug(self, cell)
                self.images[cell] = image

            Log.debug(self, f"{self.images}")

    def getLine(self, row):
        row = row + 3
        return {
            "작업내역": str(self.sheet[f"B{row}"].value),
            "선로번호": str(self.sheet[f"C{row}"].value),
            "전산화번호": str(self.sheet[f"D{row}"].value),
        }, self.images[f"E{row}"], self.images[f"F{row}"], self.images[f"G{row}"]

    @staticmethod
    def createNewFile(dest):
        NEW_FILE = "./static/hj.xlsx"
        shutil.copyfile(NEW_FILE, dest)
        return HJ(dest)
