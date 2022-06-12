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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SettingWidget(object):
    def setupUi(self, SettingWidget):
        if not SettingWidget.objectName():
            SettingWidget.setObjectName(u"SettingWidget")
        SettingWidget.resize(650, 502)
        self.gridLayout = QGridLayout(SettingWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(SettingWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.gjWidthLineEdit = QLineEdit(self.groupBox)
        self.gjWidthLineEdit.setObjectName(u"gjWidthLineEdit")

        self.gridLayout_2.addWidget(self.gjWidthLineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.gjHeightLineEdit = QLineEdit(self.groupBox)
        self.gjHeightLineEdit.setObjectName(u"gjHeightLineEdit")

        self.gridLayout_2.addWidget(self.gjHeightLineEdit, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(SettingWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.hjWidthLineEdit = QLineEdit(self.groupBox_2)
        self.hjWidthLineEdit.setObjectName(u"hjWidthLineEdit")

        self.horizontalLayout_2.addWidget(self.hjWidthLineEdit)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.hjHeightLineEdit = QLineEdit(self.groupBox_2)
        self.hjHeightLineEdit.setObjectName(u"hjHeightLineEdit")

        self.horizontalLayout_2.addWidget(self.hjHeightLineEdit)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.savePushButton = QPushButton(SettingWidget)
        self.savePushButton.setObjectName(u"savePushButton")

        self.gridLayout.addWidget(self.savePushButton, 5, 0, 1, 1)

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

        self.label_7 = QLabel(SettingWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)


        self.retranslateUi(SettingWidget)

        QMetaObject.connectSlotsByName(SettingWidget)
    # setupUi

    def retranslateUi(self, SettingWidget):
        SettingWidget.setWindowTitle(QCoreApplication.translate("SettingWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingWidget", u"\uacbd\uc8fc \ud658\uacbd\uc124\uc815", None))
        self.label_4.setText(QCoreApplication.translate("SettingWidget", u"\uc138\ub85c", None))
        self.label_3.setText(QCoreApplication.translate("SettingWidget", u"\uac00\ub85c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingWidget", u"\ud55c\uc804 \ud658\uacbd\uc124\uc815", None))
        self.label_5.setText(QCoreApplication.translate("SettingWidget", u"\uac00\ub85c", None))
        self.label_6.setText(QCoreApplication.translate("SettingWidget", u"\uc138\ub85c", None))
        self.savePushButton.setText(QCoreApplication.translate("SettingWidget", u"\uc800\uc7a5", None))
        self.label.setText(QCoreApplication.translate("SettingWidget", u"\ud604\uc7ac\ubc84\uc804", None))
        self.currentLabel.setText(QCoreApplication.translate("SettingWidget", u"current", None))
        self.label_2.setText(QCoreApplication.translate("SettingWidget", u"\ucd5c\uc2e0\ubc84\uc804", None))
        self.latestLabel.setText(QCoreApplication.translate("SettingWidget", u"latest", None))
        self.label_7.setText(QCoreApplication.translate("SettingWidget", u"\uc800\uc7a5\ud55c \ud6c4\uc5d0 \ud504\ub85c\uadf8\ub7a8\uc744 \ud55c \ubc88 \uaed0\ub2e4 \ucf1c\uc8fc\uc138\uc694.", None))
    # retranslateUi

