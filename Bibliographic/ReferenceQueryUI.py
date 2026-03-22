# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReferenceQueryUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ReferenceQuery(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1410, 911)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(Form)
        self.main_gb.setObjectName(u"main_gb")
        self.verticalLayout_2 = QVBoxLayout(self.main_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_gb = QGroupBox(self.main_gb)
        self.title_gb.setObjectName(u"title_gb")
        self.verticalLayout = QVBoxLayout(self.title_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.title_gb)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.title_gb)

        self.ref_gb = QGroupBox(self.main_gb)
        self.ref_gb.setObjectName(u"ref_gb")
        self.gridLayout_2 = QGridLayout(self.ref_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Input_reference = QLineEdit(self.ref_gb)
        self.Input_reference.setObjectName(u"Input_reference")

        self.gridLayout_2.addWidget(self.Input_reference, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.submit_clear_gb = QGroupBox(self.ref_gb)
        self.submit_clear_gb.setObjectName(u"submit_clear_gb")
        self.horizontalLayout = QHBoxLayout(self.submit_clear_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_5)

        self.B_clear_all = QPushButton(self.submit_clear_gb)
        self.B_clear_all.setObjectName(u"B_clear_all")

        self.horizontalLayout.addWidget(self.B_clear_all)

        self.B_submit = QPushButton(self.submit_clear_gb)
        self.B_submit.setObjectName(u"B_submit")

        self.horizontalLayout.addWidget(self.B_submit)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.gridLayout_2.addWidget(self.submit_clear_gb, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 3, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)

        self.verticalLayout_2.addWidget(self.ref_gb)

        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"Reference Query", None))
        self.ref_gb.setTitle("")
        self.Input_reference.setPlaceholderText(QCoreApplication.translate("Form", u"Enter a full reference string (e.g. Kovlakas et al. 2021, MNRAS, 506, 1896)", None))
        self.submit_clear_gb.setTitle("")
        self.B_clear_all.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.B_submit.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

