# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ObjectIdPolygUI.ui'
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
    QLabel, QSizePolicy, QSpinBox, QWidget, QPushButton)

class Ui_Polygon(object):
    def setupUi(self, ObjectIdPolyg):
        if not ObjectIdPolyg.objectName():
            ObjectIdPolyg.setObjectName(u"ObjectIdPolyg")
        ObjectIdPolyg.resize(885, 300)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        ObjectIdPolyg.setFont(font)
        self.gridLayout = QGridLayout(ObjectIdPolyg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.polyg_gb = QGroupBox(ObjectIdPolyg)
        self.polyg_gb.setObjectName(u"polyg_gb")
        self.gridLayout_2 = QGridLayout(self.polyg_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.polyg_hypot_sb = QDoubleSpinBox(self.polyg_gb)
        self.polyg_hypot_sb.setObjectName(u"polyg_hypot_sb")

        self.gridLayout_2.addWidget(self.polyg_hypot_sb, 1, 1, 1, 1)

        self.label_2 = QLabel(self.polyg_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.vertices_sb = QSpinBox(self.polyg_gb)
        self.vertices_sb.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.vertices_sb, 0, 1, 1, 1)

        self.label = QLabel(self.polyg_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.units_label = QLabel(self.polyg_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.polyg_gb, 0, 0, 1, 1)

        self.B_confirm_area = QPushButton(ObjectIdPolyg)
        self.B_confirm_area.setObjectName(u"B_confirm_area")
        self.gridLayout.addWidget(self.B_confirm_area, 1, 0, 1, 1, Qt.AlignRight | Qt.AlignBottom)

        self.retranslateUi(ObjectIdPolyg)

        QMetaObject.connectSlotsByName(ObjectIdPolyg)
    # setupUi

    def retranslateUi(self, ObjectIdPolyg):
        ObjectIdPolyg.setWindowTitle(QCoreApplication.translate("ObjectIdPolyg", u"Form", None))
        self.polyg_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("ObjectIdPolyg", u"Center to vertices distance:", None))
        self.label.setText(QCoreApplication.translate("ObjectIdPolyg", u"Vertices of polygon:", None))
        self.units_label.setText(QCoreApplication.translate("ObjectIdPolyg", u"Units", None))
        self.B_confirm_area.setText(QCoreApplication.translate("ObjectIdPolyg", u"Confirm area", None))
    # retranslateUi

