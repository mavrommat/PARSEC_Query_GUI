# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchByObjectID_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SearchByObjectId(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1583, 1057)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_by_object_id_main_gb = QGroupBox(Form)
        self.search_by_object_id_main_gb.setObjectName(u"search_by_object_id_main_gb")
        self.verticalLayout_2 = QVBoxLayout(self.search_by_object_id_main_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_by_object_id_label_gb = QGroupBox(self.search_by_object_id_main_gb)
        self.search_by_object_id_label_gb.setObjectName(u"search_by_object_id_label_gb")
        self.verticalLayout_3 = QVBoxLayout(self.search_by_object_id_label_gb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.search_by_object_id_label_gb)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.search_by_object_id_label_gb)

        self.search_by_object_id_input_gb = QGroupBox(self.search_by_object_id_main_gb)
        self.search_by_object_id_input_gb.setObjectName(u"search_by_object_id_input_gb")
        self.horizontalLayout = QHBoxLayout(self.search_by_object_id_input_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.object_id_input = QLineEdit(self.search_by_object_id_input_gb)
        self.object_id_input.setObjectName(u"object_id_input")

        self.horizontalLayout.addWidget(self.object_id_input)

        self.B_objectID_search = QPushButton(self.search_by_object_id_input_gb)
        self.B_objectID_search.setObjectName(u"B_objectID_search")

        self.horizontalLayout.addWidget(self.B_objectID_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_2.addWidget(self.search_by_object_id_input_gb)

        self.search_by_object_id_input_info_gb = QGroupBox(self.search_by_object_id_main_gb)
        self.search_by_object_id_input_info_gb.setObjectName(u"search_by_object_id_input_info_gb")
        self.verticalLayout_4 = QVBoxLayout(self.search_by_object_id_input_info_gb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.search_by_object_id_input_info_gb)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.search_by_object_id_input_info_gb)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 4)

        self.verticalLayout.addWidget(self.search_by_object_id_main_gb)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_by_object_id_main_gb.setTitle("")
        self.search_by_object_id_label_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"Search by Object Identification", None))
        #self.search_by_object_id_input_gb.setTitle("")
        self.object_id_input.setPlaceholderText(QCoreApplication.translate("Form", u"Provide Identifications (e.g.  M32, NGC2472,...)", None))
        self.B_objectID_search.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.search_by_object_id_input_info_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">How to use:</span></p><p>To ensure a correct search, objects must be written in the exact format used in the bibliography <span style=\" font-style:italic;\">(capitalization is not required)</span>.</p><p>By adding a comma (<span style=\" font-weight:700;\">,</span>) between objects, you can search for multiple items at once.</p></body></html>", None))
    # retranslateUi

