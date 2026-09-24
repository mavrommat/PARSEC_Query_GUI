# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SingleMeasurement.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SingleMeasurement(object):
    def setupUi(self, SingleMeasurement):
        if not SingleMeasurement.objectName():
            SingleMeasurement.setObjectName(u"SingleMeasurement")
        SingleMeasurement.resize(1179, 842)
        self.gridLayout = QGridLayout(SingleMeasurement)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(SingleMeasurement)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_gb = QGroupBox(self.groupBox)
        self.button_gb.setObjectName(u"button_gb")
        self.verticalLayout = QVBoxLayout(self.button_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.B_details = QPushButton(self.button_gb)
        self.B_details.setObjectName(u"B_details")

        self.verticalLayout.addWidget(self.B_details)

        self.verticalLayout.setStretch(0, 1)

        self.gridLayout_2.addWidget(self.button_gb, 0, 1, 1, 1)

        self.label_gb = QGroupBox(self.groupBox)
        self.label_gb.setObjectName(u"label_gb")
        self.gridLayout_3 = QGridLayout(self.label_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.units_label = QLabel(self.label_gb)
        self.units_label.setObjectName(u"units_label")

        self.gridLayout_3.addWidget(self.units_label, 4, 0, 1, 1)

        self.auxiliary_label = QLabel(self.label_gb)
        self.auxiliary_label.setObjectName(u"auxiliary_label")

        self.gridLayout_3.addWidget(self.auxiliary_label, 0, 0, 1, 1)

        self.auxiliary = QLabel(self.label_gb)
        self.auxiliary.setObjectName(u"auxiliary")

        self.gridLayout_3.addWidget(self.auxiliary, 0, 1, 1, 1)

        self.characterisation = QLabel(self.label_gb)
        self.characterisation.setObjectName(u"characterisation")

        self.gridLayout_3.addWidget(self.characterisation, 1, 1, 1, 1)

        self.characterisation_label = QLabel(self.label_gb)
        self.characterisation_label.setObjectName(u"characterisation_label")

        self.gridLayout_3.addWidget(self.characterisation_label, 1, 0, 1, 1)

        self.value = QLabel(self.label_gb)
        self.value.setObjectName(u"value")

        self.gridLayout_3.addWidget(self.value, 2, 1, 1, 1)

        self.value_label = QLabel(self.label_gb)
        self.value_label.setObjectName(u"value_label")

        self.gridLayout_3.addWidget(self.value_label, 2, 0, 1, 1)

        self.units = QLabel(self.label_gb)
        self.units.setObjectName(u"units")

        self.gridLayout_3.addWidget(self.units, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.label_gb, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(SingleMeasurement)

        QMetaObject.connectSlotsByName(SingleMeasurement)
    # setupUi

    def retranslateUi(self, SingleMeasurement):
        SingleMeasurement.setWindowTitle(QCoreApplication.translate("SingleMeasurement", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SingleMeasurement", u"", None))
        self.button_gb.setTitle("")
        self.B_details.setText(QCoreApplication.translate("SingleMeasurement", u"Show Details", None))
        self.label_gb.setTitle("")
        self.units_label.setText(QCoreApplication.translate("SingleMeasurement", u"Units:", None))
        self.auxiliary_label.setText(QCoreApplication.translate("SingleMeasurement", u"Auxiliary:", None))
        self.auxiliary.setText(QCoreApplication.translate("SingleMeasurement", u"aux", None))
        self.characterisation.setText(QCoreApplication.translate("SingleMeasurement", u"char", None))
        self.characterisation_label.setText(QCoreApplication.translate("SingleMeasurement", u"Characterisation:", None))
        self.value.setText(QCoreApplication.translate("SingleMeasurement", u"val", None))
        self.value_label.setText(QCoreApplication.translate("SingleMeasurement", u"Value: ", None))
        self.units.setText(QCoreApplication.translate("SingleMeasurement", u"units", None))
    # retranslateUi

