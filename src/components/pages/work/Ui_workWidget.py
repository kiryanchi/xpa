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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_Ui_WorkWidget(object):
    def setupUi(self, Ui_WorkWidget):
        if not Ui_WorkWidget.objectName():
            Ui_WorkWidget.setObjectName(u"Ui_WorkWidget")
        Ui_WorkWidget.resize(400, 300)
        self.gridLayout = QGridLayout(Ui_WorkWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.workStackedWidget = QStackedWidget(Ui_WorkWidget)
        self.workStackedWidget.setObjectName(u"workStackedWidget")

        self.gridLayout.addWidget(self.workStackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Ui_WorkWidget)

        QMetaObject.connectSlotsByName(Ui_WorkWidget)
    # setupUi

    def retranslateUi(self, Ui_WorkWidget):
        Ui_WorkWidget.setWindowTitle(QCoreApplication.translate("Ui_WorkWidget", u"Form", None))
    # retranslateUi

