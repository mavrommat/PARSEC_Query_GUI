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
        
        # --- Width Inputs (Row 0) ---
        self.width_label = QLabel(self.rectangular_gb)
        self.width_label.setObjectName(u"width_label")
        self.gridLayout_2.addWidget(self.width_label, 0, 0, 1, 1)

        self.width_sb = QDoubleSpinBox(self.rectangular_gb)
        self.width_sb.setObjectName(u"width_sb")
        self.gridLayout_2.addWidget(self.width_sb, 0, 1, 1, 1)

        # RENAMED TO width_units_label
        self.width_units_label = QLabel(self.rectangular_gb)
        self.width_units_label.setObjectName(u"width_units_label")
        self.gridLayout_2.addWidget(self.width_units_label, 0, 2, 1, 1)

        # --- Height Inputs (Row 1) ---
        self.height_label = QLabel(self.rectangular_gb)
        self.height_label.setObjectName(u"height_label")
        self.gridLayout_2.addWidget(self.height_label, 1, 0, 1, 1)

        self.height_sb = QDoubleSpinBox(self.rectangular_gb)
        self.height_sb.setObjectName(u"height_sb")
        self.gridLayout_2.addWidget(self.height_sb, 1, 1, 1, 1)

        # RENAMED TO height_units_label
        self.height_units_label = QLabel(self.rectangular_gb)
        self.height_units_label.setObjectName(u"height_units_label")
        self.gridLayout_2.addWidget(self.height_units_label, 1, 2, 1, 1)

        # --- Main Layout Assembly ---
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
        
        # Translations for Width
        self.width_label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Side Width:", None))
        self.width_units_label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Units", None)) # UPDATED HERE
        
        # Translations for Height
        self.height_label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Height:", None))
        self.height_units_label.setText(QCoreApplication.translate("ObjectIdRectagular", u"Units", None)) # UPDATED HERE
        
        self.B_confirm_area.setText(QCoreApplication.translate("ObjectIdRectagular", u"Confirm area", None))
    # retranslateUi