# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox,
    QLabel, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_InfoViewSelection(object):
    def setupUi(self, InfoViewSelection):
        if not InfoViewSelection.objectName():
            InfoViewSelection.setObjectName(u"InfoViewSelection")
        InfoViewSelection.resize(1320, 950)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        InfoViewSelection.setFont(font)
        
        self.gridLayout = QGridLayout(InfoViewSelection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(InfoViewSelection)
        self.main_gb.setObjectName(u"main_gb")
        
        self.verticalLayout = QVBoxLayout(self.main_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.label_gb = QGroupBox(self.main_gb)
        self.label_gb.setObjectName(u"label_gb")
        self.verticalLayout_2 = QVBoxLayout(self.label_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label = QLabel(self.label_gb)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.label_gb)

        self.selections_gb = QGroupBox(self.main_gb)
        self.selections_gb.setObjectName(u"selections_gb")
        self.gridLayout_2 = QGridLayout(self.selections_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.R_all_columns = QRadioButton(self.selections_gb)
        self.R_all_columns.setObjectName(u"R_all_columns")
        self.gridLayout_2.addWidget(self.R_all_columns, 0, 0, 1, 1)

        self.R_specific_columns = QRadioButton(self.selections_gb)
        self.R_specific_columns.setObjectName(u"R_specific_columns")
        self.gridLayout_2.addWidget(self.R_specific_columns, 0, 1, 1, 2)

        self.matrix_view_gb = QGroupBox(self.selections_gb)
        self.matrix_view_gb.setObjectName(u"matrix_view_gb")
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setRetainSizeWhenHidden(True)
        self.matrix_view_gb.setSizePolicy(sizePolicy)

        self.gridLayout_3 = QGridLayout(self.matrix_view_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # --- LABELS (Row 0) ---
        self.label_concept = QLabel(self.matrix_view_gb)
        self.label_concept.setObjectName(u"label_concept")
        self.gridLayout_3.addWidget(self.label_concept, 0, 0, 1, 1)

        self.label_blank = QLabel(self.matrix_view_gb)
        self.label_blank.setObjectName(u"label_blank")
        self.gridLayout_3.addWidget(self.label_blank, 0, 1, 1, 1)

        # --- INTERACTIVE CONTROLS (Row 1) ---
        self.menu_categories_features = QToolButton(self.matrix_view_gb)
        self.menu_categories_features.setObjectName(u"menu_categories_features")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.menu_categories_features.setSizePolicy(sizePolicy1)
        self.gridLayout_3.addWidget(self.menu_categories_features, 1, 0, 1, 1)

        self.options_menu = QToolButton(self.matrix_view_gb)
        self.options_menu.setObjectName(u"options_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.options_menu.setSizePolicy(sizePolicy2)
        self.gridLayout_3.addWidget(self.options_menu, 1, 1, 1, 1)

        self.B_apply_column = QPushButton(self.matrix_view_gb)
        self.B_apply_column.setObjectName(u"B_apply_column")
        self.gridLayout_3.addWidget(self.B_apply_column, 1, 2, 1, 1)

        # --- SCROLL AREA (Row 2) ---
        self.scrollArea = QScrollArea(self.matrix_view_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 570, 632))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 2, 0, 1, 3)

        self.gridLayout_2.addWidget(self.matrix_view_gb, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.selections_gb)

        self.B_confirm_query = QPushButton(self.main_gb)
        self.B_confirm_query.setObjectName(u"B_confirm_query")
        self.verticalLayout.addWidget(self.B_confirm_query)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)

        self.retranslateUi(InfoViewSelection)
        QMetaObject.connectSlotsByName(InfoViewSelection)

    def retranslateUi(self, InfoViewSelection):
        InfoViewSelection.setWindowTitle(QCoreApplication.translate("InfoViewSelection", u"Form", None))
        self.label.setText(QCoreApplication.translate("InfoViewSelection", u"How do you want the information to be displayed?", None))
        self.R_all_columns.setText(QCoreApplication.translate("InfoViewSelection", u"Return all columns", None))
        self.R_specific_columns.setText(QCoreApplication.translate("InfoViewSelection", u"Select specific columns", None))
        self.menu_categories_features.setText(QCoreApplication.translate("InfoViewSelection", u"Select Concept Tree", None))
        self.options_menu.setText(QCoreApplication.translate("InfoViewSelection", u"Placeholder Menu", None))
        self.B_apply_column.setText(QCoreApplication.translate("InfoViewSelection", u"Apply", None))
        self.B_confirm_query.setText(QCoreApplication.translate("InfoViewSelection", u"Confirm Query", None))
        self.label_concept.setText(QCoreApplication.translate("InfoViewSelection", u"Define the Concept Properties:", None))
        self.label_blank.setText(QCoreApplication.translate("InfoViewSelection", u"Future Options:", None))