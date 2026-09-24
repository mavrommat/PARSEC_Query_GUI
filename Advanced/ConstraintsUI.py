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
    QVBoxLayout, QWidget)

class Ui_Constraints(object):
    def setupUi(self, Constraints):
        if not Constraints.objectName():
            Constraints.setObjectName(u"Constraints")
        Constraints.resize(1788, 1340)
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
        self.left_gb = QGroupBox(self.opper_gb)
        self.left_gb.setObjectName(u"left_gb")
        self.verticalLayout_3 = QVBoxLayout(self.left_gb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.manual_constraints_gb = QGroupBox(self.left_gb)
        self.manual_constraints_gb.setObjectName(u"manual_constraints_gb")
        self.verticalLayout = QVBoxLayout(self.manual_constraints_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Manual_constrain_Input = QPlainTextEdit(self.manual_constraints_gb)
        self.Manual_constrain_Input.setObjectName(u"Manual_constrain_Input")

        self.verticalLayout.addWidget(self.Manual_constrain_Input)

        self.B_add_manual = QPushButton(self.manual_constraints_gb)
        self.B_add_manual.setObjectName(u"B_add_manual")

        self.verticalLayout.addWidget(self.B_add_manual)


        self.verticalLayout_3.addWidget(self.manual_constraints_gb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.ui_contraint_input_gb = QGroupBox(self.left_gb)
        self.ui_contraint_input_gb.setObjectName(u"ui_contraint_input_gb")
        self.verticalLayout_2 = QVBoxLayout(self.ui_contraint_input_gb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logical_gb = QGroupBox(self.ui_contraint_input_gb)
        self.logical_gb.setObjectName(u"logical_gb")
        self.gridLayout_5 = QGridLayout(self.logical_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.B_AND_NOT = QPushButton(self.logical_gb)
        self.B_AND_NOT.setObjectName(u"B_AND_NOT")

        self.gridLayout_5.addWidget(self.B_AND_NOT, 0, 4, 1, 1)

        self.B_OR = QPushButton(self.logical_gb)
        self.B_OR.setObjectName(u"B_OR")

        self.gridLayout_5.addWidget(self.B_OR, 0, 3, 1, 1)

        self.B_AND = QPushButton(self.logical_gb)
        self.B_AND.setObjectName(u"B_AND")

        self.gridLayout_5.addWidget(self.B_AND, 0, 2, 1, 1)

        self.label_2 = QLabel(self.logical_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.logical_gb)

        self.lists_gb = QGroupBox(self.ui_contraint_input_gb)
        self.lists_gb.setObjectName(u"lists_gb")
        self.gridLayout_9 = QGridLayout(self.lists_gb)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Concepts_cb = QToolButton(self.lists_gb)
        self.Concepts_cb.setObjectName(u"Concepts_cb")

        self.gridLayout_9.addWidget(self.Concepts_cb, 1, 0, 1, 1)

        self.Auxiliary_Concept_cb = QComboBox(self.lists_gb)
        self.Auxiliary_Concept_cb.addItem("")
        self.Auxiliary_Concept_cb.addItem("")
        self.Auxiliary_Concept_cb.setObjectName(u"Auxiliary_Concept_cb")

        self.gridLayout_9.addWidget(self.Auxiliary_Concept_cb, 1, 2, 1, 1)

        self.Concept_Characterisation_cb = QComboBox(self.lists_gb)
        self.Concept_Characterisation_cb.addItem("")
        self.Concept_Characterisation_cb.setObjectName(u"Concept_Characterisation_cb")

        self.gridLayout_9.addWidget(self.Concept_Characterisation_cb, 1, 1, 1, 1)

        self.label_4 = QLabel(self.lists_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.lists_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.lists_gb)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.lists_gb)

        self.values_units_gb = QGroupBox(self.ui_contraint_input_gb)
        self.values_units_gb.setObjectName(u"values_units_gb")
        self.gridLayout_10 = QGridLayout(self.values_units_gb)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.right_constraint_val = QLineEdit(self.values_units_gb)
        self.right_constraint_val.setObjectName(u"right_constraint_val")

        self.gridLayout_10.addWidget(self.right_constraint_val, 1, 2, 1, 1)

        self.left_constraint_val = QLineEdit(self.values_units_gb)
        self.left_constraint_val.setObjectName(u"left_constraint_val")

        self.gridLayout_10.addWidget(self.left_constraint_val, 1, 0, 1, 1)

        self.Operator_symbol = QComboBox(self.values_units_gb)
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")
        self.Operator_symbol.addItem("")

        self.Operator_symbol.setObjectName(u"Operator_symbol")

        self.gridLayout_10.addWidget(self.Operator_symbol, 1, 1, 1, 1)

        self.menu_units = QComboBox(self.values_units_gb)
        self.menu_units.addItem("")
        self.menu_units.setObjectName(u"menu_units")

        self.gridLayout_10.addWidget(self.menu_units, 1, 3, 1, 1)

        self.add_constraint = QPushButton(self.values_units_gb)
        self.add_constraint.setObjectName(u"add_constraint")

        self.gridLayout_10.addWidget(self.add_constraint, 2, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.values_units_gb)


        self.verticalLayout_3.addWidget(self.ui_contraint_input_gb)


        self.gridLayout_4.addWidget(self.left_gb, 1, 0, 8, 1)

        self.right_gb = QGroupBox(self.opper_gb)
        self.right_gb.setObjectName(u"right_gb")
        self.verticalLayout_4 = QVBoxLayout(self.right_gb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.right_gb)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.B_del_gr = QPushButton(self.groupBox_2)
        self.B_del_gr.setObjectName(u"B_del_gr")

        self.gridLayout_7.addWidget(self.B_del_gr, 2, 2, 1, 1)

        self.Group_cb = QComboBox(self.groupBox_2)
        self.Group_cb.addItem("")
        self.Group_cb.setObjectName(u"Group_cb")

        self.gridLayout_7.addWidget(self.Group_cb, 2, 0, 1, 2)

        self.horizontalSpacer_del_constraint = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_del_constraint, 2, 3, 1, 1)

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

        self.B_add_gr = QPushButton(self.groupBox_3)
        self.B_add_gr.setObjectName(u"B_add_gr")

        self.gridLayout_8.addWidget(self.B_add_gr, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 4)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.constrains_scroll_area = QScrollArea(self.right_gb)
        self.constrains_scroll_area.setObjectName(u"constrains_scroll_area")
        self.constrains_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 812, 920))
        self.constrains_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.constrains_scroll_area)

        self.B_copy_constraints = QPushButton(self.right_gb)
        self.B_copy_constraints.setObjectName(u"B_copy_constraints")

        self.verticalLayout_4.addWidget(self.B_copy_constraints)

        self.Confirm_constraints_next_step = QPushButton(self.right_gb)
        self.Confirm_constraints_next_step.setObjectName(u"Confirm_constraints_next_step")

        self.verticalLayout_4.addWidget(self.Confirm_constraints_next_step)


        self.gridLayout_4.addWidget(self.right_gb, 1, 2, 8, 1)


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
        self.left_gb.setTitle("")
        self.manual_constraints_gb.setTitle("")
        self.B_add_manual.setText(QCoreApplication.translate("Constraints", u"Add manual constraints", None))
        self.ui_contraint_input_gb.setTitle("")
        self.logical_gb.setTitle("")
        self.B_AND_NOT.setText(QCoreApplication.translate("Constraints", u"AND NOT", None))
        self.B_OR.setText(QCoreApplication.translate("Constraints", u"OR", None))
        self.B_AND.setText(QCoreApplication.translate("Constraints", u"AND", None))
        self.label_2.setText(QCoreApplication.translate("Constraints", u"Logical Operator:", None))
        self.lists_gb.setTitle("")
        self.Concepts_cb.setText(QCoreApplication.translate("Constraints", u"Categories/Features", None))
        self.Auxiliary_Concept_cb.setItemText(0, QCoreApplication.translate("Constraints", u"None", None))
        self.Auxiliary_Concept_cb.setItemText(1, QCoreApplication.translate("Constraints", u"Any", None))

        self.Concept_Characterisation_cb.setItemText(0, QCoreApplication.translate("Constraints", u"Unspecified", None))

        self.label_4.setText(QCoreApplication.translate("Constraints", u"Define the Concept:", None))
        self.label_5.setText(QCoreApplication.translate("Constraints", u"Define the Characterisation of the Concept:", None))
        self.label_6.setText(QCoreApplication.translate("Constraints", u"Define if Auxiliary:", None))
        self.values_units_gb.setTitle("")
        self.Operator_symbol.setItemText(0, QCoreApplication.translate("Constraints", u">", None))
        self.Operator_symbol.setItemText(1, QCoreApplication.translate("Constraints", u"<", None))
        self.Operator_symbol.setItemText(2, QCoreApplication.translate("Constraints", u">=", None))
        self.Operator_symbol.setItemText(3, QCoreApplication.translate("Constraints", u"<=", None))
        self.Operator_symbol.setItemText(4, QCoreApplication.translate("Constraints", u"<=>", None))
        self.Operator_symbol.setItemText(5, QCoreApplication.translate("Constraints", u"=!", None))
        self.Operator_symbol.setItemText(6, QCoreApplication.translate("Constraints", u"==", None))
        self.Operator_symbol.setItemText(7, QCoreApplication.translate("Constraints", u"str", None))

        self.menu_units.setItemText(0, QCoreApplication.translate("Constraints", u"Independent of units", None))

        self.add_constraint.setText(QCoreApplication.translate("Constraints", u"Add constraint", None))
        self.right_gb.setTitle("")
        self.groupBox_2.setTitle("")
        self.B_del_gr.setText(QCoreApplication.translate("Constraints", u"Delete Group", None))
        self.Group_cb.setItemText(0, QCoreApplication.translate("Constraints", u"Group 1", None))

        self.groupBox_3.setTitle("")
        self.B_or_gr.setText(QCoreApplication.translate("Constraints", u"OR", None))
        self.B_and_gr.setText(QCoreApplication.translate("Constraints", u"AND", None))
        self.B_not_gr.setText(QCoreApplication.translate("Constraints", u"AND NOT", None))
        self.label_3.setText(QCoreApplication.translate("Constraints", u"Logical Operation with last group:", None))
        self.B_add_gr.setText(QCoreApplication.translate("Constraints", u"Add Group", None))
        self.B_copy_constraints.setText(QCoreApplication.translate("Constraints", u"Copy Constraints to Clipboard", None))
        self.Confirm_constraints_next_step.setText(QCoreApplication.translate("Constraints", u"Confirm constraints: Next Step", None))
    # retranslateUi

