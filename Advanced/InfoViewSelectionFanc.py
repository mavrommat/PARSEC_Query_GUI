import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QPushButton, QRadioButton, QScrollArea, 
                               QLabel, QMenu, QToolButton)

# Assuming these are custom modules in your project
from Concepts.ConceptsProcessing import ConceptsProcessing
from Advanced.InfoViewSelectionUI import Ui_InfoViewSelection

class InfoViewSelection(QWidget):
    Displayed_concepts_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        
        # Setup UI
        self.ui = Ui_InfoViewSelection()
        self.ui.setupUi(self)

        self.current_category = "" 
        self.current_concept = ""
        self.current_view = "default_view"
        
        # --- Tracking elements for deletion and logic ---
        self.feature_widgets = []        
        self.selected_features_data = [] 
        
        # --- Setup Scroll Area Layout ---
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("SearchWrapper")
        
        self.setStyleSheet("""
            QWidget#SearchWrapper {
                background-color: hsla(0, 0%, 12%, 150); 
                border-radius: 8px;   
            }
        """)

        self.ui.B_del_feature.clicked.connect(self.del_last_feature)
        self.ui.B_confirm_query.clicked.connect(self.emit_updates)
        self.ui.R_default.clicked.connect(lambda: self.set_view_logic("default_view"))
        self.ui.R_object_view.clicked.connect(lambda: self.set_view_logic("object_view"))

        # EXACT replica call
        self.add_concepts()

    # --- EXACT REPLICA OF add_concepts FROM ConstraintsFanc.py ---
    def add_concepts(self):
        file_name = 'Concepts/Parsec_concepts v.1.1 - sifis_current_version.csv'
        processor = ConceptsProcessing(file_name)

        try:
            self.valid_concepts = processor.build_dictionary()
            main_menu = QMenu(self)

            for category, features in self.valid_concepts.items():
                category_submenu = QMenu(category, self)
                for feature in features:
                    feature_action = QAction(feature, self)
                    feature_action.triggered.connect(
                        lambda checked=False, c=category, f=feature: self.on_feature_selected(c, f)
                    )
                    category_submenu.addAction(feature_action)
                main_menu.addMenu(category_submenu)
            
            self.ui.menu_categories_features.setMenu(main_menu)
            self.ui.menu_categories_features.setPopupMode(QToolButton.InstantPopup)
            self.ui.menu_categories_features.setText("Select Concept")

        except Exception as e:
            print(f"An error occurred loading concepts: {e}")

    # --- EXACT REPLICA OF on_feature_selected FROM ConstraintsFanc.py ---
    def on_feature_selected(self, category_name, feature_name):        
        self.current_category = category_name
        self.current_concept = feature_name
        
        # New call to add to the scroll layout directly
        self.add_feature_to_ui(category_name, feature_name)

    def add_feature_to_ui(self, category, feature):
        display_text = f"{category} -> {feature}"
        
        # Styled to match the Constraints UI styling you use
        feature_label = QLabel(display_text)
        feature_label.setStyleSheet("""
            QLabel { 
                background-color: hsla(248, 24%, 38%, 150); 
                color: white; 
                padding: 5px; 
                border-radius: 4px; 
                margin-top: 5px;
            }
        """)
        
        self.scroll_layout.addWidget(feature_label)
        
        self.feature_widgets.append(feature_label)
        self.selected_features_data.append({"Category": category, "Concept": feature})

    def del_last_feature(self):
        if not self.feature_widgets:
            print("No features to delete.")
            return

        last_widget = self.feature_widgets.pop()
        self.selected_features_data.pop()

        self.scroll_layout.removeWidget(last_widget)
        last_widget.deleteLater()

    def set_view_logic(self, view):
        self.current_view = view
        
        self.ui.R_default.setStyleSheet("")
        self.ui.R_object_view.setStyleSheet("")
        
        clicked_button = self.sender()
        if clicked_button:
            clicked_button.setStyleSheet("""
                QRadioButton { background-color: hsla(248,24%,48%, 200); 
                            border: 1px solid hsla(210, 80%, 70%, 255); 
                            color: white; }
            """)

    def emit_updates(self):
        payload = {
            "view_mode": self.current_view,
            "features": self.selected_features_data
        }
        self.Displayed_concepts_signal.emit(payload)