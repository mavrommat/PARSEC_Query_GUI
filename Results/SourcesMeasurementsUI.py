# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SourcesMeasurementsUI.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_ConceptMeasurements(object):
    def setupUi(self, ConceptMeasurements):
        if not ConceptMeasurements.objectName():
            ConceptMeasurements.setObjectName(u"ConceptMeasurements")
        ConceptMeasurements.resize(825, 657)
        self.gridLayout = QGridLayout(ConceptMeasurements)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.main_gb = QGroupBox(ConceptMeasurements)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.catalogs_scroll_area = QScrollArea(self.main_gb)
        self.catalogs_scroll_area.setObjectName(u"catalogs_scroll_area")
        self.catalogs_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 479))
        self.catalogs_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.catalogs_scroll_area, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_gb, 2, 0, 1, 2)

        self.B_back = QPushButton(ConceptMeasurements)
        self.B_back.setObjectName(u"B_back")

        self.gridLayout.addWidget(self.B_back, 0, 0, 1, 1)

        self.caterory_concept_gb = QGroupBox(ConceptMeasurements)
        self.caterory_concept_gb.setObjectName(u"caterory_concept_gb")
        self.gridLayout_3 = QGridLayout(self.caterory_concept_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.category_label = QLabel(self.caterory_concept_gb)
        self.category_label.setObjectName(u"category_label")

        self.gridLayout_3.addWidget(self.category_label, 0, 0, 1, 1)

        self.concept_label = QLabel(self.caterory_concept_gb)
        self.concept_label.setObjectName(u"concept_label")

        self.gridLayout_3.addWidget(self.concept_label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.caterory_concept_gb, 1, 0, 1, 2)


        self.retranslateUi(ConceptMeasurements)

        QMetaObject.connectSlotsByName(ConceptMeasurements)
    # setupUi

    def retranslateUi(self, ConceptMeasurements):
        ConceptMeasurements.setWindowTitle(QCoreApplication.translate("ConceptMeasurements", u"Form", None))
        self.main_gb.setTitle("")
        self.B_back.setText(QCoreApplication.translate("ConceptMeasurements", u"Back to overview", None))
        self.caterory_concept_gb.setTitle("")
        self.category_label.setText(QCoreApplication.translate("ConceptMeasurements", u"Category:", None))
        self.concept_label.setText(QCoreApplication.translate("ConceptMeasurements", u"Concept:", None))
    # retranslateUi

