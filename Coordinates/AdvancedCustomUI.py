# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedCustomUI.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AdvancedCustom(object):
    def setupUi(self, AdvancedCustom):
        if not AdvancedCustom.objectName():
            AdvancedCustom.setObjectName(u"AdvancedCustom")
        AdvancedCustom.resize(1579, 809)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        AdvancedCustom.setFont(font)
        self.gridLayout = QGridLayout(AdvancedCustom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(AdvancedCustom)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.custom_coords_input = QLineEdit(self.main_gb)
        self.custom_coords_input.setObjectName(u"custom_coords_input")

        self.gridLayout_2.addWidget(self.custom_coords_input, 0, 1, 1, 1)

        self.label = QLabel(self.main_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.units_label = QLabel(self.main_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 0, 2, 1, 1)

        self.B_confirm_area = QPushButton(self.main_gb)
        self.B_confirm_area.setObjectName(u"B_confirm_area")

        self.gridLayout_2.addWidget(self.B_confirm_area, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(AdvancedCustom)

        QMetaObject.connectSlotsByName(AdvancedCustom)
    # setupUi

    def retranslateUi(self, AdvancedCustom):
        AdvancedCustom.setWindowTitle(QCoreApplication.translate("AdvancedCustom", u"Form", None))
        self.main_gb.setTitle("")
        self.custom_coords_input.setPlaceholderText(QCoreApplication.translate("AdvancedCustom", u"(RA1,DEC1),(RA2,DEC2),...,(RAn,DECn)", None))
        self.label.setText(QCoreApplication.translate("AdvancedCustom", u"RA/DEC Vertices of custom shape:", None))
        self.units_label.setText(QCoreApplication.translate("AdvancedCustom", u"Units", None))
        self.B_confirm_area.setText(QCoreApplication.translate("AdvancedCustom", u"Confirm Area", None))
    # retranslateUi

