import io
import os
import shutil
import string

import openpyxl
from openpyxl.drawing.image import Image
from PIL import Image as PImage


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

    def insertImage(self, col, row, imageData):
        cell = f"{col}{row}"
        print(f"{cell} 사진 삽입")
        if not imageData:
            return
        if cell in self.images and self.images[cell]._data() == imageData:
            print(f'{cell}: 이미 같은 사진')
            return
        self._deleteImage(col, row)
        bytes_io = self.resizeImage(imageData)
        image = Image(bytes_io)
        image.width, image.height = 50, 50
        self.sheet.add_image(image, cell)
        self.images[cell] = image
        print(f"{cell} 사진 삽입 완료 {self.images}")

    @staticmethod
    def createNewFile(dest):
        NEW_FILE = "./static/gj.xlsx"
        shutil.copyfile(NEW_FILE, dest)
        return GJ(dest)

    def _indexToRow(self, index):
        return index * 22 + 4

    def resizeImage(self, imageData):
        imageData = io.BytesIO(imageData)
        pimage = PImage.open(imageData)
        pimage = pimage.resize((1200, 800))
        bytes_io = io.BytesIO()
        pimage.save(bytes_io, 'PNG')

        return bytes_io

    def _deleteImage(self, col, row):
        cell = f"{col}{row}"
        # print(self.images)
        try:
            self.sheet._images.remove(self.images[cell])
        except KeyError:
            print(f"{cell} 비어있는 공간~")
        else:
            del self.images[cell]

    def save(self, dest=None):
        if dest is None:
            dest = self.file
        self.wb.save(dest)
        print('저장완료')

    def saveLine(self, index, 공사전, 전주번호, 공사후):
        textCol = ['B', None, 'P']
        imageCol = ['A', 'I', 'O']

        row = self._indexToRow(index)

        # 공사전
        if 공사전['imageData']:
            print(f"{row}공사전 삽입")
            self.insertImage(imageCol[0], row + 2, 공사전['imageData'])
        else:
            print(f"{row}공사전 사진 업슴")
            self._deleteImage(imageCol[0], row + 2)

        self.sheet[f"{textCol[0]}{row}"] = 공사전['text']

        # 전주번호
        if 전주번호['imageData']:
            print(f"{row}전주번호 삽입")
            self.insertImage(imageCol[1], row + 10, 전주번호['imageData'])
        else:
            print(f"{row}전주번호 없으")
            self._deleteImage(imageCol[1], row + 10)

        # 공사 후
        if 공사후['imageData']:
            print(f"{row}공사후 삽입")
            self.insertImage(imageCol[2], row + 2, 공사후['imageData'])
        else:
            print(f"{row}공사후 사진 없음")
            self._deleteImage(imageCol[2], row + 2)

        self.sheet[f"{textCol[2]}{row}"] = 공사후['text']