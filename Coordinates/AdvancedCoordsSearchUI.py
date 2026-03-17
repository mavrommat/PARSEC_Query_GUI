# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedCoordsSearch.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AdvancedCoordsSearch(object):
    def setupUi(self, AdvancedCoordsSearch):
        if not AdvancedCoordsSearch.objectName():
            AdvancedCoordsSearch.setObjectName(u"AdvancedCoordsSearch")
        AdvancedCoordsSearch.resize(1957, 1205)
        self.gridLayout = QGridLayout(AdvancedCoordsSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(AdvancedCoordsSearch)
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

        self.B_Custom_Search = QPushButton(self.shape_gb)
        self.B_Custom_Search.setObjectName(u"B_Custom_Search")

        self.verticalLayout_5.addWidget(self.B_Custom_Search)


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


        self.retranslateUi(AdvancedCoordsSearch)

        QMetaObject.connectSlotsByName(AdvancedCoordsSearch)
    # setupUi

    def retranslateUi(self, AdvancedCoordsSearch):
        AdvancedCoordsSearch.setWindowTitle(QCoreApplication.translate("AdvancedCoordsSearch", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Advanced Coordinate search", None))
        self.input_text_frames_shape_gb.setTitle("")
        self.shape_frames_gb.setTitle("")
        self.shape_gb.setTitle("")
        self.B_Radius_Search.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Radius search", None))
        self.B_Rect_Search.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Rectangle search", None))
        self.B_Custom_Search.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Custom shape search", None))
        self.frame_gb.setTitle("")
        self.frame_cb.setItemText(0, QCoreApplication.translate("AdvancedCoordsSearch", u"Default", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("AdvancedCoordsSearch", u"Galactic", None))
        self.frame_cb.setItemText(2, QCoreApplication.translate("AdvancedCoordsSearch", u"FK5", None))
        self.frame_cb.setItemText(3, QCoreApplication.translate("AdvancedCoordsSearch", u"FK4", None))
        self.frame_cb.setItemText(4, QCoreApplication.translate("AdvancedCoordsSearch", u"ICRS", None))

        self.epoch_cb.setItemText(0, QCoreApplication.translate("AdvancedCoordsSearch", u"Default", None))
        self.epoch_cb.setItemText(1, QCoreApplication.translate("AdvancedCoordsSearch", u"J2000", None))
        self.epoch_cb.setItemText(2, QCoreApplication.translate("AdvancedCoordsSearch", u"J1950", None))
        self.epoch_cb.setItemText(3, QCoreApplication.translate("AdvancedCoordsSearch", u"J1900", None))

        self.label_2.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Angular Units:", None))
        self.units_cb.setItemText(0, QCoreApplication.translate("AdvancedCoordsSearch", u"Degrees", None))
        self.units_cb.setItemText(1, QCoreApplication.translate("AdvancedCoordsSearch", u"Arcseconds", None))
        self.units_cb.setItemText(2, QCoreApplication.translate("AdvancedCoordsSearch", u"Arcminutes", None))

        self.label_3.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Epoch:", None))
        self.equinox_cb.setItemText(0, QCoreApplication.translate("AdvancedCoordsSearch", u"Default", None))
        self.equinox_cb.setItemText(1, QCoreApplication.translate("AdvancedCoordsSearch", u"2000", None))
        self.equinox_cb.setItemText(2, QCoreApplication.translate("AdvancedCoordsSearch", u"1950", None))
        self.equinox_cb.setItemText(3, QCoreApplication.translate("AdvancedCoordsSearch", u"1900", None))

        self.label_4.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Equinoxe:", None))
        self.label_5.setText(QCoreApplication.translate("AdvancedCoordsSearch", u"Frame:", None))
        self.widget_gb.setTitle("")
    # retranslateUi

