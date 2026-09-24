# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ObjectOverviewUI.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ObjectOverview(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1160, 919)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(Form)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.measurements_gb = QGroupBox(self.main_gb)
        self.measurements_gb.setObjectName(u"measurements_gb")
        self.gridLayout_5 = QGridLayout(self.measurements_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.measurements_sources_label = QLabel(self.measurements_gb)
        self.measurements_sources_label.setObjectName(u"measurements_sources_label")

        self.gridLayout_5.addWidget(self.measurements_sources_label, 1, 0, 1, 1)

        self.c_f_s_label_4 = QLabel(self.measurements_gb)
        self.c_f_s_label_4.setObjectName(u"c_f_s_label_4")

        self.gridLayout_5.addWidget(self.c_f_s_label_4, 2, 1, 1, 1)

        self.c_f_s_label_2 = QLabel(self.measurements_gb)
        self.c_f_s_label_2.setObjectName(u"c_f_s_label_2")

        self.gridLayout_5.addWidget(self.c_f_s_label_2, 3, 0, 1, 1)

        self.c_f_s_label_1 = QLabel(self.measurements_gb)
        self.c_f_s_label_1.setObjectName(u"c_f_s_label_1")

        self.gridLayout_5.addWidget(self.c_f_s_label_1, 2, 0, 1, 1)

        self.c_f_s_label_5 = QLabel(self.measurements_gb)
        self.c_f_s_label_5.setObjectName(u"c_f_s_label_5")

        self.gridLayout_5.addWidget(self.c_f_s_label_5, 3, 1, 1, 1)

        self.B_view_all = QPushButton(self.measurements_gb)
        self.B_view_all.setObjectName(u"B_view_all")

        self.gridLayout_5.addWidget(self.B_view_all, 5, 1, 1, 1)

        self.c_f_s_label_3 = QLabel(self.measurements_gb)
        self.c_f_s_label_3.setObjectName(u"c_f_s_label_3")

        self.gridLayout_5.addWidget(self.c_f_s_label_3, 4, 0, 1, 1)

        self.c_f_s_label_6 = QLabel(self.measurements_gb)
        self.c_f_s_label_6.setObjectName(u"c_f_s_label_6")

        self.gridLayout_5.addWidget(self.c_f_s_label_6, 4, 1, 1, 1)

        self.label_8 = QLabel(self.measurements_gb)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.measurements_gb, 3, 0, 1, 3)

        self.B_close = QPushButton(self.main_gb)
        self.B_close.setObjectName(u"B_close")

        self.gridLayout_2.addWidget(self.B_close, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.id_gb = QGroupBox(self.main_gb)
        self.id_gb.setObjectName(u"id_gb")
        self.verticalLayout = QVBoxLayout(self.id_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.id_gb)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.identifiers_scroll_area = QScrollArea(self.id_gb)
        self.identifiers_scroll_area.setObjectName(u"identifiers_scroll_area")
        self.identifiers_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 581, 199))
        self.identifiers_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.identifiers_scroll_area)


        self.gridLayout_2.addWidget(self.id_gb, 2, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.coordinates_gb = QGroupBox(self.main_gb)
        self.coordinates_gb.setObjectName(u"coordinates_gb")
        self.gridLayout_4 = QGridLayout(self.coordinates_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.epoch_val = QLabel(self.coordinates_gb)
        self.epoch_val.setObjectName(u"epoch_val")

        self.gridLayout_4.addWidget(self.epoch_val, 5, 1, 1, 1)

        self.label_3 = QLabel(self.coordinates_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label_7 = QLabel(self.coordinates_gb)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_5 = QLabel(self.coordinates_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.ra_val = QLabel(self.coordinates_gb)
        self.ra_val.setObjectName(u"ra_val")
        self.ra_val.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.ra_val, 2, 1, 1, 1)

        self.frame_cb = QComboBox(self.coordinates_gb)
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.setObjectName(u"frame_cb")

        self.gridLayout_4.addWidget(self.frame_cb, 4, 1, 1, 1)

        self.label_6 = QLabel(self.coordinates_gb)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_4 = QLabel(self.coordinates_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.format_cb = QComboBox(self.coordinates_gb)
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.format_cb.setObjectName(u"format_cb")

        self.gridLayout_4.addWidget(self.format_cb, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.dec_val = QLabel(self.coordinates_gb)
        self.dec_val.setObjectName(u"dec_val")
        self.dec_val.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.dec_val, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.coordinates_gb, 2, 2, 1, 1)

        self.object_type_id_code_gb = QGroupBox(self.main_gb)
        self.object_type_id_code_gb.setObjectName(u"object_type_id_code_gb")
        self.gridLayout_3 = QGridLayout(self.object_type_id_code_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.object_type_label = QLabel(self.object_type_id_code_gb)
        self.object_type_label.setObjectName(u"object_type_label")
        self.object_type_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_3.addWidget(self.object_type_label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.ObjectId = QLabel(self.object_type_id_code_gb)
        self.ObjectId.setObjectName(u"ObjectId")
        self.ObjectId.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_3.addWidget(self.ObjectId, 2, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label = QLabel(self.object_type_id_code_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.object_type_id_code_gb, 1, 0, 1, 3)

        self.sources_gb = QGroupBox(self.main_gb)
        self.sources_gb.setObjectName(u"sources_gb")
        self.gridLayout_6 = QGridLayout(self.sources_gb)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.sources_gb)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.sources_scroll = QScrollArea(self.sources_gb)
        self.sources_scroll.setObjectName(u"sources_scroll")
        self.sources_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1074, 198))
        self.sources_scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.sources_scroll, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.sources_gb, 4, 0, 1, 3)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_gb.setTitle("")
        self.measurements_gb.setTitle("")
        self.measurements_sources_label.setText(QCoreApplication.translate("Form", u"measurements_sources", None))
        self.c_f_s_label_4.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_4", None))
        self.c_f_s_label_2.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_2", None))
        self.c_f_s_label_1.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_1", None))
        self.c_f_s_label_5.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_5", None))
        self.B_view_all.setText(QCoreApplication.translate("Form", u"View all measurements", None))
        self.c_f_s_label_3.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_3", None))
        self.c_f_s_label_6.setText(QCoreApplication.translate("Form", u"catagory_concept_sources_6", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Available Measurements", None))
        self.B_close.setText(QCoreApplication.translate("Form", u"Close overview", None))
        self.id_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Identifiers", None))
        self.coordinates_gb.setTitle("")
        self.epoch_val.setText(QCoreApplication.translate("Form", u"epoch", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Coordinates", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Epoch:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"DEC:", None))
        self.ra_val.setText(QCoreApplication.translate("Form", u"ra_val", None))
        self.frame_cb.setItemText(0, QCoreApplication.translate("Form", u"ICRS", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("Form", u"Galactic", None))
        self.frame_cb.setItemText(2, QCoreApplication.translate("Form", u"FK5", None))
        self.frame_cb.setItemText(3, QCoreApplication.translate("Form", u"FK4", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Frame:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"RA:", None))
        self.format_cb.setItemText(0, QCoreApplication.translate("Form", u"Sexagesimal", None))
        self.format_cb.setItemText(1, QCoreApplication.translate("Form", u"Decimal degrees", None))

        self.dec_val.setText(QCoreApplication.translate("Form", u"dec_val", None))
        self.object_type_id_code_gb.setTitle("")
        self.object_type_label.setText(QCoreApplication.translate("Form", u"Object Type", None))
        self.ObjectId.setText(QCoreApplication.translate("Form", u"Object ID", None))
        self.label.setText(QCoreApplication.translate("Form", u"Object's Overview ", None))
        self.sources_gb.setTitle("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Sources", None))
    # retranslateUi

