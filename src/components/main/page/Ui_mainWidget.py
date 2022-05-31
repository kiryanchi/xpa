# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_mainWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(885, 763)
        self.gridLayout = QGridLayout(MainWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sideTab = QFrame(MainWidget)
        self.frame_sideTab.setObjectName(u"frame_sideTab")
        self.frame_sideTab.setMinimumSize(QSize(98, 0))
        self.frame_sideTab.setMaximumSize(QSize(100, 16777215))
        self.frame_sideTab.setFrameShape(QFrame.NoFrame)
        self.frame_sideTab.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_sideTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeButton = QToolButton(self.frame_sideTab)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(16)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../static/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(32, 32))
        self.homeButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.homeButton)

        self.newButton = QToolButton(self.frame_sideTab)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setMinimumSize(QSize(80, 80))
        self.newButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../../../static/icon/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newButton.setIcon(icon1)
        self.newButton.setIconSize(QSize(32, 32))
        self.newButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.newButton)

        self.recentButton = QToolButton(self.frame_sideTab)
        self.recentButton.setObjectName(u"recentButton")
        self.recentButton.setMinimumSize(QSize(80, 80))
        self.recentButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"../../../static/icon/recent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recentButton.setIcon(icon2)
        self.recentButton.setIconSize(QSize(32, 32))
        self.recentButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.recentButton)

        self.openButton = QToolButton(self.frame_sideTab)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setMinimumSize(QSize(80, 80))
        self.openButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u"../../../static/icon/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon3)
        self.openButton.setIconSize(QSize(32, 32))
        self.openButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.openButton)

        self.workButton = QToolButton(self.frame_sideTab)
        self.workButton.setObjectName(u"workButton")
        self.workButton.setMinimumSize(QSize(80, 80))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.workButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"../../../static/icon/work.png", QSize(), QIcon.Normal, QIcon.Off)
        self.workButton.setIcon(icon4)
        self.workButton.setIconSize(QSize(32, 32))
        self.workButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.workButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.settingButton = QToolButton(self.frame_sideTab)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy)
        self.settingButton.setMinimumSize(QSize(80, 80))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.settingButton.setFont(font2)

        self.verticalLayout.addWidget(self.settingButton)


        self.gridLayout.addWidget(self.frame_sideTab, 0, 0, 1, 1)

        self.frame_main = QFrame(MainWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(787, 727))
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainStackedWidget = QStackedWidget(self.frame_main)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")

        self.verticalLayout_2.addWidget(self.mainStackedWidget)


        self.gridLayout.addWidget(self.frame_main, 0, 1, 1, 1)


        self.retranslateUi(MainWidget)

        self.mainStackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"XPA", None))
        self.homeButton.setText(QCoreApplication.translate("MainWidget", u"Home", None))
        self.newButton.setText(QCoreApplication.translate("MainWidget", u"New", None))
        self.recentButton.setText(QCoreApplication.translate("MainWidget", u"Recent", None))
        self.openButton.setText(QCoreApplication.translate("MainWidget", u"Open", None))
        self.workButton.setText(QCoreApplication.translate("MainWidget", u"Work", None))
        self.settingButton.setText(QCoreApplication.translate("MainWidget", u"Setting", None))
    # retranslateUi

