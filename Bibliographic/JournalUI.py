# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JournalUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_JournalSearch(object):
    def setupUi(self, JournalSearch):
        if not JournalSearch.objectName():
            JournalSearch.setObjectName(u"JournalSearch")
        JournalSearch.resize(992, 615)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        JournalSearch.setFont(font)
        self.gridLayout = QGridLayout(JournalSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(JournalSearch)
        self.main_gb.setObjectName(u"main_gb")
        self.verticalLayout = QVBoxLayout(self.main_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_gb = QGroupBox(self.main_gb)
        self.title_gb.setObjectName(u"title_gb")
        self.verticalLayout_2 = QVBoxLayout(self.title_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.title_gb)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.title_gb)

        self.input_gb = QGroupBox(self.main_gb)
        self.input_gb.setObjectName(u"input_gb")
        self.gridLayout_2 = QGridLayout(self.input_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Input_publ_abbr = QLineEdit(self.input_gb)
        self.Input_publ_abbr.setObjectName(u"Input_publ_abbr")

        self.gridLayout_2.addWidget(self.Input_publ_abbr, 2, 0, 1, 1)

        self.Input_year = QLineEdit(self.input_gb)
        self.Input_year.setObjectName(u"Input_year")

        self.gridLayout_2.addWidget(self.Input_year, 2, 1, 1, 1)

        self.Input_page_id = QLineEdit(self.input_gb)
        self.Input_page_id.setObjectName(u"Input_page_id")

        self.gridLayout_2.addWidget(self.Input_page_id, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 4)

        self.label_2 = QLabel(self.input_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.input_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_5 = QLabel(self.input_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 3, 1, 1)

        self.Input_volume = QLineEdit(self.input_gb)
        self.Input_volume.setObjectName(u"Input_volume")

        self.gridLayout_2.addWidget(self.Input_volume, 2, 2, 1, 1)

        self.label_3 = QLabel(self.input_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)

        self.B_submit = QPushButton(self.input_gb)
        self.B_submit.setObjectName(u"B_submit")

        self.gridLayout_2.addWidget(self.B_submit, 4, 3, 1, 1)

        self.B_clear_all = QPushButton(self.input_gb)
        self.B_clear_all.setObjectName(u"B_clear_all")

        self.gridLayout_2.addWidget(self.B_clear_all, 4, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.input_gb)

        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(JournalSearch)

        QMetaObject.connectSlotsByName(JournalSearch)
    # setupUi

    def retranslateUi(self, JournalSearch):
        JournalSearch.setWindowTitle(QCoreApplication.translate("JournalSearch", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("JournalSearch", u"Journal Search", None))
        self.input_gb.setTitle("")
        self.Input_publ_abbr.setPlaceholderText(QCoreApplication.translate("JournalSearch", u"(e.g. ApJ for Astrophysical Journal)", None))
        self.Input_year.setPlaceholderText(QCoreApplication.translate("JournalSearch", u"YYYY", None))
        self.label_2.setText(QCoreApplication.translate("JournalSearch", u"Publication abbreviation:", None))
        self.label_4.setText(QCoreApplication.translate("JournalSearch", u"Volume", None))
        self.label_5.setText(QCoreApplication.translate("JournalSearch", u"Page/ID", None))
        self.Input_volume.setText("")
        self.label_3.setText(QCoreApplication.translate("JournalSearch", u"Year", None))
        self.B_submit.setText(QCoreApplication.translate("JournalSearch", u"Submit", None))
        self.B_clear_all.setText(QCoreApplication.translate("JournalSearch", u"Clear All", None))
    # retranslateUi

