import os
import shutil
import string

import openpyxl


class GJ:
    def __init__(self, file):
        self.file = file
        self.root, self.name = os.path.split(file)

        self.wb = openpyxl.load_workbook(file)
        self.sheet = self.wb['공정별사진대장']
        self.row = (self.sheet.max_row - 3) // 22

        self.images = {}

        for image in self.sheet._images:
            cell = f"{string.ascii_uppercase[image.anchor._from.col]}{image.anchor._from.row + 1}"
            self.images[cell] = image

    def addInfo(self, 공사명, 공사일자, 시공업체, 담당자):
        self.sheet['B2'] = 공사명
        self.sheet['Q2'] = f"공사일자 : {공사일자}"
        self.sheet['B3'] = 시공업체
        self.sheet['Q3'] = f"담당자 : {담당자}"

    def getLine(self, index):
        row = self._indexToRow(index)
        return {
            '공사전': {
                'text': str(self.sheet[f"B{row}"].value),
                'image': self.images[f"A{row + 2}"] if f"A{row + 2}" in self.images else None,
            },
            '전주 번호': {
                'text': '',
                'image': self.images[f"I{row + 10}"] if f"I{row + 10}" in self.images else None,
            },
            '공사후': {
                'text': str(self.sheet[f"P{row}"].value),
                'image': self.images[f"O{row + 2}"] if f"O{row + 2}" in self.images else None,
            }
        }

    @staticmethod
    def createNewFile(dest):
        NEW_FILE = "./static/gj.xlsx"
        shutil.copyfile(NEW_FILE, dest)
        return GJ(dest)

    def _indexToRow(self, index):
        return index * 22 + 4
