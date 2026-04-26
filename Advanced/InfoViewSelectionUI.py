# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoViewSelectionUI.ui'
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
    QLabel, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout, QWidget)

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
        self.R_default = QRadioButton(self.selections_gb)
        self.R_default.setObjectName(u"R_default")

        self.gridLayout_2.addWidget(self.R_default, 0, 1, 1, 2)

        self.R_object_view = QRadioButton(self.selections_gb)
        self.R_object_view.setObjectName(u"R_object_view")

        self.gridLayout_2.addWidget(self.R_object_view, 0, 0, 1, 1)

        self.matrix_view_gb = QGroupBox(self.selections_gb)
        self.matrix_view_gb.setObjectName(u"matrix_view_gb")
        self.gridLayout_3 = QGridLayout(self.matrix_view_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        #-----
        self.menu_categories_features = QToolButton(self.matrix_view_gb)
        self.menu_categories_features.setObjectName(u"menu_categories_features")
        self.gridLayout_3.addWidget(self.menu_categories_features, 0, 1, 1, 1)
        #-----
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.B_del_feature = QPushButton(self.matrix_view_gb)
        self.B_del_feature.setObjectName(u"B_del_feature")

        self.gridLayout_3.addWidget(self.B_del_feature, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.matrix_view_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 570, 632))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.matrix_view_gb, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setRowMinimumHeight(0, 1)
        self.gridLayout_2.setRowMinimumHeight(1, 1)

        self.verticalLayout.addWidget(self.selections_gb)

        self.B_confirm_query = QPushButton(self.main_gb)
        self.B_confirm_query.setObjectName(u"B_confirm_query")

        self.verticalLayout.addWidget(self.B_confirm_query)

        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(InfoViewSelection)

        QMetaObject.connectSlotsByName(InfoViewSelection)
    # setupUi

    def retranslateUi(self, InfoViewSelection):
        InfoViewSelection.setWindowTitle(QCoreApplication.translate("InfoViewSelection", u"Form", None))
        self.main_gb.setTitle("")
        self.label_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("InfoViewSelection", u"How do you want the information to be diplayed?", None))
        self.selections_gb.setTitle("")
        self.R_default.setText(QCoreApplication.translate("InfoViewSelection", u"Matrix Vew", None))
        self.R_object_view.setText(QCoreApplication.translate("InfoViewSelection", u"Default (Object View)", None))
        self.matrix_view_gb.setTitle("")
        self.B_del_feature.setText(QCoreApplication.translate("InfoViewSelection", u"Delete last feature", None))
        self.B_confirm_query.setText(QCoreApplication.translate("InfoViewSelection", u"Confirm Query", None))
        self.menu_categories_features.setText(QCoreApplication.translate("InfoViewSelection", u"Select Concept", None))
    # retranslateUi

