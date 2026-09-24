# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConstraintsMetadataUI.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Constraint_metadata(object):
    def setupUi(self, Constraint_metadata):
        if not Constraint_metadata.objectName():
            Constraint_metadata.setObjectName(u"Constraint_metadata")
        Constraint_metadata.resize(934, 860)
        self.gridLayout = QGridLayout(Constraint_metadata)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(Constraint_metadata)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.constraints_cb = QComboBox(self.main_gb)
        self.constraints_cb.setObjectName(u"constraints_cb")

        self.gridLayout_2.addWidget(self.constraints_cb, 0, 0, 1, 1)

        self.B_del_constraint = QPushButton(self.main_gb)
        self.B_del_constraint.setObjectName(u"B_del_constraint")

        self.gridLayout_2.addWidget(self.B_del_constraint, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.metadata_gb = QGroupBox(self.main_gb)
        self.metadata_gb.setObjectName(u"metadata_gb")
        self.gridLayout_3 = QGridLayout(self.metadata_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.metadata_gb)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_op_next_group = QLabel(self.metadata_gb)
        self.label_op_next_group.setObjectName(u"label_op_next_group")

        self.gridLayout_3.addWidget(self.label_op_next_group, 1, 1, 1, 1)

        self.label_7 = QLabel(self.metadata_gb)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_op_next_constraint = QLabel(self.metadata_gb)
        self.label_op_next_constraint.setObjectName(u"label_op_next_constraint")

        self.gridLayout_3.addWidget(self.label_op_next_constraint, 3, 1, 1, 1)

        self.label_feature = QLabel(self.metadata_gb)
        self.label_feature.setObjectName(u"label_feature")

        self.gridLayout_3.addWidget(self.label_feature, 5, 1, 1, 1)

        self.label_operator = QLabel(self.metadata_gb)
        self.label_operator.setObjectName(u"label_operator")

        self.gridLayout_3.addWidget(self.label_operator, 8, 1, 1, 1)

        self.label_category = QLabel(self.metadata_gb)
        self.label_category.setObjectName(u"label_category")

        self.gridLayout_3.addWidget(self.label_category, 4, 1, 1, 1)

        self.label_6 = QLabel(self.metadata_gb)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_9 = QLabel(self.metadata_gb)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 8, 0, 1, 1)

        self.label_10 = QLabel(self.metadata_gb)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_op_prev_constraint = QLabel(self.metadata_gb)
        self.label_op_prev_constraint.setObjectName(u"label_op_prev_constraint")

        self.gridLayout_3.addWidget(self.label_op_prev_constraint, 2, 1, 1, 1)

        self.label_constraint_val = QLabel(self.metadata_gb)
        self.label_constraint_val.setObjectName(u"label_constraint_val")

        self.gridLayout_3.addWidget(self.label_constraint_val, 9, 1, 1, 1)

        self.label_2 = QLabel(self.metadata_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_op_prev_group = QLabel(self.metadata_gb)
        self.label_op_prev_group.setObjectName(u"label_op_prev_group")

        self.gridLayout_3.addWidget(self.label_op_prev_group, 0, 1, 1, 1)

        self.label_4 = QLabel(self.metadata_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(self.metadata_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.metadata_gb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_characterisation = QLabel(self.metadata_gb)
        self.label_characterisation.setObjectName(u"label_characterisation")

        self.gridLayout_3.addWidget(self.label_characterisation, 6, 1, 1, 1)

        self.label_3 = QLabel(self.metadata_gb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_auxilary = QLabel(self.metadata_gb)
        self.label_auxilary.setObjectName(u"label_auxilary")

        self.gridLayout_3.addWidget(self.label_auxilary, 7, 1, 1, 1)

        self.label_11 = QLabel(self.metadata_gb)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 10, 0, 1, 1)

        self.label_unit = QLabel(self.metadata_gb)
        self.label_unit.setObjectName(u"label_unit")

        self.gridLayout_3.addWidget(self.label_unit, 10, 1, 1, 1)


        self.gridLayout_2.addWidget(self.metadata_gb, 1, 0, 1, 3)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(Constraint_metadata)

        QMetaObject.connectSlotsByName(Constraint_metadata)
    # setupUi

    def retranslateUi(self, Constraint_metadata):
        Constraint_metadata.setWindowTitle(QCoreApplication.translate("Constraint_metadata", u"Form", None))
        self.main_gb.setTitle("")
        self.B_del_constraint.setText(QCoreApplication.translate("Constraint_metadata", u"Delete Constraint", None))
        self.metadata_gb.setTitle("")
        self.label_8.setText(QCoreApplication.translate("Constraint_metadata", u"Auxilary:", None))
        self.label_op_next_group.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("Constraint_metadata", u"Characterisation:", None))
        self.label_op_next_constraint.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_feature.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_operator.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_category.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("Constraint_metadata", u"Feature:", None))
        self.label_9.setText(QCoreApplication.translate("Constraint_metadata", u"Comparison Operator:", None))
        self.label_10.setText(QCoreApplication.translate("Constraint_metadata", u"Constraint Value/s:", None))
        self.label_op_prev_constraint.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_constraint_val.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_2.setText(QCoreApplication.translate("Constraint_metadata", u"Next Group Operator:", None))
        self.label_op_prev_group.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_4.setText(QCoreApplication.translate("Constraint_metadata", u"Next Constraint Operator:", None))
        self.label.setText(QCoreApplication.translate("Constraint_metadata", u"Previous Group Operator:", None))
        self.label_5.setText(QCoreApplication.translate("Constraint_metadata", u"Category:", None))
        self.label_characterisation.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_3.setText(QCoreApplication.translate("Constraint_metadata", u"Previous Constraint Operator:", None))
        self.label_auxilary.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("Constraint_metadata", u"Units:", None))
        self.label_unit.setText(QCoreApplication.translate("Constraint_metadata", u"N/A", None))
    # retranslateUi

