# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_workWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_WorkWidget(object):
    def setupUi(self, WorkWidget):
        if not WorkWidget.objectName():
            WorkWidget.setObjectName(u"WorkWidget")
        WorkWidget.resize(608, 464)
        self.gridLayout = QGridLayout(WorkWidget)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.addButton = QPushButton(WorkWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(50, 32))
        self.addButton.setMaximumSize(QSize(50, 32))

        self.gridLayout.addWidget(self.addButton, 1, 2, 1, 1)

        self.undoButton = QPushButton(WorkWidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMinimumSize(QSize(50, 32))
        self.undoButton.setMaximumSize(QSize(50, 32))

        self.gridLayout.addWidget(self.undoButton, 1, 4, 1, 1)

        self.redoButton = QPushButton(WorkWidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMinimumSize(QSize(50, 32))
        self.redoButton.setMaximumSize(QSize(50, 32))

        self.gridLayout.addWidget(self.redoButton, 1, 5, 1, 1)

        self.removeButton = QPushButton(WorkWidget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(50, 32))
        self.removeButton.setMaximumSize(QSize(50, 32))

        self.gridLayout.addWidget(self.removeButton, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.saveButton = QPushButton(WorkWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.saveButton, 1, 0, 1, 1)

        self.workTableWidget = QTableWidget(WorkWidget)
        self.workTableWidget.setObjectName(u"workTableWidget")

        self.gridLayout.addWidget(self.workTableWidget, 0, 0, 1, 6)


        self.retranslateUi(WorkWidget)

        QMetaObject.connectSlotsByName(WorkWidget)
    # setupUi

    def retranslateUi(self, WorkWidget):
        WorkWidget.setWindowTitle(QCoreApplication.translate("WorkWidget", u"Form", None))
        self.addButton.setText(QCoreApplication.translate("WorkWidget", u"+", None))
        self.undoButton.setText(QCoreApplication.translate("WorkWidget", u"undo", None))
        self.redoButton.setText(QCoreApplication.translate("WorkWidget", u"redo", None))
        self.removeButton.setText(QCoreApplication.translate("WorkWidget", u"-", None))
        self.saveButton.setText(QCoreApplication.translate("WorkWidget", u"\uc800\uc7a5", None))
    # retranslateUi

