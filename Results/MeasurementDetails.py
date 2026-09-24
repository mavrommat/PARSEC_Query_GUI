# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeasurementDetails.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_MeasurementDetails(object):
    def setupUi(self, MeasurementDetails):
        if not MeasurementDetails.objectName():
            MeasurementDetails.setObjectName(u"MeasurementDetails")
        MeasurementDetails.resize(1122, 802)
        self.gridLayout = QGridLayout(MeasurementDetails)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(MeasurementDetails)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.main_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.main_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.table_name = QLabel(self.main_gb)
        self.table_name.setObjectName(u"table_name")
        self.table_name.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.table_name, 5, 1, 1, 1)

        self.raw_value = QLabel(self.main_gb)
        self.raw_value.setObjectName(u"raw_value")
        self.raw_value.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.raw_value, 0, 1, 1, 1)

        self.label = QLabel(self.main_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)

        self.raw_units = QLabel(self.main_gb)
        self.raw_units.setObjectName(u"raw_units")
        self.raw_units.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.raw_units, 2, 1, 1, 1)

        self.raw_value_label = QLabel(self.main_gb)
        self.raw_value_label.setObjectName(u"raw_value_label")

        self.gridLayout_2.addWidget(self.raw_value_label, 0, 0, 1, 1)

        self.col_name = QLabel(self.main_gb)
        self.col_name.setObjectName(u"col_name")
        self.col_name.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.col_name, 4, 1, 1, 1)

        self.label_3 = QLabel(self.main_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.col_descr = QLabel(self.main_gb)
        self.col_descr.setObjectName(u"col_descr")
        self.col_descr.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.col_descr, 6, 1, 1, 1)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.B_close_details = QPushButton(MeasurementDetails)
        self.B_close_details.setObjectName(u"B_close_details")

        self.gridLayout.addWidget(self.B_close_details, 1, 1, 1, 1)


        self.retranslateUi(MeasurementDetails)

        QMetaObject.connectSlotsByName(MeasurementDetails)
    # setupUi

    def retranslateUi(self, MeasurementDetails):
        MeasurementDetails.setWindowTitle(QCoreApplication.translate("MeasurementDetails", u"Form", None))
        self.main_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MeasurementDetails", u"Raw Units:", None))
        self.label_4.setText(QCoreApplication.translate("MeasurementDetails", u"Column Name:", None))
        self.table_name.setText(QCoreApplication.translate("MeasurementDetails", u"table_name", None))
        self.raw_value.setText(QCoreApplication.translate("MeasurementDetails", u"raw_val", None))
        self.label.setText(QCoreApplication.translate("MeasurementDetails", u"Table:", None))
        self.raw_units.setText(QCoreApplication.translate("MeasurementDetails", u"raw_units", None))
        self.raw_value_label.setText(QCoreApplication.translate("MeasurementDetails", u"Raw Value:", None))
        self.col_name.setText(QCoreApplication.translate("MeasurementDetails", u"col_name", None))
        self.label_3.setText(QCoreApplication.translate("MeasurementDetails", u"Column Description:", None))
        self.col_descr.setText(QCoreApplication.translate("MeasurementDetails", u"Col_discr", None))
        self.B_close_details.setText(QCoreApplication.translate("MeasurementDetails", u"Close Details", None))
    # retranslateUi

