# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_workInnerWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_WorkInnerWidget(object):
    def setupUi(self, WorkInnerWidget):
        if not WorkInnerWidget.objectName():
            WorkInnerWidget.setObjectName(u"WorkInnerWidget")
        WorkInnerWidget.resize(618, 457)
        self.verticalLayout = QVBoxLayout(WorkInnerWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame = QFrame(WorkInnerWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(454, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(50, 32))
        self.addButton.setMaximumSize(QSize(50, 32))

        self.horizontalLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(self.frame)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(50, 32))
        self.removeButton.setMaximumSize(QSize(50, 32))

        self.horizontalLayout.addWidget(self.removeButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WorkInnerWidget)

        QMetaObject.connectSlotsByName(WorkInnerWidget)
    # setupUi

    def retranslateUi(self, WorkInnerWidget):
        WorkInnerWidget.setWindowTitle(QCoreApplication.translate("WorkInnerWidget", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("WorkInnerWidget", u"\uc800\uc7a5", None))
        self.addButton.setText(QCoreApplication.translate("WorkInnerWidget", u"+", None))
        self.removeButton.setText(QCoreApplication.translate("WorkInnerWidget", u"-", None))
    # retranslateUi

