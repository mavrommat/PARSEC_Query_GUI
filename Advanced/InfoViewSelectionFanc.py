import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QRadioButton, QScrollArea, 
                               QLabel, QMenu, QToolButton)

from Concepts.OntologyProcessing import OntologyParser
from Advanced.InfoViewSelectionUI import Ui_InfoViewSelection

class InfoViewSelection(QWidget):
    Displayed_concepts_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_InfoViewSelection()
        self.ui.setupUi(self)

        self.current_category = "" 
        self.current_concept = ""
        self.current_characterisation = ""
        self.current_auxiliary = ""
        self.current_option = "None Selected"
        
        self.selected_features_data = [] 
        self.current_view = "all_columns"
        
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

        self.ui.R_all_columns.clicked.connect(lambda: self.set_view_logic("all_columns"))
        self.ui.R_specific_columns.clicked.connect(lambda: self.set_view_logic("specific_columns"))
        self.ui.B_apply_column.clicked.connect(self.add_column_to_ui)
        self.ui.B_confirm_query.clicked.connect(self.emit_confimation)

        self.processor = OntologyParser(file_path="Concepts/data/concepts/concepts_for_metadata.json", 
                                        offline_api_file="Concepts/offline_API_ontology.json")
        self.add_concepts()
        
        # Set default view state
        self.ui.R_all_columns.setChecked(True)
        self.set_view_logic("all_columns")

    def add_concepts(self):
        try:
            self.valid_concepts = self.processor.build_dictionary()
            
            # Setup Left Menu Tree
            main_menu = QMenu(self)
            
            aux_options = ["No Auxilary"]
            global_auxiliaries = list(self.processor.VALID_AUXILIARY)
            if global_auxiliaries:
                aux_options.extend(sorted(global_auxiliaries))
                
            for category, features in self.valid_concepts.items():
                if not features: continue
                
                category_menu = QMenu(category, self)
                
                for feature_name in features.keys():
                    feature_menu = QMenu(feature_name, self)
                    
                    characterizations = self.processor.get_feature_characterizations(category, feature_name)
                    char_options = []
                    
                    if isinstance(characterizations, list) and characterizations:
                        char_options.extend(characterizations)
                    
                    # Failsafe: If there are no characterizations, add "None" so the menu chain doesn't break
                    if not char_options:
                        char_options.append("None")
                        
                    for char_name in char_options:
                        char_menu = QMenu(char_name, self)
                        
                        # Apply auxiliaries to the final cascade
                        for aux_name in aux_options:
                            aux_action = QAction(aux_name, self)
                            # Tie the resolved pathway 
                            aux_action.triggered.connect(
                                lambda checked=False, c=category, f=feature_name, ch=char_name, a=aux_name: 
                                self.on_full_selection(c, f, ch, a)
                            )
                            char_menu.addAction(aux_action)
                            
                        feature_menu.addMenu(char_menu)
                        
                    category_menu.addMenu(feature_menu)
                    
                main_menu.addMenu(category_menu)
            
            self.ui.menu_categories_features.setMenu(main_menu)
            self.ui.menu_categories_features.setPopupMode(QToolButton.InstantPopup)

            # Setup the Options Menu (replacing the blank menu placeholder)
            options_menu = QMenu(self)
            
            # 1. Preset Option (Direct action, no cascade)
            preset_action = QAction("Preset: Integrated Value to PARSEC", self)
            preset_action.triggered.connect(
                lambda: self.on_option_selection("Preset: Integrated Value to PARSEC")
            )
            options_menu.addAction(preset_action)
            
            # Raw Data Options 
            raw_data_menu = QMenu("Raw Data", self)
            
            raw_options = [
                "LLM Description",
                "Raw Units",
                "Raw Column Name",
                "Raw Value",
                "Paper DOI",              
                "Author/Institution",     
                "Publication Date"        
            ]
            
            for option in raw_options:
                action = QAction(option, self)
                action.triggered.connect(
                    lambda checked=False, opt=option: self.on_option_selection(f"Raw Data / {opt}")
                )
                raw_data_menu.addAction(action)
                
            options_menu.addMenu(raw_data_menu)
            
            self.ui.options_menu.setMenu(options_menu)
            self.ui.options_menu.setPopupMode(QToolButton.InstantPopup)

        except Exception as e:
            print(f"An error occurred loading concepts: {e}")

    def on_option_selection(self, selection_path):
        self.current_option = selection_path  
        self.ui.options_menu.setText(selection_path)
        print(f"Option selected: {selection_path}")

    def on_full_selection(self, category_name, feature_name, characterisation, auxiliary):        
        self.current_category = category_name
        self.current_concept = feature_name
        self.current_characterisation = characterisation
        self.current_auxiliary = auxiliary
        
        display_text = f"{category_name} / {feature_name} | {characterisation} | {auxiliary}"
        self.ui.menu_categories_features.setText(display_text)

    def add_column_to_ui(self):
        if not self.current_category or not self.current_concept:
            print("Select a complete Concept pathway first.")
            return
            
        char_val = self.current_characterisation
        aux_val = self.current_auxiliary
        opt_val = self.current_option  
        
        col_data = {
            "Category": self.current_category, 
            "Concept": self.current_concept,
            "Characterisation": char_val,
            "Auxiliary": aux_val,
            "Option": opt_val  
        }
        self.selected_features_data.append(col_data)

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(10, 4, 10, 4)
        row_widget.setStyleSheet("""
            QWidget { 
                background-color: hsla(248, 24%, 38%, 150); 
                border-radius: 6px; 
            }
        """)
        
        # Updated display_text 
        display_text = f"{self.current_category} / {self.current_concept} | Char: {char_val} | Aux: {aux_val} | Opt: {opt_val}"
        feature_label = QLabel(display_text)
        feature_label.setStyleSheet("""
            QLabel { 
                background-color: transparent; 
                color: white; 
                border: none; 
            }
        """)
        
        del_btn = QPushButton("✕")
        del_btn.setFixedSize(28, 28)

        del_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #888888;
                border: none;
                font-family: "Arial";
                font-size: 15px;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
            }
            QPushButton:hover {
                color: #ff6b6b;
                background: rgba(255, 255, 255, 15);
                border-radius: 6px;
            }
            QPushButton:pressed {
                color: #ff4444;
                background: rgba(255, 255, 255, 25);
            }
        """)

        del_btn.clicked.connect(lambda: self.remove_column(row_widget, col_data))
        row_layout.addWidget(feature_label)
        row_layout.addWidget(del_btn)
        self.scroll_layout.addWidget(row_widget)

    def remove_column(self, widget, col_data):
        self.scroll_layout.removeWidget(widget)
        widget.deleteLater()
        if col_data in self.selected_features_data:
            self.selected_features_data.remove(col_data)

    def set_view_logic(self, view):
        self.current_view = view
        self.ui.R_all_columns.setStyleSheet("")
        self.ui.R_specific_columns.setStyleSheet("")
        
        clicked_button = self.sender()
        if clicked_button:
            clicked_button.setStyleSheet("""
                QRadioButton { background-color: hsla(248,24%,48%, 200); 
                               border: 1px solid hsla(210, 80%, 70%, 255); 
                               color: white; }
            """)
            
        if view == "all_columns":
            self.ui.matrix_view_gb.setEnabled(False)
        else:
            self.ui.matrix_view_gb.setEnabled(True)

    def emit_confimation(self):
        print("Final Confirmation: Emitting the selected concepts and view mode.")
        payload = {
            "view_mode": self.current_view,
            "features": self.selected_features_data if self.current_view == "specific_columns" else []
        }
        self.Displayed_concepts_signal.emit(payload)