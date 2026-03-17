# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchAroundObjectSpecifiedCoordsUI.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SearchAround(object):
    def setupUi(self, SearchAroundAnObject):
        if not SearchAroundAnObject.objectName():
            SearchAroundAnObject.setObjectName(u"SearchAroundAnObject")
        SearchAroundAnObject.resize(1957, 1205)
        self.gridLayout = QGridLayout(SearchAroundAnObject)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(SearchAroundAnObject)
        self.main_gb.setObjectName(u"main_gb")
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        self.main_gb.setFont(font)
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

        self.input_text_frames_shape_gb = QGroupBox(self.main_gb)
        self.input_text_frames_shape_gb.setObjectName(u"input_text_frames_shape_gb")
        self.verticalLayout_3 = QVBoxLayout(self.input_text_frames_shape_gb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_text_gb = QGroupBox(self.input_text_frames_shape_gb)
        self.input_text_gb.setObjectName(u"input_text_gb")
        self.verticalLayout_4 = QVBoxLayout(self.input_text_gb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.coords_id_input = QLineEdit(self.input_text_gb)
        self.coords_id_input.setObjectName(u"coords_id_input")

        self.verticalLayout_4.addWidget(self.coords_id_input)


        self.verticalLayout_3.addWidget(self.input_text_gb)

        self.shape_frames_gb = QGroupBox(self.input_text_frames_shape_gb)
        self.shape_frames_gb.setObjectName(u"shape_frames_gb")
        self.horizontalLayout = QHBoxLayout(self.shape_frames_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shape_gb = QGroupBox(self.shape_frames_gb)
        self.shape_gb.setObjectName(u"shape_gb")
        self.verticalLayout_5 = QVBoxLayout(self.shape_gb)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.B_Radius_Search = QPushButton(self.shape_gb)
        self.B_Radius_Search.setObjectName(u"B_Radius_Search")

        self.verticalLayout_5.addWidget(self.B_Radius_Search)

        self.B_Rect_Search = QPushButton(self.shape_gb)
        self.B_Rect_Search.setObjectName(u"B_Rect_Search")

        self.verticalLayout_5.addWidget(self.B_Rect_Search)

        self.B_polyg_Search = QPushButton(self.shape_gb)
        self.B_polyg_Search.setObjectName(u"B_polyg_Search")

        self.verticalLayout_5.addWidget(self.B_polyg_Search)


        self.horizontalLayout.addWidget(self.shape_gb)

        self.frame_gb = QGroupBox(self.shape_frames_gb)
        self.frame_gb.setObjectName(u"frame_gb")
        self.gridLayout_2 = QGridLayout(self.frame_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_cb = QComboBox(self.frame_gb)
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.setObjectName(u"frame_cb")

        self.gridLayout_2.addWidget(self.frame_cb, 1, 3, 1, 1)

        self.epoch_cb = QComboBox(self.frame_gb)
        self.epoch_cb.addItem("")
        self.epoch_cb.addItem("")
        self.epoch_cb.addItem("")
        self.epoch_cb.addItem("")
        self.epoch_cb.setObjectName(u"epoch_cb")

        self.gridLayout_2.addWidget(self.epoch_cb, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.units_cb = QComboBox(self.frame_gb)
        self.units_cb.addItem("")
        self.units_cb.addItem("")
        self.units_cb.addItem("")
        self.units_cb.setObjectName(u"units_cb")

        self.gridLayout_2.addWidget(self.units_cb, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.equinox_cb = QComboBox(self.frame_gb)
        self.equinox_cb.addItem("")
        self.equinox_cb.addItem("")
        self.equinox_cb.addItem("")
        self.equinox_cb.addItem("")
        self.equinox_cb.setObjectName(u"equinox_cb")

        self.gridLayout_2.addWidget(self.equinox_cb, 0, 3, 1, 1)

        self.label_4 = QLabel(self.frame_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.frame_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frame_gb)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.shape_frames_gb)


        self.verticalLayout.addWidget(self.input_text_frames_shape_gb)

        self.widget_gb = QGroupBox(self.main_gb)
        self.widget_gb.setObjectName(u"widget_gb")
        self.gridLayout_3 = QGridLayout(self.widget_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.WidgetCoordsShapeInfo = QWidget(self.widget_gb)
        self.WidgetCoordsShapeInfo.setObjectName(u"WidgetCoordsShapeInfo")

        self.gridLayout_3.addWidget(self.WidgetCoordsShapeInfo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_gb)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout.addWidget(self.main_gb, 1, 0, 1, 1)


        self.retranslateUi(SearchAroundAnObject)

        QMetaObject.connectSlotsByName(SearchAroundAnObject)
    # setupUi

    def retranslateUi(self, SearchAroundAnObject):
        SearchAroundAnObject.setWindowTitle(QCoreApplication.translate("SearchAroundAnObject", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("SearchAroundAnObject", u"Search around an object / Specified coordinates", None))
        self.input_text_frames_shape_gb.setTitle("")
        self.input_text_gb.setTitle("")
        self.coords_id_input.setPlaceholderText(QCoreApplication.translate("SearchAroundAnObject", u"Provide Identification (i.e. M32, ...)/Coordinates (i.e. 20 54 05.689 +37 01 17.38)", None))
        self.shape_frames_gb.setTitle("")
        self.shape_gb.setTitle("")
        self.B_Radius_Search.setText(QCoreApplication.translate("SearchAroundAnObject", u"Radius search", None))
        self.B_Rect_Search.setText(QCoreApplication.translate("SearchAroundAnObject", u"Rectangle search", None))
        self.B_polyg_Search.setText(QCoreApplication.translate("SearchAroundAnObject", u"Polygon search", None))
        self.frame_gb.setTitle("")
        self.frame_cb.setItemText(0, QCoreApplication.translate("SearchAroundAnObject", u"Default", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("SearchAroundAnObject", u"Galactic", None))
        self.frame_cb.setItemText(2, QCoreApplication.translate("SearchAroundAnObject", u"FK5", None))
        self.frame_cb.setItemText(3, QCoreApplication.translate("SearchAroundAnObject", u"FK4", None))
        self.frame_cb.setItemText(4, QCoreApplication.translate("SearchAroundAnObject", u"ICRS", None))

        self.epoch_cb.setItemText(0, QCoreApplication.translate("SearchAroundAnObject", u"Default", None))
        self.epoch_cb.setItemText(1, QCoreApplication.translate("SearchAroundAnObject", u"J2000"
"", None))
        self.epoch_cb.setItemText(2, QCoreApplication.translate("SearchAroundAnObject", u"J1950", None))
        self.epoch_cb.setItemText(3, QCoreApplication.translate("SearchAroundAnObject", u"J1900", None))

        self.label_2.setText(QCoreApplication.translate("SearchAroundAnObject", u"Angular Units:", None))
        self.units_cb.setItemText(0, QCoreApplication.translate("SearchAroundAnObject", u"Degrees"
"", None))
        self.units_cb.setItemText(1, QCoreApplication.translate("SearchAroundAnObject", u"Arcseconds", None))
        self.units_cb.setItemText(2, QCoreApplication.translate("SearchAroundAnObject", u"Arcminutes", None))

        self.label_3.setText(QCoreApplication.translate("SearchAroundAnObject", u"Epoch:", None))
        self.equinox_cb.setItemText(0, QCoreApplication.translate("SearchAroundAnObject", u"Default", None))
        self.equinox_cb.setItemText(1, QCoreApplication.translate("SearchAroundAnObject", u"2000", None))
        self.equinox_cb.setItemText(2, QCoreApplication.translate("SearchAroundAnObject", u"1950", None))
        self.equinox_cb.setItemText(3, QCoreApplication.translate("SearchAroundAnObject", u"1900", None))

        self.label_4.setText(QCoreApplication.translate("SearchAroundAnObject", u"Equinoxe:", None))
        self.label_5.setText(QCoreApplication.translate("SearchAroundAnObject", u"Frame:", None))
        self.widget_gb.setTitle("")
    # retranslateUi

