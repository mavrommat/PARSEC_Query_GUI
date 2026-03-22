# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BibliographicSearchUI.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_BibliographicSearch(object):
    def setupUi(self, BibliographySearch):
        if not BibliographySearch.objectName():
            BibliographySearch.setObjectName(u"BibliographySearch")
        BibliographySearch.resize(800, 605)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        BibliographySearch.setFont(font)
        self.verticalLayout = QVBoxLayout(BibliographySearch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_gb = QGroupBox(BibliographySearch)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout = QGridLayout(self.main_gb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttons_gb = QGroupBox(self.main_gb)
        self.buttons_gb.setObjectName(u"buttons_gb")
        self.gridLayout_2 = QGridLayout(self.buttons_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.B_reference_search = QPushButton(self.buttons_gb)
        self.B_reference_search.setObjectName(u"B_reference_search")

        self.gridLayout_2.addWidget(self.B_reference_search, 0, 1, 1, 1)

        self.B_journal_search = QPushButton(self.buttons_gb)
        self.B_journal_search.setObjectName(u"B_journal_search")

        self.gridLayout_2.addWidget(self.B_journal_search, 0, 0, 1, 1)

        self.B_bibcode_search = QPushButton(self.buttons_gb)
        self.B_bibcode_search.setObjectName(u"B_bibcode_search")

        self.gridLayout_2.addWidget(self.B_bibcode_search, 0, 2, 1, 1)

        self.B_advanced_bib_search = QPushButton(self.buttons_gb)
        self.B_advanced_bib_search.setObjectName(u"B_advanced_bib_search")

        self.gridLayout_2.addWidget(self.B_advanced_bib_search, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.buttons_gb, 2, 0, 1, 1)

        self.title_gb_2 = QGroupBox(self.main_gb)
        self.title_gb_2.setObjectName(u"title_gb_2")
        self.verticalLayout_3 = QVBoxLayout(self.title_gb_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.title_gb_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)


        self.gridLayout.addWidget(self.title_gb_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_gb)


        self.retranslateUi(BibliographySearch)

        QMetaObject.connectSlotsByName(BibliographySearch)
    # setupUi

    def retranslateUi(self, BibliographySearch):
        BibliographySearch.setWindowTitle(QCoreApplication.translate("BibliographySearch", u"Form", None))
        self.main_gb.setTitle("")
        self.buttons_gb.setTitle("")
        self.B_reference_search.setText(QCoreApplication.translate("BibliographySearch", u"Reference Search", None))
        self.B_journal_search.setText(QCoreApplication.translate("BibliographySearch", u"Journal Search", None))
        self.B_bibcode_search.setText(QCoreApplication.translate("BibliographySearch", u"Bibcode Search", None))
        self.B_advanced_bib_search.setText(QCoreApplication.translate("BibliographySearch", u"Advanced Bibliographic Search", None))
        self.title_gb_2.setTitle("")
        self.label.setText(QCoreApplication.translate("BibliographySearch", u"Bibliographic Search", None))
    # retranslateUi

