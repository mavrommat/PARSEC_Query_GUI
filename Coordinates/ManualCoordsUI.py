# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualCoordsUI.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ManualCoords(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(869, 671)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_gb = QGroupBox(Form)
        self.main_gb.setObjectName(u"main_gb")
        self.gridLayout_2 = QGridLayout(self.main_gb)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title_gb = QGroupBox(self.main_gb)
        self.title_gb.setObjectName(u"title_gb")
        self.horizontalLayout = QHBoxLayout(self.title_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.title_gb)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.title_gb, 0, 0, 1, 1)

        self.coords_gb = QGroupBox(self.main_gb)
        self.coords_gb.setObjectName(u"coords_gb")
        self.gridLayout_3 = QGridLayout(self.coords_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.B_add_vertex = QPushButton(self.coords_gb)
        self.B_add_vertex.setObjectName(u"B_add_vertex")

        self.gridLayout_3.addWidget(self.B_add_vertex, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.B_del_vertex = QPushButton(self.coords_gb)
        self.B_del_vertex.setObjectName(u"B_del_vertex")

        self.gridLayout_3.addWidget(self.B_del_vertex, 0, 2, 1, 1)

        self.Coordinates_Table = QTableWidget(self.coords_gb)
        if (self.Coordinates_Table.columnCount() < 4):
            self.Coordinates_Table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Coordinates_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Coordinates_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Coordinates_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Coordinates_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.Coordinates_Table.rowCount() < 3):
            self.Coordinates_Table.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Coordinates_Table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Coordinates_Table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Coordinates_Table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Coordinates_Table.setItem(2, 2, __qtablewidgetitem7)
        self.Coordinates_Table.setObjectName(u"Coordinates_Table")

        self.gridLayout_3.addWidget(self.Coordinates_Table, 1, 0, 1, 3)


        self.gridLayout_2.addWidget(self.coords_gb, 2, 0, 1, 1)

        self.frame_units_gb = QGroupBox(self.main_gb)
        self.frame_units_gb.setObjectName(u"frame_units_gb")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_units_gb)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_units_gb)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.frame_cb = QComboBox(self.frame_units_gb)
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.setObjectName(u"frame_cb")

        self.horizontalLayout_2.addWidget(self.frame_cb)

        self.label_3 = QLabel(self.frame_units_gb)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.units_cb = QComboBox(self.frame_units_gb)
        self.units_cb.addItem("")
        self.units_cb.addItem("")
        self.units_cb.addItem("")
        self.units_cb.setObjectName(u"units_cb")

        self.horizontalLayout_2.addWidget(self.units_cb)


        self.gridLayout_2.addWidget(self.frame_units_gb, 1, 0, 1, 1)

        self.select_gb = QGroupBox(self.main_gb)
        self.select_gb.setObjectName(u"select_gb")
        self.gridLayout_4 = QGridLayout(self.select_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.B_submit_shape = QPushButton(self.select_gb)
        self.B_submit_shape.setObjectName(u"B_submit_shape")

        self.gridLayout_4.addWidget(self.B_submit_shape, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.select_gb, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.main_gb, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_gb.setTitle("")
        self.title_gb.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"Define Search Area: Manual Coordinates", None))
        self.coords_gb.setTitle("")
        self.B_add_vertex.setText(QCoreApplication.translate("Form", u"Add Vertex", None))
        self.B_del_vertex.setText(QCoreApplication.translate("Form", u"Delete Vertex", None))
        ___qtablewidgetitem = self.Coordinates_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"RA", None));
        ___qtablewidgetitem1 = self.Coordinates_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DEC", None));
        ___qtablewidgetitem2 = self.Coordinates_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Active/Deactive (1/0)", None));
        ___qtablewidgetitem3 = self.Coordinates_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Order:(1,2...n)", None));
        ___qtablewidgetitem4 = self.Coordinates_Table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Coordinates #1", None));
        ___qtablewidgetitem5 = self.Coordinates_Table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Coordinates #2", None));
        ___qtablewidgetitem6 = self.Coordinates_Table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Coordinates #3", None));

        __sortingEnabled = self.Coordinates_Table.isSortingEnabled()
        self.Coordinates_Table.setSortingEnabled(False)
        self.Coordinates_Table.setSortingEnabled(__sortingEnabled)

        self.frame_units_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Select Frame:", None))
        self.frame_cb.setItemText(0, QCoreApplication.translate("Form", u"ICRS", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("Form", u"FK5", None))
        self.frame_cb.setItemText(2, QCoreApplication.translate("Form", u"FK4", None))
        self.frame_cb.setItemText(3, QCoreApplication.translate("Form", u"Galactic", None))
        self.frame_cb.setItemText(4, QCoreApplication.translate("Form", u"Barycentric True Ecliptic\n"
"", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"Select Units:", None))
        self.units_cb.setItemText(0, QCoreApplication.translate("Form", u"Degrees", None))
        self.units_cb.setItemText(1, QCoreApplication.translate("Form", u"Arcseconds", None))
        self.units_cb.setItemText(2, QCoreApplication.translate("Form", u"Arcminutes", None))

        self.select_gb.setTitle("")
        self.B_submit_shape.setText(QCoreApplication.translate("Form", u"Submit Shape", None))
    # retranslateUi

