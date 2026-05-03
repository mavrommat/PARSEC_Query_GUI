# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedSemanticUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_AdvancedSemantic(object):
    def setupUi(self, AdvancedSemantic):
        if not AdvancedSemantic.objectName():
            AdvancedSemantic.setObjectName(u"AdvancedSemantic")
        AdvancedSemantic.resize(862, 658)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        AdvancedSemantic.setFont(font)
        self.gridLayout = QGridLayout(AdvancedSemantic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title_gb = QGroupBox(AdvancedSemantic)
        self.title_gb.setObjectName(u"title_gb")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.title_gb.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.title_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.title_gb)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.title_gb, 0, 0, 1, 1)

        self.main_gb = QGroupBox(AdvancedSemantic)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.main_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 357, 404))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 4, 3, 1, 1)

        self.B_del = QPushButton(self.main_gb)
        self.B_del.setObjectName(u"B_del")

        self.gridLayout_2.addWidget(self.B_del, 3, 3, 1, 1)

        self.B_submit = QPushButton(self.main_gb)
        self.B_submit.setObjectName(u"B_submit")

        self.gridLayout_2.addWidget(self.B_submit, 5, 3, 1, 1)

        self.groupBox = QGroupBox(self.main_gb)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.cmd_cb = QComboBox(self.groupBox)
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.addItem("")
        self.cmd_cb.setObjectName(u"cmd_cb")

        self.gridLayout_3.addWidget(self.cmd_cb, 1, 1, 1, 1)

        self.B_add = QPushButton(self.groupBox)
        self.B_add.setObjectName(u"B_add")

        self.gridLayout_3.addWidget(self.B_add, 1, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.gridLayout_2.addWidget(self.groupBox, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 2, 2, 1)


        self.gridLayout.addWidget(self.main_gb, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(AdvancedSemantic)

        QMetaObject.connectSlotsByName(AdvancedSemantic)
    # setupUi

    def retranslateUi(self, AdvancedSemantic):
        AdvancedSemantic.setWindowTitle(QCoreApplication.translate("AdvancedSemantic", u"Form", None))
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("AdvancedSemantic", u"Advanced Semantic Search", None))
        self.main_gb.setTitle("")
        self.B_del.setText(QCoreApplication.translate("AdvancedSemantic", u"Delete last addition", None))
        self.B_submit.setText(QCoreApplication.translate("AdvancedSemantic", u"Submit", None))
        self.groupBox.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("AdvancedSemantic", u"LLM expansion", None))
        self.cmd_cb.setItemText(0, QCoreApplication.translate("AdvancedSemantic", u"catalog ID (J/...)", None))
        self.cmd_cb.setItemText(1, QCoreApplication.translate("AdvancedSemantic", u"file name (hatlas.dat)", None))
        self.cmd_cb.setItemText(2, QCoreApplication.translate("AdvancedSemantic", u"title", None))
        self.cmd_cb.setItemText(3, QCoreApplication.translate("AdvancedSemantic", u"abstract", None))
        self.cmd_cb.setItemText(4, QCoreApplication.translate("AdvancedSemantic", u"keywords", None))
        self.cmd_cb.setItemText(5, QCoreApplication.translate("AdvancedSemantic", u"general description", None))
        self.cmd_cb.setItemText(6, QCoreApplication.translate("AdvancedSemantic", u"column name", None))
        self.cmd_cb.setItemText(7, QCoreApplication.translate("AdvancedSemantic", u"column description", None))
        self.cmd_cb.setItemText(8, QCoreApplication.translate("AdvancedSemantic", u"units", None))
        self.cmd_cb.setItemText(9, QCoreApplication.translate("AdvancedSemantic", u"authors", None))
        self.cmd_cb.setItemText(10, QCoreApplication.translate("AdvancedSemantic", u"references / bibcode", None))
        self.cmd_cb.setItemText(11, QCoreApplication.translate("AdvancedSemantic", u"search everywhere", None))

        self.B_add.setText(QCoreApplication.translate("AdvancedSemantic", u"Add", None))
    # retranslateUi

