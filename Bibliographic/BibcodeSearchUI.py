# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BibcodeSearchUI.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_BibliocodeSearch(object):
    def setupUi(self, BibliocodeSearch):
        if not BibliocodeSearch.objectName():
            BibliocodeSearch.setObjectName(u"BibliocodeSearch")
        BibliocodeSearch.resize(943, 630)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        BibliocodeSearch.setFont(font)
        self.gridLayout = QGridLayout(BibliocodeSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(BibliocodeSearch)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addWidget(self.title_gb, 0, 0, 1, 1)

        self.bibcode_gb = QGroupBox(self.main_gb)
        self.bibcode_gb.setObjectName(u"bibcode_gb")
        self.verticalLayout_2 = QVBoxLayout(self.bibcode_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.bibcode_gb)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Input_bibcodes = QTextEdit(self.bibcode_gb)
        self.Input_bibcodes.setObjectName(u"Input_bibcodes")

        self.verticalLayout_2.addWidget(self.Input_bibcodes)

        self.groupBox = QGroupBox(self.bibcode_gb)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_3)

        self.B_clear_all = QPushButton(self.groupBox)
        self.B_clear_all.setObjectName(u"B_clear_all")

        self.horizontalLayout.addWidget(self.B_clear_all)

        self.B_submit = QPushButton(self.groupBox)
        self.B_submit.setObjectName(u"B_submit")

        self.horizontalLayout.addWidget(self.B_submit)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 1)

        self.gridLayout_2.addWidget(self.bibcode_gb, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(1, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(BibliocodeSearch)

        QMetaObject.connectSlotsByName(BibliocodeSearch)
    # setupUi

    def retranslateUi(self, BibliocodeSearch):
        BibliocodeSearch.setWindowTitle(QCoreApplication.translate("BibliocodeSearch", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("BibliocodeSearch", u"Bibliographic Code Query\n"
"", None))
        self.bibcode_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("BibliocodeSearch", u"Enter a list of Bibcodes:", None))
        self.Input_bibcodes.setPlaceholderText(QCoreApplication.translate("BibliocodeSearch",
        "Enter list of Bibcodes (e.g. 2021MNRAS.506.1896K), one per line or separate them by comma (,)."
            )
        )
        self.groupBox.setTitle("")
        self.B_clear_all.setText(QCoreApplication.translate("BibliocodeSearch", u"Clear All", None))
        self.B_submit.setText(QCoreApplication.translate("BibliocodeSearch", u"Submit", None))
    # retranslateUi

