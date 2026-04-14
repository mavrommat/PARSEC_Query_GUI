# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Constraints.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_Constraints(object):
    def setupUi(self, Constraints):
        if not Constraints.objectName():
            Constraints.setObjectName(u"Constraints")
        Constraints.resize(1788, 1287)
        self.gridLayout = QGridLayout(Constraints)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(Constraints)
        self.main_gb.setObjectName(u"main_gb")
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        self.main_gb.setFont(font)
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title_gb = QGroupBox(self.main_gb)
        self.title_gb.setObjectName(u"title_gb")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.title_gb.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.title_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.title_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.title_gb, 0, 0, 1, 1)

        self.opper_gb = QGroupBox(self.main_gb)
        self.opper_gb.setObjectName(u"opper_gb")
        self.gridLayout_4 = QGridLayout(self.opper_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 9, 1)

        self.menu_categories_features = QToolButton(self.opper_gb)
        self.menu_categories_features.setObjectName(u"menu_categories_features")

        self.gridLayout_4.addWidget(self.menu_categories_features, 5, 0, 1, 1)

        self.delete_last_constrain = QPushButton(self.opper_gb)
        self.delete_last_constrain.setObjectName(u"delete_last_constrain")

        self.gridLayout_4.addWidget(self.delete_last_constrain, 1, 7, 1, 1)

        self.logical_gb = QGroupBox(self.opper_gb)
        self.logical_gb.setObjectName(u"logical_gb")
        self.gridLayout_5 = QGridLayout(self.logical_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.B_AND = QPushButton(self.logical_gb)
        self.B_AND.setObjectName(u"B_AND")

        self.gridLayout_5.addWidget(self.B_AND, 1, 2, 1, 1)

        self.B_OR = QPushButton(self.logical_gb)
        self.B_OR.setObjectName(u"B_OR")

        self.gridLayout_5.addWidget(self.B_OR, 1, 3, 1, 1)

        self.label_2 = QLabel(self.logical_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 1, 1, 1)

        self.B_NOT = QPushButton(self.logical_gb)
        self.B_NOT.setObjectName(u"B_NOT")

        self.gridLayout_5.addWidget(self.B_NOT, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.logical_gb, 6, 0, 1, 2)

        self.Manual_constrain_Input = QPlainTextEdit(self.opper_gb)
        self.Manual_constrain_Input.setObjectName(u"Manual_constrain_Input")

        self.gridLayout_4.addWidget(self.Manual_constrain_Input, 1, 0, 4, 2)

        self.groupBox = QGroupBox(self.opper_gb)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 2, 5, 1, 1)

        self.right_constrain = QLineEdit(self.groupBox)
        self.right_constrain.setObjectName(u"right_constrain")

        self.gridLayout_6.addWidget(self.right_constrain, 2, 3, 1, 1)

        self.relation_cb = QComboBox(self.groupBox)
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.setObjectName(u"relation_cb")

        self.gridLayout_6.addWidget(self.relation_cb, 2, 2, 1, 1)

        self.left_constrain = QLineEdit(self.groupBox)
        self.left_constrain.setObjectName(u"left_constrain")

        self.gridLayout_6.addWidget(self.left_constrain, 2, 1, 1, 1)

        self.menu_units = QComboBox(self.groupBox)
        self.menu_units.setObjectName(u"menu_units")

        self.gridLayout_6.addWidget(self.menu_units, 2, 4, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 7, 0, 1, 2)

        self.constrains_scroll_area = QScrollArea(self.opper_gb)
        self.constrains_scroll_area.setObjectName(u"constrains_scroll_area")
        self.constrains_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 644, 1033))
        self.constrains_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.constrains_scroll_area, 2, 5, 6, 3)

        self.add_constrain = QPushButton(self.opper_gb)
        self.add_constrain.setObjectName(u"add_constrain")

        self.gridLayout_4.addWidget(self.add_constrain, 8, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 8, 0, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 6, 1, 1)

        self.Confirm_constrains_next_step = QPushButton(self.opper_gb)
        self.Confirm_constrains_next_step.setObjectName(u"Confirm_constrains_next_step")

        self.gridLayout_4.addWidget(self.Confirm_constrains_next_step, 9, 6, 1, 2)


        self.gridLayout_2.addWidget(self.opper_gb, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(1, 1)

        self.gridLayout.addWidget(self.main_gb, 1, 0, 1, 1)


        self.retranslateUi(Constraints)

        QMetaObject.connectSlotsByName(Constraints)
    # setupUi

    def retranslateUi(self, Constraints):
        Constraints.setWindowTitle(QCoreApplication.translate("Constraints", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("Constraints", u"Set Constraints", None))
        self.opper_gb.setTitle("")
        self.Manual_constrain_Input.setPlaceholderText("Enter manual your constraints in this format: (flux.K_4 <=> [0.1, 0.5] counts) AND (temperature.T_eff > 5000 K) Note: By pressing the Add Constrain/s button while having text in manual input will bypass the button options and add the manual constrain directly to the scroll widget)")
        self.menu_categories_features.setText(QCoreApplication.translate("Constraints", u"Categories/Features", None))
        self.delete_last_constrain.setText(QCoreApplication.translate("Constraints", u"Delete last constraint", None))
        self.logical_gb.setTitle("")
        self.B_AND.setText(QCoreApplication.translate("Constraints", u"AND", None))
        self.B_OR.setText(QCoreApplication.translate("Constraints", u"OR", None))
        self.label_2.setText(QCoreApplication.translate("Constraints", u"Logical Operator:", None))
        self.B_NOT.setText(QCoreApplication.translate("Constraints", u"NOT", None))
        self.groupBox.setTitle("")
        self.relation_cb.setItemText(0, QCoreApplication.translate("Constraints", u">", None))
        self.relation_cb.setItemText(1, QCoreApplication.translate("Constraints", u"<", None))
        self.relation_cb.setItemText(2, QCoreApplication.translate("Constraints", u">=", None))
        self.relation_cb.setItemText(3, QCoreApplication.translate("Constraints", u"<=", None))
        self.relation_cb.setItemText(4, QCoreApplication.translate("Constraints", u"<=>", None))
        self.relation_cb.setItemText(5, QCoreApplication.translate("Constraints", u"=!", None))

        self.add_constrain.setText(QCoreApplication.translate("Constraints", u"Add Constraint/s", None))
        self.Confirm_constrains_next_step.setText(QCoreApplication.translate("Constraints", u"Confirm Constraints: Next Step", None))
    # retranslateUi

