# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_homeWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
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
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 2)

        self.label_2 = QLabel(HomeWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 26))
        font = QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)

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
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(HomeWidget)

        self.gjButton.setDefault(False)


        QMetaObject.connectSlotsByName(HomeWidget)
    # setupUi

    def retranslateUi(self, HomeWidget):
        HomeWidget.setWindowTitle(QCoreApplication.translate("HomeWidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("HomeWidget", u"\uacf5\uc9c0\uc0ac\ud56d", None))
        self.gjButton.setText(QCoreApplication.translate("HomeWidget", u"\uacbd\uc8fc\n"
"\uad6c\ud604\uc911", None))
        self.hjButton.setText(QCoreApplication.translate("HomeWidget", u"\ud55c\uc804", None))
        self.label.setText(QCoreApplication.translate("HomeWidget", u"\ud15c\ud50c\ub9bf", None))
    # retranslateUi

