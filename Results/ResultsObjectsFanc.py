# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QHBoxLayout, QMenu, QSpacerItem, QSizePolicy, QToolButton, QVBoxLayout, QWidget
)
from Results.ResultsObjectsUI import Ui_Results_Objects
from Results.ObjectResultWidgetFanc import ObjectResultWidget

class Results_Objects(QWidget):
    request_view_signal = Signal(str, dict)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Results_Objects()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("SearchWrapper")
        
        self.setStyleSheet("""
            QWidget#SearchWrapper { background-color: hsla(0, 0%, 12%, 150); border-radius: 8px; }
            QScrollArea { border: none; background: transparent; }
            QWidget#scrollAreaWidgetContents { background: transparent; }
        """)

        self.list_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.list_layout.setSpacing(12)

        self.view_options = ["Overview"]
        self.current_view_mode = "Overview"  # State tracker for the central router

        self._setup_toolbar()

    def _setup_toolbar(self):
        self.ui.toolbar_results.setVisible(False)
        top_bar_layout = QHBoxLayout()
        top_bar_layout.setContentsMargins(0, 0, 0, 0)

        self.btn_view = QToolButton(self)
        self.btn_view.setText(f"View Mode: {self.current_view_mode}")
        self.btn_view.setPopupMode(QToolButton.InstantPopup) 
        
        self.view_menu = QMenu(self)
        self.view_menu.setStyleSheet("""
            QMenu { background-color: hsla(248, 24%, 32%, 255); color: white; border: 1px solid hsla(248, 24%, 60%, 150); }
            QMenu::item:selected { background-color: hsla(248, 24%, 52%, 255); }
        """)
        self.btn_view.setMenu(self.view_menu)
        
        top_bar_layout.addWidget(self.btn_view)
        top_bar_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.ui.verticalLayout.insertLayout(0, top_bar_layout)

    def set_available_views(self, views_list):
        self.view_options = views_list
        self.view_menu.clear()
        
        if views_list:
            self.set_active_view_mode(views_list[0])
            
        for option in views_list:
            action = self.view_menu.addAction(option)
            # Default argument opt=option prevents lambda loop-capture bug
            action.triggered.connect(lambda checked=False, opt=option: self.set_active_view_mode(opt))

    def set_active_view_mode(self, mode):
        # Updates the UI and internal state when a new mode is selected
        self.current_view_mode = mode
        self.btn_view.setText(f"View Mode: {mode}")

    def receive_processed_data(self, data_list):
        for i in reversed(range(self.list_layout.count())): 
            widget = self.list_layout.itemAt(i).widget()
            if widget: 
                widget.deleteLater()

        for item in data_list:
            card = ObjectResultWidget(item)
            
            card.request_view_signal.connect(
                lambda data: self.request_view_signal.emit(self.current_view_mode, data)
            )
            
            self.list_layout.addWidget(card)