# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_workWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

class Ui_WorkWidget(object):
    def setupUi(self, WorkWidget):
        if not WorkWidget.objectName():
            WorkWidget.setObjectName(u"WorkWidget")
        WorkWidget.resize(400, 300)
        self.gridLayout = QGridLayout(WorkWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(WorkWidget)

        QMetaObject.connectSlotsByName(WorkWidget)
    # setupUi

    def retranslateUi(self, WorkWidget):
        WorkWidget.setWindowTitle(QCoreApplication.translate("WorkWidget", u"Form", None))
    # retranslateUi

