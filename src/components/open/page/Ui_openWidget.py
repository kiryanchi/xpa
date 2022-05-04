# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_openWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_OpenWidget(object):
    def setupUi(self, OpenWidget):
        if not OpenWidget.objectName():
            OpenWidget.setObjectName(u"OpenWidget")
        OpenWidget.resize(584, 502)
        self.openHjButton = QPushButton(OpenWidget)
        self.openHjButton.setObjectName(u"openHjButton")
        self.openHjButton.setGeometry(QRect(240, 110, 100, 32))
        self.label = QLabel(OpenWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 240, 301, 171))

        self.retranslateUi(OpenWidget)

        QMetaObject.connectSlotsByName(OpenWidget)
    # setupUi

    def retranslateUi(self, OpenWidget):
        OpenWidget.setWindowTitle(QCoreApplication.translate("OpenWidget", u"Form", None))
        self.openHjButton.setText(QCoreApplication.translate("OpenWidget", u"\ud55c\uc804 \ubd88\ub7ec\uc624\uae30", None))
        self.label.setText(QCoreApplication.translate("OpenWidget", u"\ud6c8\ub828\uc18c \ub2e4\ub140\uc640\uc11c \uc880 \ub2e4\ub4ec\uc744 \uc608\uc815 \ub300\ucda9 \uc4f0\uace0 \uc788\uc5b4\ub77c\n"
"\uacbd\uc8fc\ub294 \uac14\ub2e4\uc640\uc11c  \ucd94\uac00\ud574\uc904\uac8c", None))
    # retranslateUi

