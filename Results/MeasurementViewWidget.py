# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeasurementViewWidget.ui'
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

class Ui_IndividualMeasurement(object):
    def setupUi(self, IndividualMeasurement):
        if not IndividualMeasurement.objectName():
            IndividualMeasurement.setObjectName(u"IndividualMeasurement")
        IndividualMeasurement.resize(1123, 726)
        self.gridLayout = QGridLayout(IndividualMeasurement)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(IndividualMeasurement)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sources_label = QLabel(self.main_gb)
        self.sources_label.setObjectName(u"sources_label")

        self.gridLayout_2.addWidget(self.sources_label, 0, 1, 1, 1)

        self.category_feature_label = QLabel(self.main_gb)
        self.category_feature_label.setObjectName(u"category_feature_label")

        self.gridLayout_2.addWidget(self.category_feature_label, 0, 0, 1, 1)

        self.B_view_measurements = QPushButton(self.main_gb)
        self.B_view_measurements.setObjectName(u"B_view_measurements")

        self.gridLayout_2.addWidget(self.B_view_measurements, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(IndividualMeasurement)

        QMetaObject.connectSlotsByName(IndividualMeasurement)
    # setupUi

    def retranslateUi(self, IndividualMeasurement):
        IndividualMeasurement.setWindowTitle(QCoreApplication.translate("IndividualMeasurement", u"Form", None))
        self.main_gb.setTitle("")
        self.sources_label.setText(QCoreApplication.translate("IndividualMeasurement", u"n sources", None))
        self.category_feature_label.setText(QCoreApplication.translate("IndividualMeasurement", u"Catagory Feature", None))
        self.B_view_measurements.setText(QCoreApplication.translate("IndividualMeasurement", u"View", None))
    # retranslateUi

