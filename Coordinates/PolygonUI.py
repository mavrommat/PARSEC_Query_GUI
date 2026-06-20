# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QSpinBox, QPushButton)

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
        
        # --- Vertices Input (Row 0) ---
        self.label = QLabel(self.polyg_gb)
        self.label.setObjectName(u"label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.vertices_sb = QSpinBox(self.polyg_gb)
        self.vertices_sb.setObjectName(u"spinBox")
        # Set a minimum of 3 vertices (a polygon needs at least 3 sides)
        self.vertices_sb.setMinimum(3) 
        self.gridLayout_2.addWidget(self.vertices_sb, 0, 1, 1, 1)

        # --- Single Side Length Input (Row 1) ---
        self.side_label = QLabel(self.polyg_gb)
        self.side_label.setObjectName(u"side_label")
        self.gridLayout_2.addWidget(self.side_label, 1, 0, 1, 1)

        self.side_sb = QDoubleSpinBox(self.polyg_gb)
        self.side_sb.setObjectName(u"side_sb")
        self.gridLayout_2.addWidget(self.side_sb, 1, 1, 1, 1)

        self.side_units_label = QLabel(self.polyg_gb)
        self.side_units_label.setObjectName(u"side_units_label")
        self.gridLayout_2.addWidget(self.side_units_label, 1, 2, 1, 1)

        # --- Main Layout Assembly ---
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
        
        self.label.setText(QCoreApplication.translate("ObjectIdPolyg", u"Vertices of polygon:", None))
        
        # Translations for Side Length
        self.side_label.setText(QCoreApplication.translate("ObjectIdPolyg", u"Side length:", None))
        self.side_units_label.setText(QCoreApplication.translate("ObjectIdPolyg", u"Units", None))
        
        self.B_confirm_area.setText(QCoreApplication.translate("ObjectIdPolyg", u"Confirm area", None))
    # retranslateUi