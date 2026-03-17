# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CoordinateSearchUI.ui'
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
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CoordinatesSearch(object):
    def setupUi(self, CoordinatesSearch):
        if not CoordinatesSearch.objectName():
            CoordinatesSearch.setObjectName(u"CoordinatesSearch")
        CoordinatesSearch.resize(1597, 1139)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        CoordinatesSearch.setFont(font)
        self.gridLayout = QGridLayout(CoordinatesSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.coord_search_main_gb = QGroupBox(CoordinatesSearch)
        self.coord_search_main_gb.setObjectName(u"coord_search_main_gb")
        self.horizontalLayout = QHBoxLayout(self.coord_search_main_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.coord_search_label_coord_mode_gb = QGroupBox(self.coord_search_main_gb)
        self.coord_search_label_coord_mode_gb.setObjectName(u"coord_search_label_coord_mode_gb")
        self.verticalLayout = QVBoxLayout(self.coord_search_label_coord_mode_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.coord_search_title = QLabel(self.coord_search_label_coord_mode_gb)
        self.coord_search_title.setObjectName(u"coord_search_title")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.coord_search_title.setFont(font1)

        self.verticalLayout.addWidget(self.coord_search_title)

        self.coord_search_mode_selection_gb = QGroupBox(self.coord_search_label_coord_mode_gb)
        self.coord_search_mode_selection_gb.setObjectName(u"coord_search_mode_selection_gb")
        self.verticalLayout_3 = QVBoxLayout(self.coord_search_mode_selection_gb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.coord_search_mode_selection_sub_gb = QGroupBox(self.coord_search_mode_selection_gb)
        self.coord_search_mode_selection_sub_gb.setObjectName(u"coord_search_mode_selection_sub_gb")
        self.gridLayout_3 = QGridLayout(self.coord_search_mode_selection_sub_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.B_coord_mode_search_around_object_specified_coords = QPushButton(self.coord_search_mode_selection_sub_gb)
        self.B_coord_mode_search_around_object_specified_coords.setObjectName(u"B_coord_mode_search_around_object_specified_coords")

        self.gridLayout_3.addWidget(self.B_coord_mode_search_around_object_specified_coords, 0, 0, 1, 1)

        self.B_coord_mode_advanced_search = QPushButton(self.coord_search_mode_selection_sub_gb)
        self.B_coord_mode_advanced_search.setObjectName(u"B_coord_mode_advanced_search")

        self.gridLayout_3.addWidget(self.B_coord_mode_advanced_search, 1, 0, 1, 1)

        self.gridLayout_3.setRowMinimumHeight(0, 1)

        self.verticalLayout_3.addWidget(self.coord_search_mode_selection_sub_gb)

        self.placeholder_gb = QGroupBox(self.coord_search_mode_selection_gb)
        self.placeholder_gb.setObjectName(u"placeholder_gb")

        self.verticalLayout_3.addWidget(self.placeholder_gb)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self.coord_search_mode_selection_gb)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.coord_search_label_coord_mode_gb)

        self.coord_search_scroll_add_gb = QGroupBox(self.coord_search_main_gb)
        self.coord_search_scroll_add_gb.setObjectName(u"coord_search_scroll_add_gb")
        self.gridLayout_2 = QGridLayout(self.coord_search_scroll_add_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.B_submit_coord_search = QPushButton(self.coord_search_scroll_add_gb)
        self.B_submit_coord_search.setObjectName(u"B_submit_coord_search")

        self.gridLayout_2.addWidget(self.B_submit_coord_search, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.scrollArea = QScrollArea(self.coord_search_scroll_add_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 963, 483))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 0, 1, 2)

        self.B_add_search_area = QPushButton(self.coord_search_scroll_add_gb)
        self.B_add_search_area.setObjectName(u"B_add_search_area")

        self.gridLayout_2.addWidget(self.B_add_search_area, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.B_delete_search_area = QPushButton(self.coord_search_scroll_add_gb)
        self.B_delete_search_area.setObjectName(u"B_delete_search_area")

        self.gridLayout_2.addWidget(self.B_delete_search_area, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 3)

        self.gridLayout_2.setRowMinimumHeight(0, 1)
        self.gridLayout_2.setRowMinimumHeight(2, 3)
        self.gridLayout_2.setRowMinimumHeight(3, 3)

        self.horizontalLayout.addWidget(self.coord_search_scroll_add_gb)


        self.gridLayout.addWidget(self.coord_search_main_gb, 0, 0, 1, 1)


        self.retranslateUi(CoordinatesSearch)

        QMetaObject.connectSlotsByName(CoordinatesSearch)
    # setupUi

    def retranslateUi(self, CoordinatesSearch):
        CoordinatesSearch.setWindowTitle(QCoreApplication.translate("CoordinatesSearch", u"Form", None))
        self.coord_search_main_gb.setTitle("")
        self.coord_search_label_coord_mode_gb.setTitle("")
        self.coord_search_title.setText(QCoreApplication.translate("CoordinatesSearch", u"Coordinates Search", None))
        self.coord_search_mode_selection_gb.setTitle("")
        self.coord_search_mode_selection_sub_gb.setTitle("")
        self.B_coord_mode_search_around_object_specified_coords.setText(QCoreApplication.translate("CoordinatesSearch", u"Searching around an object/Specified coordinates", None))
        self.B_coord_mode_advanced_search.setText(QCoreApplication.translate("CoordinatesSearch", u"Advanced coordinate search", None))
        self.placeholder_gb.setTitle("")
        self.coord_search_scroll_add_gb.setTitle("")
        self.B_submit_coord_search.setText(QCoreApplication.translate("CoordinatesSearch", u"Submit", None))
        self.B_add_search_area.setText(QCoreApplication.translate("CoordinatesSearch", u"Add new area search", None))
        self.B_delete_search_area.setText(QCoreApplication.translate("CoordinatesSearch", u"Delete area search", None))
    # retranslateUi

