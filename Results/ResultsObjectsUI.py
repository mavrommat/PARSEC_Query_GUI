# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultsObjectsUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QScrollArea,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Results_Objects(object):
    def setupUi(self, Results_Objects):
        if not Results_Objects.objectName():
            Results_Objects.setObjectName(u"Results_Objects")
        Results_Objects.resize(931, 757)
        self.gridLayout_2 = QGridLayout(Results_Objects)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_gb = QGroupBox(Results_Objects)
        self.main_gb.setObjectName(u"main_gb")
        self.verticalLayout = QVBoxLayout(self.main_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbar_results = QToolButton(self.main_gb)
        self.toolbar_results.setObjectName(u"toolbar_results")

        self.verticalLayout.addWidget(self.toolbar_results)

        self.object_stack = QScrollArea(self.main_gb)
        self.object_stack.setObjectName(u"object_stack")
        self.object_stack.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 875, 669))
        self.object_stack.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.object_stack)


        self.gridLayout_2.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(Results_Objects)

        QMetaObject.connectSlotsByName(Results_Objects)
    # setupUi

    def retranslateUi(self, Results_Objects):
        Results_Objects.setWindowTitle(QCoreApplication.translate("Results_Objects", u"Form", None))
        self.main_gb.setTitle("")
        self.toolbar_results.setText(QCoreApplication.translate("Results_Objects", u"...", None))
    # retranslateUi

