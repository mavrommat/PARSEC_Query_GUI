import re
import pprint
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QDoubleValidator
from PySide6.QtWidgets import QWidget, QMenu, QToolButton, QLabel, QVBoxLayout, QGroupBox

# Assuming these are custom modules in your project
from Advanced.ConstraintsUI import Ui_Constraints
from Advanced.QueryParser import QueryParser
from Concepts.ConceptsProcessing import ConceptsProcessing

class Constraints(QWidget):
    # --- FIX 1: Changed Signal type to dict since self.groups_data is a dictionary ---
    Constraints_query_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Constraints()
        self.ui.setupUi(self)

        self.current_category = "" 
        self.current_concept = ""
        
        # --- FIX 2: Initialize state variable to avoid missing attribute errors later ---
        self.current_search_mode = "AND"
        
        # --- Group Data Structure ---
        self.groups_data = {} 
        self.group_counter = 0
        self.group_layouts = {} 
        self.group_constraint_widgets = {}

        # --- Tracking elements for deletion and logic ---
        self.ordered_groups = [] 
        self.group_ui_elements = {} 
        self.current_group_logic = "AND" 
        
        # --- Setup Scroll Area Layout ---
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.ui.Categories_features.clear()
        self.add_new_group()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("SearchWrapper")
        
        self.setStyleSheet("""
            QWidget#SearchWrapper {
                background-color: hsla(0, 0%, 12%, 150); 
                border-radius: 8px;   
            }
            QGroupBox {
                background-color: transparent;
                border: none;
                margin-top: 10px;     
            }
        """)

        self.ui.left_constrain.setEnabled(False)
        self.ui.B_AND.clicked.connect(self.set_selected_one)
        self.ui.B_OR.clicked.connect(self.set_selected_one)
        self.ui.B_NOT.clicked.connect(self.set_selected_one)

        # --- FIX 5: Applied standard Python snake_case to method names ---
        self.ui.relation_cb.currentTextChanged.connect(self.update_constraint_logic)
        self.add_concepts()

        self.ui.add_constrain.clicked.connect(self.collect_constraints)
        self.ui.B_add_manual.clicked.connect(self.manual_constraints)
        self.ui.B_del_last_constrain.clicked.connect(self.delete_last_constraint)

        self.ui.B_add_group.clicked.connect(self.add_new_group)
        self.ui.B_del_group.clicked.connect(self.delete_last_group)
        
        self.ui.B_and_gr.clicked.connect(lambda: self.set_group_logic("AND"))
        self.ui.B_or_gr.clicked.connect(lambda: self.set_group_logic("OR"))
        self.ui.B_not_gr.clicked.connect(lambda: self.set_group_logic("NOT"))

        self.num_validator = QDoubleValidator(self) 
        self.num_validator.setNotation(QDoubleValidator.StandardNotation) 

        self.ui.Confirm_constrains_next_step.clicked.connect(self.emit_updates)

    # --- FIX 1: Helper method to emit the signal cleanly ---
    def emit_updates(self):
        """Emits the current constraints data to the parent application."""
        self.Constraints_query_signal.emit(self.groups_data)

    def set_selected_one(self):
        self.ui.B_AND.setStyleSheet("")
        self.ui.B_OR.setStyleSheet("")
        self.ui.B_NOT.setStyleSheet("")
        
        clicked_button = self.sender()
        clicked_button.setStyleSheet("""
            QPushButton { background-color: hsla(248,24%,48%, 200); border: 1px solid hsla(210, 80%, 70%, 255); color: hsla(0, 0%, 100%, 255); }
            QPushButton:hover { background-color: hsla(248,24%,60%, 200); }
            """)
        
        self.current_search_mode = clicked_button.text() 

    def update_constraint_logic(self, relation):
        def clear_inputs():
            self.ui.left_constrain.clear() 
            self.ui.right_constrain.clear()

        if relation == "<=>":
            clear_inputs()
            self.ui.left_constrain.setEnabled(True)   
            self.ui.right_constrain.setEnabled(True)
        elif relation in ["<", ">", "<=", ">=", "=!", "=="]:
            clear_inputs()
            self.ui.left_constrain.setEnabled(False)   
            self.ui.right_constrain.setEnabled(True)

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

    def setup_group_ui(self, group_name):
        group_box = QGroupBox(group_name)
        group_box.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 5px; margin-top: 10px; } QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }")
        
        group_layout = QVBoxLayout()
        group_box.setLayout(group_layout)
        self.scroll_layout.addWidget(group_box) 
        self.group_layouts[group_name] = group_layout 

    def set_group_logic(self, logic):
        self.current_group_logic = logic
        
        self.ui.B_and_gr.setStyleSheet("")
        self.ui.B_or_gr.setStyleSheet("")
        self.ui.B_not_gr.setStyleSheet("")
        
        clicked_button = self.sender()
        if clicked_button:
            clicked_button.setStyleSheet("""
                QPushButton { background-color: hsla(248,24%,48%, 200); 
                            border: 1px solid hsla(210, 80%, 70%, 255); 
                            color: white; }
                                        """)

    def add_new_group(self):
        self.group_counter += 1
        new_group_name = f"Group {self.group_counter}"
        
        self.group_constraint_widgets[new_group_name] = []

        logic_label = None
        if self.ordered_groups: 
            logic_label = QLabel(self.current_group_logic)
            logic_label.setAlignment(Qt.AlignCenter)
            logic_label.setStyleSheet("""
                QLabel { color: hsla(210, 80%, 70%, 255); font-weight: bold; font-size: 14px; margin: 5px; }
            """)
            self.scroll_layout.addWidget(logic_label)
            
        group_box = QGroupBox(new_group_name)
        group_box.setObjectName("DynamicGroup")
        group_box.setStyleSheet("""
            QGroupBox#DynamicGroup { 
                border: 1px solid hsla(210, 80%, 70%, 255); 
                border-radius: 6px; margin-top: 15px; 
                background-color: hsla(0, 0%, 20%, 150); 
            } 
            QGroupBox#DynamicGroup::title { 
                subcontrol-origin: margin; left: 10px; padding: 0 5px 0 5px; 
                color: hsla(210, 80%, 70%, 255); font-weight: bold;
            }
        """)
        
        group_layout = QVBoxLayout()
        group_box.setLayout(group_layout)
        self.scroll_layout.addWidget(group_box)
        
        self.groups_data[new_group_name] = []
        self.ordered_groups.append(new_group_name)
        self.group_layouts[new_group_name] = group_layout
        self.group_ui_elements[new_group_name] = {'box': group_box, 'logic_label': logic_label}
        
        self.ui.Categories_features.addItem(new_group_name)
        self.ui.Categories_features.setCurrentText(new_group_name)

    def collect_constraints(self):
        if not hasattr(self, 'valid_concepts') or not self.valid_concepts:
            print("Error: The concept database is empty. Check your CSV file path!")
            return
        
        c_left = self.ui.left_constrain.text()
        c_right = self.ui.right_constrain.text()
        relation = self.ui.relation_cb.currentText()
        logical_op = self.current_search_mode 
        category = self.current_category
        concept = self.current_concept 
        units = self.ui.menu_units.currentText() 
        
        current_group = self.ui.Categories_features.currentText()
        
        if not concept:
            print("Please select a concept from the menu or type a manual constraint!")
            return

        value_str = f"[{c_left},{c_right}]" if relation == "<=>" else c_right

        dropdown_dict = {
            "Category": category,
            "Concept": concept,
            "Relation": relation,
            "Value": value_str,
            "Units": units,
            "Logical Operator": logical_op
        }

        f_string = f"{logical_op} ({category}.{concept} {relation} {value_str} {units})".strip()

        self.add_constraint_to_ui(current_group, f_string)
        self.groups_data.setdefault(current_group, []).append(dropdown_dict)
        

    def add_constraint_to_ui(self, group_name, constraint_string):
        if group_name not in self.group_layouts:
            return

        constraint_label = QLabel(constraint_string)
        constraint_label.setStyleSheet("""
            QLabel { background-color: hsla(248, 24%, 38%, 150); color: white; padding: 5px; border-radius: 4px; }
        """)

        constraint_label.group = group_name
        constraint_label.text_data = constraint_string

        self.group_layouts[group_name].addWidget(constraint_label)
        self.group_constraint_widgets.setdefault(group_name, []).append(constraint_label)

    def on_feature_selected(self, category_name, feature_name):        
        self.current_category = category_name
        self.current_concept = feature_name
        
    def manual_constraints(self):
        manual_text = self.ui.Manual_constrain_Input.toPlainText().strip()
        if not manual_text:
            print("Please enter a manual constraint.")
            return

        parser = QueryParser()
        try:
            result = parser.parse(manual_text)
            raw_groups = re.findall(r"\{(.*?)\}", manual_text, re.DOTALL)
            
            if "children" in result:
                for i, child_ast in enumerate(result["children"]):
                    if i > 0:
                        self.set_group_logic("OR")
                    
                    current_group = self.ui.Categories_features.currentText()
                    
                    if i == 0 and current_group and len(self.groups_data.get(current_group, [])) == 0:
                        target_group = current_group
                    else:
                        self.add_new_group()
                        target_group = self.ordered_groups[-1]
                    
                    raw_text = raw_groups[i].strip() if i < len(raw_groups) else "Parsed Manual Constraint"
                    ui_string = f"[Manual Input] {raw_text}"
                    
                    self.add_constraint_to_ui(target_group, ui_string)
                    self.groups_data[target_group].append({
                        "Type": "Manual",
                        "AST": child_ast,
                        "Raw_Text": raw_text
                    })
                    
            self.ui.Manual_constrain_Input.clear() 
            

        except Exception as e:
            print(f"Syntax Error in Manual Constraint: {e}")

    def delete_last_group(self):
        if len(self.ordered_groups) <= 1:
            print("Cannot delete the only remaining group.")
            return 
            
        last_group_name = self.ordered_groups.pop()
        
        del self.groups_data[last_group_name]
        del self.group_layouts[last_group_name]
        
        # --- FIX 3: Remove from constraint widgets dict to stop memory leak ---
        if last_group_name in self.group_constraint_widgets:
            del self.group_constraint_widgets[last_group_name]
        
        index = self.ui.Categories_features.findText(last_group_name)
        if index >= 0:
            self.ui.Categories_features.removeItem(index)
            
        elements = self.group_ui_elements.pop(last_group_name)
        
        box = elements['box']
        self.scroll_layout.removeWidget(box)
        box.deleteLater()
        
        logic_label = elements['logic_label']
        if logic_label:
            self.scroll_layout.removeWidget(logic_label)
            logic_label.deleteLater()
            
    

    def delete_last_constraint(self):
        group_name = self.ui.Categories_features.currentText()

        widgets = self.group_constraint_widgets.get(group_name, [])
        data = self.groups_data.get(group_name, [])

        if not widgets or not data:
            print("No constraints to delete.")
            return

        last_widget = widgets.pop()
        last_widget.deleteLater()

        data.pop()
        self.group_layouts[group_name].removeWidget(last_widget)

        