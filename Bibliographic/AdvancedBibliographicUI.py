# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedBibliographicUI.ui'
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
    QLineEdit, QTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AdvancedBibliographic(object):
    def setupUi(self, AdvancedBibliographic):
        if not AdvancedBibliographic.objectName():
            AdvancedBibliographic.setObjectName(u"AdvancedBibliographic")
        AdvancedBibliographic.resize(1657, 1144)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        AdvancedBibliographic.setFont(font)
        self.gridLayout = QGridLayout(AdvancedBibliographic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(AdvancedBibliographic)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.publication_data_gb = QGroupBox(self.main_gb)
        self.publication_data_gb.setObjectName(u"publication_data_gb")
        self.gridLayout_4 = QGridLayout(self.publication_data_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.publication_data_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.Input_start_year = QLineEdit(self.publication_data_gb)
        self.Input_start_year.setObjectName(u"Input_start_year")

        self.gridLayout_4.addWidget(self.Input_start_year, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 7, 1, 1)

        self.Input_end_year = QLineEdit(self.publication_data_gb)
        self.Input_end_year.setObjectName(u"Input_end_year")

        self.gridLayout_4.addWidget(self.Input_end_year, 1, 6, 1, 1)

        self.Input_start_month = QLineEdit(self.publication_data_gb)
        self.Input_start_month.setObjectName(u"Input_start_month")

        self.gridLayout_4.addWidget(self.Input_start_month, 1, 0, 1, 1)

        self.label_6 = QLabel(self.publication_data_gb)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 3, 1, 1)

        self.Input_end_month = QLineEdit(self.publication_data_gb)
        self.Input_end_month.setObjectName(u"Input_end_month")

        self.gridLayout_4.addWidget(self.Input_end_month, 1, 4, 1, 1)

        self.label_7 = QLabel(self.publication_data_gb)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 5, 1, 1)

        self.label_4 = QLabel(self.publication_data_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 3)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(4, 1)
        self.gridLayout_4.setColumnStretch(6, 1)
        self.gridLayout_4.setColumnStretch(7, 4)

        self.gridLayout_2.addWidget(self.publication_data_gb, 2, 0, 1, 1)

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

        self.Abstract_keywords_gb = QGroupBox(self.main_gb)
        self.Abstract_keywords_gb.setObjectName(u"Abstract_keywords_gb")
        self.gridLayout_6 = QGridLayout(self.Abstract_keywords_gb)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.Abstract_keywords_gb)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.R_and_abs_keyw = QRadioButton(self.Abstract_keywords_gb)
        self.R_and_abs_keyw.setObjectName(u"R_and_abs_keyw")

        self.gridLayout_6.addWidget(self.R_and_abs_keyw, 0, 1, 1, 1)

        self.R_or_abs_keyw = QRadioButton(self.Abstract_keywords_gb)
        self.R_or_abs_keyw.setObjectName(u"R_or_abs_keyw")

        self.gridLayout_6.addWidget(self.R_or_abs_keyw, 0, 2, 1, 1)

        self.Input_abstract_keywords = QLineEdit(self.Abstract_keywords_gb)
        self.Input_abstract_keywords.setObjectName(u"Input_abstract_keywords")

        self.gridLayout_6.addWidget(self.Input_abstract_keywords, 1, 0, 1, 3)


        self.gridLayout_2.addWidget(self.Abstract_keywords_gb, 4, 0, 1, 1)

        self.author_object_gb = QGroupBox(self.main_gb)
        self.author_object_gb.setObjectName(u"author_object_gb")
        self.gridLayout_3 = QGridLayout(self.author_object_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.R_and_object = QRadioButton(self.author_object_gb)
        self.R_and_object.setObjectName(u"R_and_object")

        self.gridLayout_3.addWidget(self.R_and_object, 0, 5, 1, 1)

        self.R_and_author = QRadioButton(self.author_object_gb)
        self.R_and_author.setObjectName(u"R_and_author")

        self.gridLayout_3.addWidget(self.R_and_author, 0, 1, 1, 1)

        self.label_3 = QLabel(self.author_object_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)

        self.Input_objects = QTextEdit(self.author_object_gb)
        self.Input_objects.setObjectName(u"Input_objects")

        self.gridLayout_3.addWidget(self.Input_objects, 1, 4, 1, 3)

        self.Input_authors = QTextEdit(self.author_object_gb)
        self.Input_authors.setObjectName(u"Input_authors")

        self.gridLayout_3.addWidget(self.Input_authors, 1, 0, 1, 3)

        self.label_2 = QLabel(self.author_object_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.R_or_object = QRadioButton(self.author_object_gb)
        self.R_or_object.setObjectName(u"R_or_object")

        self.gridLayout_3.addWidget(self.R_or_object, 0, 6, 1, 1)

        self.R_or_author = QRadioButton(self.author_object_gb)
        self.R_or_author.setObjectName(u"R_or_author")

        self.gridLayout_3.addWidget(self.R_or_author, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 3, 2, 1)


        self.gridLayout_2.addWidget(self.author_object_gb, 1, 0, 1, 1)

        self.paper_title_gb = QGroupBox(self.main_gb)
        self.paper_title_gb.setObjectName(u"paper_title_gb")
        self.gridLayout_5 = QGridLayout(self.paper_title_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.R_and_title = QRadioButton(self.paper_title_gb)
        self.R_and_title.setObjectName(u"R_and_title")

        self.gridLayout_5.addWidget(self.R_and_title, 0, 1, 1, 1)

        self.label_8 = QLabel(self.paper_title_gb)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.R_or_title = QRadioButton(self.paper_title_gb)
        self.R_or_title.setObjectName(u"R_or_title")

        self.gridLayout_5.addWidget(self.R_or_title, 0, 2, 1, 1)

        self.Input_title = QLineEdit(self.paper_title_gb)
        self.Input_title.setObjectName(u"Input_title")

        self.gridLayout_5.addWidget(self.Input_title, 1, 0, 1, 3)


        self.gridLayout_2.addWidget(self.paper_title_gb, 3, 0, 1, 1)

        self.sorting_gb = QGroupBox(self.main_gb)
        self.sorting_gb.setObjectName(u"sorting_gb")
        self.gridLayout_7 = QGridLayout(self.sorting_gb)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.B_clear_all = QPushButton(self.sorting_gb)
        self.B_clear_all.setObjectName(u"B_clear_all")

        self.gridLayout_7.addWidget(self.B_clear_all, 0, 1, 1, 1)

        self.B_submit = QPushButton(self.sorting_gb)
        self.B_submit.setObjectName(u"B_submit")

        self.gridLayout_7.addWidget(self.B_submit, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.sorting_gb, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(AdvancedBibliographic)

        QMetaObject.connectSlotsByName(AdvancedBibliographic)
    # setupUi

    def retranslateUi(self, AdvancedBibliographic):
        AdvancedBibliographic.setWindowTitle(QCoreApplication.translate("AdvancedBibliographic", u"Form", None))
        self.main_gb.setTitle("")
        self.publication_data_gb.setTitle("")
        self.label_5.setText(QCoreApplication.translate("AdvancedBibliographic", u"/", None))
        self.Input_start_year.setPlaceholderText(QCoreApplication.translate("AdvancedBibliographic", u"YYYY", None))
        self.Input_end_year.setPlaceholderText(QCoreApplication.translate("AdvancedBibliographic", u"YYYY", None))
        self.Input_start_month.setPlaceholderText(QCoreApplication.translate("AdvancedBibliographic", u"MM", None))
        self.label_6.setText(QCoreApplication.translate("AdvancedBibliographic", u"and ", None))
        self.Input_end_month.setPlaceholderText(QCoreApplication.translate("AdvancedBibliographic", u"MM", None))
        self.label_7.setText(QCoreApplication.translate("AdvancedBibliographic", u"/", None))
        self.label_4.setText(QCoreApplication.translate("AdvancedBibliographic", u"Publication date between:", None))
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("AdvancedBibliographic", u"Advanced Bibliographic Search", None))
        self.Abstract_keywords_gb.setTitle("")
        self.label_9.setText(QCoreApplication.translate("AdvancedBibliographic", u"Abstract/Keywords", None))
        self.R_and_abs_keyw.setText(QCoreApplication.translate("AdvancedBibliographic", u"AND", None))
        self.R_or_abs_keyw.setText(QCoreApplication.translate("AdvancedBibliographic", u"OR", None))
        self.author_object_gb.setTitle("")
        self.R_and_object.setText(QCoreApplication.translate("AdvancedBibliographic", u"AND", None))
        self.R_and_author.setText(QCoreApplication.translate("AdvancedBibliographic", u"AND", None))
        self.label_3.setText(QCoreApplication.translate("AdvancedBibliographic", u"Object:", None))
        self.Input_authors.setPlaceholderText("Last name, First name. Separate entries by parentheses or new lines.")
        self.Input_objects.setPlaceholderText(QCoreApplication.translate("AdvancedBibliographic", u"Enter an object identification separeted by comma parenthesis or one per line.\n""", None))
        self.label_2.setText(QCoreApplication.translate("AdvancedBibliographic", u"Author:", None))
        self.R_or_object.setText(QCoreApplication.translate("AdvancedBibliographic", u"OR", None))
        self.R_or_author.setText(QCoreApplication.translate("AdvancedBibliographic", u"OR", None))
        self.paper_title_gb.setTitle("")
        self.R_and_title.setText(QCoreApplication.translate("AdvancedBibliographic", u"AND", None))
        self.label_8.setText(QCoreApplication.translate("AdvancedBibliographic", u"Title:", None))
        self.R_or_title.setText(QCoreApplication.translate("AdvancedBibliographic", u"OR", None))
        self.sorting_gb.setTitle("")
        self.B_clear_all.setText(QCoreApplication.translate("AdvancedBibliographic", u"Clear All", None))
        self.B_submit.setText(QCoreApplication.translate("AdvancedBibliographic", u"Submit", None))
    # retranslateUi

