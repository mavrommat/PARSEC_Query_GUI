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
        self.Confirm_constrains_next_step = QPushButton(self.opper_gb)
        self.Confirm_constrains_next_step.setObjectName(u"Confirm_constrains_next_step")

        self.gridLayout_4.addWidget(self.Confirm_constrains_next_step, 8, 4, 1, 3)

        self.B_add_manual = QPushButton(self.opper_gb)
        self.B_add_manual.setObjectName(u"B_add_manual")

        self.gridLayout_4.addWidget(self.B_add_manual, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.opper_gb)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.menu_units = QComboBox(self.groupBox)
        self.menu_units.addItem("")
        self.menu_units.setObjectName(u"menu_units")

        self.gridLayout_6.addWidget(self.menu_units, 2, 4, 1, 1)

        self.right_constrain = QLineEdit(self.groupBox)
        self.right_constrain.setObjectName(u"right_constrain")

        self.gridLayout_6.addWidget(self.right_constrain, 2, 3, 1, 1)

        self.left_constrain = QLineEdit(self.groupBox)
        self.left_constrain.setObjectName(u"left_constrain")

        self.gridLayout_6.addWidget(self.left_constrain, 2, 1, 1, 1)

        self.relation_cb = QComboBox(self.groupBox)
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")
        self.relation_cb.addItem("")       
        self.relation_cb.setObjectName(u"relation_cb")

        self.gridLayout_6.addWidget(self.relation_cb, 2, 2, 1, 1)

        self.menu_categories_features = QToolButton(self.groupBox)
        self.menu_categories_features.setObjectName(u"menu_categories_features")

        self.gridLayout_6.addWidget(self.menu_categories_features, 2, 0, 1, 1)

        self.add_constrain = QPushButton(self.groupBox)
        self.add_constrain.setObjectName(u"add_constrain")

        self.gridLayout_6.addWidget(self.add_constrain, 3, 4, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 7, 0, 1, 1)

        self.constrains_scroll_area = QScrollArea(self.opper_gb)
        self.constrains_scroll_area.setObjectName(u"constrains_scroll_area")
        self.constrains_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 494, 919))
        self.constrains_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.constrains_scroll_area, 2, 4, 6, 3)

        self.Manual_constrain_Input = QPlainTextEdit(self.opper_gb)
        self.Manual_constrain_Input.setObjectName(u"Manual_constrain_Input")

        self.gridLayout_4.addWidget(self.Manual_constrain_Input, 1, 0, 3, 2)

        self.groupBox_2 = QGroupBox(self.opper_gb)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.B_del_group = QPushButton(self.groupBox_2)
        self.B_del_group.setObjectName(u"B_del_group")

        self.gridLayout_7.addWidget(self.B_del_group, 2, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_7.addWidget(self.comboBox_2, 2, 0, 1, 2)

        self.B_del_last_constrain = QPushButton(self.groupBox_2)
        self.B_del_last_constrain.setObjectName(u"B_del_last_constrain")

        self.gridLayout_7.addWidget(self.B_del_last_constrain, 2, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.B_or_gr = QPushButton(self.groupBox_3)
        self.B_or_gr.setObjectName(u"B_or_gr")

        self.gridLayout_8.addWidget(self.B_or_gr, 0, 2, 1, 1)

        self.B_and_gr = QPushButton(self.groupBox_3)
        self.B_and_gr.setObjectName(u"B_and_gr")

        self.gridLayout_8.addWidget(self.B_and_gr, 0, 1, 1, 1)

        self.B_not_gr = QPushButton(self.groupBox_3)
        self.B_not_gr.setObjectName(u"B_not_gr")

        self.gridLayout_8.addWidget(self.B_not_gr, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.B_add_group = QPushButton(self.groupBox_3)
        self.B_add_group.setObjectName(u"B_add_group")

        self.gridLayout_8.addWidget(self.B_add_group, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 4)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 4, 1, 3)

        self.logical_gb = QGroupBox(self.opper_gb)
        self.logical_gb.setObjectName(u"logical_gb")
        self.gridLayout_5 = QGridLayout(self.logical_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.B_NOT = QPushButton(self.logical_gb)
        self.B_NOT.setObjectName(u"B_NOT")

        self.gridLayout_5.addWidget(self.B_NOT, 0, 4, 1, 1)

        self.B_OR = QPushButton(self.logical_gb)
        self.B_OR.setObjectName(u"B_OR")

        self.gridLayout_5.addWidget(self.B_OR, 0, 3, 1, 1)

        self.B_AND = QPushButton(self.logical_gb)
        self.B_AND.setObjectName(u"B_AND")

        self.gridLayout_5.addWidget(self.B_AND, 0, 2, 1, 1)

        self.label_2 = QLabel(self.logical_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.logical_gb, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 5, 0, 1, 1)


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
        self.Confirm_constrains_next_step.setText(QCoreApplication.translate("Constraints", u"Confirm constraints: Next Step", None))
        self.B_add_manual.setText(QCoreApplication.translate("Constraints", u"Add manual contraints", None))
        self.groupBox.setTitle("")
        self.menu_units.setItemText(0, QCoreApplication.translate("Constraints", u"Independent of units", None))
        self.Manual_constrain_Input.setPlaceholderText(
    QCoreApplication.translate(
        "Constraints",
        "Enter manual constraint: e.g. { ( flux.H > 0.1 counts ) AND ( flux.V IN [0.1, 0.2] indep_units )} OR {  ( flux.U > 0.4 counts ) AND NOT ( flux.I IN [0.5, 0.7] indep_units ) }",
        None
    )
)
        self.relation_cb.setItemText(0, QCoreApplication.translate("Constraints", u">", None))
        self.relation_cb.setItemText(1, QCoreApplication.translate("Constraints", u"<", None))
        self.relation_cb.setItemText(2, QCoreApplication.translate("Constraints", u">=", None))
        self.relation_cb.setItemText(3, QCoreApplication.translate("Constraints", u"<=", None))
        self.relation_cb.setItemText(4, QCoreApplication.translate("Constraints", u"<=>", None))
        self.relation_cb.setItemText(5, QCoreApplication.translate("Constraints", u"=!", None))
        self.relation_cb.setItemText(5, QCoreApplication.translate("Constraints", u"==", None))

        self.menu_categories_features.setText(QCoreApplication.translate("Constraints", u"Categories/Features", None))
        self.add_constrain.setText(QCoreApplication.translate("Constraints", u"Add constrain", None))
        self.groupBox_2.setTitle("")
        self.B_del_group.setText(QCoreApplication.translate("Constraints", u"Delete Group", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Constraints", u"Group 1", None))

        self.B_del_last_constrain.setText(QCoreApplication.translate("Constraints", u"Delete last constraint", None))
        self.groupBox_3.setTitle("")
        self.B_or_gr.setText(QCoreApplication.translate("Constraints", u"OR", None))
        self.B_and_gr.setText(QCoreApplication.translate("Constraints", u"AND", None))
        self.B_not_gr.setText(QCoreApplication.translate("Constraints", u"NOT", None))
        self.label_3.setText(QCoreApplication.translate("Constraints", u"Logical Operation with last group:", None))
        self.B_add_group.setText(QCoreApplication.translate("Constraints", u"Add Group", None))
        self.logical_gb.setTitle("")
        self.B_NOT.setText(QCoreApplication.translate("Constraints", u"NOT", None))
        self.B_OR.setText(QCoreApplication.translate("Constraints", u"OR", None))
        self.B_AND.setText(QCoreApplication.translate("Constraints", u"AND", None))
        self.label_2.setText(QCoreApplication.translate("Constraints", u"Logical Operator:", None))
    # retranslateUi

