# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestionCoordinatesUI.UI'
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

class Ui_QuestionCoordinates(object):
    def setupUi(self, QuestionCoordinates):
        if not QuestionCoordinates.objectName():
            QuestionCoordinates.setObjectName(u"QuestionCoordinates")
        QuestionCoordinates.resize(731, 540)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        QuestionCoordinates.setFont(font)
        self.gridLayout = QGridLayout(QuestionCoordinates)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(QuestionCoordinates)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.answer_gb = QGroupBox(self.main_gb)
        self.answer_gb.setObjectName(u"answer_gb")
        self.gridLayout_4 = QGridLayout(self.answer_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.B_yes = QPushButton(self.answer_gb)
        self.B_yes.setObjectName(u"B_yes")

        self.gridLayout_4.addWidget(self.B_yes, 1, 1, 1, 1)

        self.B_no = QPushButton(self.answer_gb)
        self.B_no.setObjectName(u"B_no")

        self.gridLayout_4.addWidget(self.B_no, 1, 2, 1, 1)

        self.label = QLabel(self.answer_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)

        self.gridLayout_2.addWidget(self.answer_gb, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(QuestionCoordinates)

        QMetaObject.connectSlotsByName(QuestionCoordinates)
    # setupUi

    def retranslateUi(self, QuestionCoordinates):
        QuestionCoordinates.setWindowTitle(QCoreApplication.translate("QuestionCoordinates", u"Form", None))
        self.main_gb.setTitle("")
        self.answer_gb.setTitle("")
        self.B_yes.setText(QCoreApplication.translate("QuestionCoordinates", u"Yes", None))
        self.B_no.setText(QCoreApplication.translate("QuestionCoordinates", u"No", None))
        self.label.setText(QCoreApplication.translate("QuestionCoordinates", u"Do you need to query by coordinates too?", None))
    # retranslateUi

