# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ObjectIdRectanUI.ui'
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
    QLabel, QSizePolicy, QWidget, QPushButton)

class Ui_Rectagular(object):
    def setupUi(self, ObjectIdRectagular):
        if not ObjectIdRectagular.objectName():
            ObjectIdRectagular.setObjectName(u"ObjectIdRectagular")
        ObjectIdRectagular.resize(933, 300)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        ObjectIdRectagular.setFont(font)
        self.gridLayout = QGridLayout(ObjectIdRectagular)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rectangular_gb = QGroupBox(ObjectIdRectagular)
        self.rectangular_gb.setObjectName(u"rectangular_gb")
        self.gridLayout_2 = QGridLayout(self.rectangular_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.hypot_sb = QDoubleSpinBox(self.rectangular_gb)
        self.hypot_sb.setObjectName(u"hypot_sb")

        self.gridLayout_2.addWidget(self.hypot_sb, 0, 1, 1, 1)

        self.label = QLabel(self.rectangular_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.units_label = QLabel(self.rectangular_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.rectangular_gb, 0, 0, 1, 1)

        self.B_confirm_area = QPushButton(ObjectIdRectagular)
        self.B_confirm_area.setObjectName(u"B_confirm_area")
        self.gridLayout.addWidget(self.B_confirm_area, 1, 0, 1, 1, Qt.AlignRight | Qt.AlignBottom)

        self.retranslateUi(ObjectIdRectagular)

        QMetaObject.connectSlotsByName(ObjectIdRectagular)

       
    # setupUi

    def retranslateUi(self, ObjectIdRectagular):
        ObjectIdRectagular.setWindowTitle(QCoreApplication.translate("ObjectIdRectagular", u"Form", None))
        self.rectangular_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Hypotenuse distance from center:", None))
        self.units_label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Units", None))
        self.B_confirm_area.setText(QCoreApplication.translate("ObjectIdRectagular", u"Confirm area", None))
    
    # retranslateUi

