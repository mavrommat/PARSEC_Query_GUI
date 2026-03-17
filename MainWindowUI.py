# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 803)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        MainWindow.setFont(font)
        self.actionCSV = QAction(MainWindow)
        self.actionCSV.setObjectName(u"actionCSV")
        self.actionCopy_Table = QAction(MainWindow)
        self.actionCopy_Table.setObjectName(u"actionCopy_Table")
        self.actionCreate_Plot = QAction(MainWindow)
        self.actionCreate_Plot.setObjectName(u"actionCreate_Plot")
        self.actionGraph_Interface = QAction(MainWindow)
        self.actionGraph_Interface.setObjectName(u"actionGraph_Interface")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_gb = QGroupBox(self.centralwidget)
        self.main_gb.setObjectName(u"main_gb")
        self.horizontalLayout = QHBoxLayout(self.main_gb)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.db_query_selection_widget_gb = QGroupBox(self.main_gb)
        self.db_query_selection_widget_gb.setObjectName(u"db_query_selection_widget_gb")
        self.verticalLayout = QVBoxLayout(self.db_query_selection_widget_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcome_db_query_gb = QGroupBox(self.db_query_selection_widget_gb)
        self.welcome_db_query_gb.setObjectName(u"welcome_db_query_gb")
        self.gridLayout = QGridLayout(self.welcome_db_query_gb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.databases_gb = QGroupBox(self.welcome_db_query_gb)
        self.databases_gb.setObjectName(u"databases_gb")
        self.horizontalLayout_2 = QHBoxLayout(self.databases_gb)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.databases_gb)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.B_database_1 = QPushButton(self.databases_gb)
        self.B_database_1.setObjectName(u"B_database_1")
        self.B_database_1.setFont(font1)

        self.horizontalLayout_2.addWidget(self.B_database_1)

        self.B_database_2 = QPushButton(self.databases_gb)
        self.B_database_2.setObjectName(u"B_database_2")
        self.B_database_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.B_database_2)


        self.gridLayout.addWidget(self.databases_gb, 1, 0, 1, 1)

        self.search_by_gb = QGroupBox(self.welcome_db_query_gb)
        self.search_by_gb.setObjectName(u"search_by_gb")
        self.search_by_gb.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.search_by_gb)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_3 = QLabel(self.search_by_gb)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.B_objectid_search = QPushButton(self.search_by_gb)
        self.B_objectid_search.setObjectName(u"B_objectid_search")
        self.B_objectid_search.setFont(font1)

        self.horizontalLayout_3.addWidget(self.B_objectid_search)

        self.B_coordinates_search = QPushButton(self.search_by_gb)
        self.B_coordinates_search.setObjectName(u"B_coordinates_search")
        self.B_coordinates_search.setFont(font1)

        self.horizontalLayout_3.addWidget(self.B_coordinates_search)

        self.B_paper_authors_search = QPushButton(self.search_by_gb)
        self.B_paper_authors_search.setObjectName(u"B_paper_authors_search")
        self.B_paper_authors_search.setFont(font1)

        self.horizontalLayout_3.addWidget(self.B_paper_authors_search)

        self.B_advanced_search = QPushButton(self.search_by_gb)
        self.B_advanced_search.setObjectName(u"B_advanced_search")
        self.B_advanced_search.setFont(font1)

        self.horizontalLayout_3.addWidget(self.B_advanced_search)


        self.gridLayout.addWidget(self.search_by_gb, 2, 0, 1, 1)

        self.label = QLabel(self.welcome_db_query_gb)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro"])
        font2.setPointSize(18)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.welcome_db_query_gb)

        self.main_query_gb = QGroupBox(self.db_query_selection_widget_gb)
        self.main_query_gb.setObjectName(u"main_query_gb")
        self.gridLayout_3 = QGridLayout(self.main_query_gb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.query_widget = QWidget(self.main_query_gb)
        self.query_widget.setObjectName(u"query_widget")

        self.gridLayout_3.addWidget(self.query_widget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_query_gb)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.horizontalLayout.addWidget(self.db_query_selection_widget_gb)

        self.output_gb = QGroupBox(self.main_gb)
        self.output_gb.setObjectName(u"output_gb")
        self.gridLayout_4 = QGridLayout(self.output_gb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.output_widget = QWidget(self.output_gb)
        self.output_widget.setObjectName(u"output_widget")

        self.gridLayout_4.addWidget(self.output_widget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.output_gb)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout_2.addWidget(self.main_gb, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1232, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave_File = QMenu(self.menuFile)
        self.menuSave_File.setObjectName(u"menuSave_File")
        self.menuToolkit = QMenu(self.menubar)
        self.menuToolkit.setObjectName(u"menuToolkit")
        self.menuVisualise = QMenu(self.menubar)
        self.menuVisualise.setObjectName(u"menuVisualise")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuToolkit.menuAction())
        self.menubar.addAction(self.menuVisualise.menuAction())
        self.menuFile.addAction(self.menuSave_File.menuAction())
        self.menuFile.addAction(self.actionCopy_Table)
        self.menuSave_File.addAction(self.actionCSV)
        self.menuVisualise.addAction(self.actionCreate_Plot)
        self.menuVisualise.addAction(self.actionGraph_Interface)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCSV.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.actionCopy_Table.setText(QCoreApplication.translate("MainWindow", u"Copy Table", None))
        self.actionCreate_Plot.setText(QCoreApplication.translate("MainWindow", u"Create Plot", None))
        self.actionGraph_Interface.setText(QCoreApplication.translate("MainWindow", u"Graph Interface", None))
        self.main_gb.setTitle("")
        self.db_query_selection_widget_gb.setTitle("")
        self.welcome_db_query_gb.setTitle("")
        self.databases_gb.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select your databases:", None))
        self.B_database_1.setText(QCoreApplication.translate("MainWindow", u"HECATE", None))
        self.B_database_2.setText(QCoreApplication.translate("MainWindow", u"HyperAtlas", None))
        self.search_by_gb.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search by:", None))
        self.B_objectid_search.setText(QCoreApplication.translate("MainWindow", u"Object ID", None))
        self.B_coordinates_search.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.B_paper_authors_search.setText(QCoreApplication.translate("MainWindow", u"Paper/Authors", None))
        self.B_advanced_search.setText(QCoreApplication.translate("MainWindow", u"Advanced Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to PARSEC!", None))
        self.main_query_gb.setTitle("")
        self.output_gb.setTitle("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave_File.setTitle(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.menuToolkit.setTitle(QCoreApplication.translate("MainWindow", u"Toolkit", None))
        self.menuVisualise.setTitle(QCoreApplication.translate("MainWindow", u"Visualise ", None))
    # retranslateUi

