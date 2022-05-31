# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_settingWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_SettingWidget(object):
    def setupUi(self, SettingWidget):
        if not SettingWidget.objectName():
            SettingWidget.setObjectName(u"SettingWidget")
        SettingWidget.resize(650, 502)
        self.gridLayout = QGridLayout(SettingWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(SettingWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.currentLabel = QLabel(self.frame)
        self.currentLabel.setObjectName(u"currentLabel")

        self.horizontalLayout.addWidget(self.currentLabel)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.latestLabel = QLabel(self.frame)
        self.latestLabel.setObjectName(u"latestLabel")

        self.horizontalLayout.addWidget(self.latestLabel)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(SettingWidget)

        QMetaObject.connectSlotsByName(SettingWidget)
    # setupUi

    def retranslateUi(self, SettingWidget):
        SettingWidget.setWindowTitle(QCoreApplication.translate("SettingWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("SettingWidget", u"\ud604\uc7ac\ubc84\uc804", None))
        self.currentLabel.setText(QCoreApplication.translate("SettingWidget", u"current", None))
        self.label_2.setText(QCoreApplication.translate("SettingWidget", u"\ucd5c\uc2e0\ubc84\uc804", None))
        self.latestLabel.setText(QCoreApplication.translate("SettingWidget", u"latest", None))
    # retranslateUi

