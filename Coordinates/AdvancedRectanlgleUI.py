# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedRectangular.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_AdvancedRectangle(object):
    def setupUi(self, AdvancedRectangular):
        if not AdvancedRectangular.objectName():
            AdvancedRectangular.setObjectName(u"AdvancedRectangular")
        AdvancedRectangular.resize(1673, 1057)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        AdvancedRectangular.setFont(font)
        self.gridLayout = QGridLayout(AdvancedRectangular)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(AdvancedRectangular)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vertices_ra_dec_input = QLineEdit(self.main_gb)
        self.vertices_ra_dec_input.setObjectName(u"vertices_ra_dec_input")

        self.gridLayout_2.addWidget(self.vertices_ra_dec_input, 2, 1, 1, 1)

        self.label = QLabel(self.main_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.units_label = QLabel(self.main_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_2.addWidget(self.units_label, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 2)

        self.B_confirm_area = QPushButton(self.main_gb)
        self.B_confirm_area.setObjectName(u"B_confirm_area")

        self.gridLayout_2.addWidget(self.B_confirm_area, 3, 2, 1, 2)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(AdvancedRectangular)

        QMetaObject.connectSlotsByName(AdvancedRectangular)
    # setupUi

    def retranslateUi(self, AdvancedRectangular):
        AdvancedRectangular.setWindowTitle(QCoreApplication.translate("AdvancedRectangular", u"Form", None))
        self.main_gb.setTitle("")
        self.vertices_ra_dec_input.setPlaceholderText(QCoreApplication.translate("AdvancedRectangular", u"e.g. (RA1,DEC1),(RA2,DEC2)", None))
        self.label.setText(QCoreApplication.translate("AdvancedRectangular", u"Vertices RA/DEC:", None))
        self.units_label.setText(QCoreApplication.translate("AdvancedRectangular", u"Units", None))
        self.B_confirm_area.setText(QCoreApplication.translate("AdvancedRectangular", u"Confirm Area", None))
    # retranslateUi

