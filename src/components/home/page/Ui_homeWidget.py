# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_homeWidget.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        if not HomeWidget.objectName():
            HomeWidget.setObjectName(u"HomeWidget")
        HomeWidget.resize(827, 644)
        self.gridLayout = QGridLayout(HomeWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(HomeWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.recentHjtableWidget = QTableWidget(self.frame_4)
        self.recentHjtableWidget.setObjectName(u"recentHjtableWidget")

        self.verticalLayout_2.addWidget(self.recentHjtableWidget)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.recentGjTableWidget = QTableWidget(self.frame_3)
        self.recentGjTableWidget.setObjectName(u"recentGjTableWidget")

        self.verticalLayout.addWidget(self.recentGjTableWidget)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 2)

        self.label_2 = QLabel(HomeWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 26))
        font1 = QFont()
        font1.setPointSize(26)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.frame = QFrame(HomeWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gjButton = QPushButton(self.frame)
        self.gjButton.setObjectName(u"gjButton")
        self.gjButton.setMinimumSize(QSize(120, 120))
        self.gjButton.setMaximumSize(QSize(120, 120))
        self.gjButton.setCheckable(False)
        self.gjButton.setChecked(False)
        self.gjButton.setFlat(False)

        self.horizontalLayout.addWidget(self.gjButton)

        self.hjButton = QPushButton(self.frame)
        self.hjButton.setObjectName(u"hjButton")
        self.hjButton.setMinimumSize(QSize(120, 120))
        self.hjButton.setMaximumSize(QSize(120, 120))
        self.hjButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.hjButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)

        self.label = QLabel(HomeWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 26))
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(HomeWidget)

        self.gjButton.setDefault(False)


        QMetaObject.connectSlotsByName(HomeWidget)
    # setupUi

    def retranslateUi(self, HomeWidget):
        HomeWidget.setWindowTitle(QCoreApplication.translate("HomeWidget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("HomeWidget", u"\ud55c\uc804", None))
        self.label_3.setText(QCoreApplication.translate("HomeWidget", u"\uacbd\uc8fc", None))
        self.label_2.setText(QCoreApplication.translate("HomeWidget", u"\ucd5c\uadfc \uc791\uc5c5\ud55c \ud30c\uc77c", None))
        self.gjButton.setText(QCoreApplication.translate("HomeWidget", u"\uacbd\uc8fc", None))
        self.hjButton.setText(QCoreApplication.translate("HomeWidget", u"\ud55c\uc804", None))
        self.label.setText(QCoreApplication.translate("HomeWidget", u"\uc791\uc5c5 \uc2dc\uc791\ud558\uae30", None))
    # retranslateUi

