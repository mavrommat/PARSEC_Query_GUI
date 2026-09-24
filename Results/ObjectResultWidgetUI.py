# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ObjectResultWidgetUI.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_ObjectWidget(object):
    def setupUi(self, ObjectWidget):
        if not ObjectWidget.objectName():
            ObjectWidget.setObjectName(u"ObjectWidget")
        ObjectWidget.resize(1145, 798)
        self.gridLayout = QGridLayout(ObjectWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(ObjectWidget)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.B_view_obj = QPushButton(self.main_gb)
        self.B_view_obj.setObjectName(u"B_view_obj")

        self.gridLayout_2.addWidget(self.B_view_obj, 5, 1, 1, 1)

        self.object_type_label = QLabel(self.main_gb)
        self.object_type_label.setObjectName(u"object_type_label")

        self.gridLayout_2.addWidget(self.object_type_label, 0, 1, 1, 1)

        self.label_other_names = QLabel(self.main_gb)
        self.label_other_names.setObjectName(u"label_other_names")

        self.gridLayout_2.addWidget(self.label_other_names, 2, 0, 1, 1)

        self.label_id_code = QLabel(self.main_gb)
        self.label_id_code.setObjectName(u"label_id_code")

        self.gridLayout_2.addWidget(self.label_id_code, 1, 0, 1, 1)

        self.label_object_type = QLabel(self.main_gb)
        self.label_object_type.setObjectName(u"label_object_type")

        self.gridLayout_2.addWidget(self.label_object_type, 0, 0, 1, 1)

        self.other_names_label = QLabel(self.main_gb)
        self.other_names_label.setObjectName(u"other_names_label")

        self.gridLayout_2.addWidget(self.other_names_label, 2, 1, 1, 1)

        self.measurements_sources_label = QLabel(self.main_gb)
        self.measurements_sources_label.setObjectName(u"measurements_sources_label")

        self.gridLayout_2.addWidget(self.measurements_sources_label, 4, 0, 1, 2)

        self.id_code_label = QLabel(self.main_gb)
        self.id_code_label.setObjectName(u"id_code_label")

        self.gridLayout_2.addWidget(self.id_code_label, 1, 1, 1, 1)

        self.ra_dec_frame_label = QLabel(self.main_gb)
        self.ra_dec_frame_label.setObjectName(u"ra_dec_frame_label")

        self.gridLayout_2.addWidget(self.ra_dec_frame_label, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.main_gb, 1, 0, 1, 1)


        self.retranslateUi(ObjectWidget)

        QMetaObject.connectSlotsByName(ObjectWidget)
    # setupUi

    def retranslateUi(self, ObjectWidget):
        ObjectWidget.setWindowTitle(QCoreApplication.translate("ObjectWidget", u"Form", None))
        self.main_gb.setTitle("")
        self.B_view_obj.setText(QCoreApplication.translate("ObjectWidget", u"View Object", None))
        self.object_type_label.setText(QCoreApplication.translate("ObjectWidget", u"N/A", None))
        self.label_other_names.setText(QCoreApplication.translate("ObjectWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Other names:</span></p></body></html>", None))
        self.label_id_code.setText(QCoreApplication.translate("ObjectWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Identifier code:</span></p></body></html>", None))
        self.label_object_type.setText(QCoreApplication.translate("ObjectWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Object Type:</span></p></body></html>", None))
        self.other_names_label.setText(QCoreApplication.translate("ObjectWidget", u"N/A", None))
        self.measurements_sources_label.setText(QCoreApplication.translate("ObjectWidget", u"<html><head/><body><p>n <span style=\" font-weight:700;\">Measurements</span><span style=\" font-weight:700;\">-</span> k S<span style=\" font-weight:700;\">ources</span></p></body></html>", None))
        self.id_code_label.setText(QCoreApplication.translate("ObjectWidget", u"N/A", None))
        self.ra_dec_frame_label.setText(QCoreApplication.translate("ObjectWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">RA:</span>label <span style=\" font-weight:700;\">DEC:</span>label <span style=\" font-weight:700;\">Frame</span></p></body></html>", None))
    # retranslateUi

