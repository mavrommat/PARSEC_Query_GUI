# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ObjectIdUI.ui'
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

class Ui_Radius(object):
    def setupUi(self, ObjectIdRadius):
        if not ObjectIdRadius.objectName():
            ObjectIdRadius.setObjectName(u"ObjectIdRadius")
        ObjectIdRadius.resize(400, 300)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        ObjectIdRadius.setFont(font)
        self.gridLayout = QGridLayout(ObjectIdRadius)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Radus_main_gb = QGroupBox(ObjectIdRadius)
        self.Radus_main_gb.setObjectName(u"Radus_main_gb")
        self.gridLayout_2 = QGridLayout(self.Radus_main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.Radus_main_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.radius_sb = QDoubleSpinBox(self.Radus_main_gb)
        self.radius_sb.setObjectName(u"radius_sb")

        self.gridLayout_2.addWidget(self.radius_sb, 0, 1, 1, 1)

        self.units_label = QLabel(self.Radus_main_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.Radus_main_gb, 0, 0, 1, 1)

        self.B_confirm_area = QPushButton(ObjectIdRadius)
        self.B_confirm_area.setObjectName(u"B_confirm_area")
        self.gridLayout.addWidget(self.B_confirm_area, 1, 0, 1, 1, Qt.AlignRight | Qt.AlignBottom)

        self.retranslateUi(ObjectIdRadius)

        QMetaObject.connectSlotsByName(ObjectIdRadius)
    # setupUi

    def retranslateUi(self, ObjectIdRadius):
        ObjectIdRadius.setWindowTitle(QCoreApplication.translate("ObjectIdRadius", u"Form", None))
        self.Radus_main_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("ObjectIdRadius", u"Radius:", None))
        self.units_label.setText(QCoreApplication.translate("ObjectIdRadius", u"Units_label", None))
        self.B_confirm_area.setText(QCoreApplication.translate("ObjectIdRectagular", u"Confirm area", None))    
    
    # retranslateUi

