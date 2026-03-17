# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedRadiousUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AdvRadius(object):
    def setupUi(self, AdvRadius):
        if not AdvRadius.objectName():
            AdvRadius.setObjectName(u"AdvRadius")
        AdvRadius.resize(883, 436)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        AdvRadius.setFont(font)
        self.gridLayout = QGridLayout(AdvRadius)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(AdvRadius)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radius_sb = QDoubleSpinBox(self.main_gb)
        self.radius_sb.setObjectName(u"radius_sb")

        self.gridLayout_2.addWidget(self.radius_sb, 1, 1, 1, 1)

        self.AdvCoords_input = QLineEdit(self.main_gb)
        self.AdvCoords_input.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.AdvCoords_input, 0, 1, 1, 2)

        self.label = QLabel(self.main_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.units_label = QLabel(self.main_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 1, 2, 1, 1)

        self.label_2 = QLabel(self.main_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.B_confirm_area = QPushButton(self.main_gb)
        self.B_confirm_area.setObjectName(u"B_confirm_area")

        self.gridLayout_2.addWidget(self.B_confirm_area, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(AdvRadius)

        QMetaObject.connectSlotsByName(AdvRadius)
    # setupUi

    def retranslateUi(self, AdvRadius):
        AdvRadius.setWindowTitle(QCoreApplication.translate("AdvRadius", u"Form", None))
        self.main_gb.setTitle("")
        self.AdvCoords_input.setPlaceholderText(QCoreApplication.translate("AdvRadius", u"e.g.  20 54 05.689 +37 01 17.38", None))
        self.label.setText(QCoreApplication.translate("AdvRadius", u"Coorinates:", None))
        self.units_label.setText(QCoreApplication.translate("AdvRadius", u"Units", None))
        self.label_2.setText(QCoreApplication.translate("AdvRadius", u"Radius:", None))
        self.B_confirm_area.setText(QCoreApplication.translate("AdvRadius", u"Confirm Area", None))
    # retranslateUi

