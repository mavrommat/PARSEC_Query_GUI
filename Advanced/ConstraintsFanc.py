import re
import pprint
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QDoubleValidator
from PySide6.QtWidgets import QWidget, QMenu, QToolButton, QLabel, QVBoxLayout, QGroupBox

# Assuming these are custom modules in your project
from Advanced.ConstraintsUI import Ui_Constraints
from Advanced.DSLParser import DSLParser
from Advanced.QueryParser import QueryParser

from Concepts.ConceptsProcessing import ConceptsProcessing

class Constraints(QWidget):
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

        self.ui.B_copy_query.clicked.connect(self.copy_query_to_clipboard)
    
    def emit_updates(self):
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
        # Force standalone NOT to be AND NOT for group connections
        if logic == "NOT":
            logic = "AND NOT"
            
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
        new_group_name = f"Criteria {self.group_counter}"
        
        self.group_constraint_widgets[new_group_name] = []

        logic_label = None
        # FIX 4: Ensure the NOT label is visually drawn even if it's the very first group
        if self.ordered_groups or self.current_group_logic in ["NOT", "AND NOT"]: 
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

        # --- FIX: Differentiate Outer Group Logic from Inner Item Logic ---
        is_first = len(self.groups_data.get(current_group, [])) == 0
        
        # If it's the first item, save the Group connection logic for the clipboard. 
        # Otherwise, save the Inner UI logic.
        applied_logic = self.current_group_logic if is_first else logical_op

        # Intercept standalone "NOT" for data storage
        if applied_logic == "NOT":
            applied_logic = "AND NOT"

        # --- Map the UI's "<=>" to the Parser's "IN" ---
        is_array_operator = (relation == "<=>" or relation == "IN")
        display_relation = "IN" if is_array_operator else relation

        # Format to match the bracket style used by the AST stringifier 
        value_str = f"[{c_left},{c_right}]" if is_array_operator else f"[{c_right}]"
        
        # Wraps the UI unit in literal double quotes
        unit_str = f' "{units}"' if units else ""

        dropdown_dict = {
            "Category": category,
            "Concept": concept,
            "Relation": display_relation,
            "Value": value_str,
            "Units": units,
            "Logical Operator": applied_logic  # Now correctly stores OR for the first item!
        }

        # The clean string for the condition block (without the AND/OR prepended)
        clean_string = f"({category}.{concept} {display_relation} {value_str}{unit_str})".strip()

        # If there are already widgets in this group, add the logic separator first
        existing_widgets = self.group_constraint_widgets.get(current_group, [])
        if len(existing_widgets) > 0:
            
            # Ensure the UI visual label strictly uses the inner logic
            ui_inner_logic = "AND NOT" if logical_op == "NOT" else logical_op
            
            inner_logic_label = QLabel(ui_inner_logic)
            inner_logic_label.setAlignment(Qt.AlignCenter)
            inner_logic_label.setStyleSheet("""
                QLabel { color: hsla(210, 80%, 70%, 255); font-weight: bold; font-size: 12px; margin: 3px; }
            """)
            
            self.group_layouts[current_group].addWidget(inner_logic_label)
            self.group_constraint_widgets[current_group].append(inner_logic_label)

        # Finally, add the actual condition block
        self.add_constraint_to_ui(current_group, clean_string)
        self.groups_data.setdefault(current_group, []).append(dropdown_dict)

        # --- UI RESET LOGIC ---
        # Reset the internal state
        self.current_category = ""
        self.current_concept = ""
        
        # Reset the tool button text to default
        self.ui.menu_categories_features.setText("Select Concept")
        
        # Clear the input boxes
        self.ui.left_constrain.clear()
        self.ui.right_constrain.clear()
        

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
        
        # FIX 1: Update the button text to show what was just selected
        self.ui.menu_categories_features.setText(f"{category_name} \u2192 {feature_name}")
        
    def manual_constraints(self):
        manual_text = self.ui.Manual_constrain_Input.toPlainText().strip()
        if not manual_text:
            print("Please enter a manual constraint.")
            return

        parser = QueryParser(manual_text)
        try:
            full_ast = parser.parse()
            
            if not isinstance(full_ast, list):
                full_ast = [full_ast]
                
            # FIX 1: Ignore UI buttons for the very first group to prevent "ghost" logic
            pending_logic = "AND" if not self.ordered_groups else self.current_group_logic
            
            for node in full_ast:
                if 'logic' in node:
                    pending_logic = node['logic']
                    self.set_group_logic(pending_logic)
                    continue
                    
                current_group = self.ui.Categories_features.currentText()
                if current_group and len(self.group_constraint_widgets.get(current_group, [])) == 0:
                    target_group = current_group
                else:
                    self.add_new_group()
                    target_group = self.ordered_groups[-1]
                    
                elements = node.get('elements', [node]) if node.get('type') == 'group' else [node]
                inner_pending_logic = "AND" 
                
                for child in elements:
                    if 'logic' in child:
                        inner_pending_logic = child['logic']
                        
                        # FIX 2: If the first inner condition has a NOT, skip drawing it 
                        # as a separate label so we can bake it directly into the condition text.
                        is_first_logic = len(self.group_constraint_widgets.get(target_group, [])) == 0
                        if is_first_logic and inner_pending_logic == "NOT":
                            continue 
                            
                        inner_logic_label = QLabel(inner_pending_logic)
                        inner_logic_label.setAlignment(Qt.AlignCenter)
                        inner_logic_label.setStyleSheet("""
                            QLabel { color: hsla(210, 80%, 70%, 255); font-weight: bold; font-size: 12px; margin: 3px; }
                        """)
                        self.group_layouts[target_group].addWidget(inner_logic_label)
                        self.group_constraint_widgets.setdefault(target_group, []).append(inner_logic_label)
                        continue 
                        
                    cond_str = self._ast_to_string(child)
                    is_first = len(self.groups_data.get(target_group, [])) == 0
                    
                    # FIX 3: Bake the inner NOT into the raw text so it is never erased
                    if is_first and inner_pending_logic == "NOT":
                        cond_str = f"NOT {cond_str}"
                        
                    applied_logic = pending_logic if is_first else inner_pending_logic
                    
                    self.add_constraint_to_ui(target_group, cond_str)
                    self.groups_data[target_group].append({
                        "Type": "Manual",
                        "Logical_Operator": applied_logic,
                        "AST": child,
                        "Raw_Text": cond_str
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
            
    

    def delete_last_group(self):
        if len(self.ordered_groups) <= 1:
            print("Cannot delete the only remaining group.")
            return 
            
        last_group_name = self.ordered_groups.pop()
        
        del self.groups_data[last_group_name]
        del self.group_layouts[last_group_name]
        
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
            
        # FIX: Dial the counter back so the next added group reclaims this number
        self.group_counter -= 1

    def delete_last_constraint(self):
        group_name = self.ui.Categories_features.currentText()

        widgets = self.group_constraint_widgets.get(group_name, [])
        data = self.groups_data.get(group_name, [])

        if not widgets or not data:
            print("No constraints to delete.")
            return

        # 1. Remove the condition block
        last_widget = widgets.pop()
        self.group_layouts[group_name].removeWidget(last_widget)
        last_widget.deleteLater()
        
        # Remove the underlying data entry
        data.pop()

        # 2. If the next thing in the UI list is a standalone logic label, remove it too
        if widgets and widgets[-1].text() in ["AND", "OR", "NOT", "AND NOT", "OR NOT"]:
            logic_widget = widgets.pop()
            self.group_layouts[group_name].removeWidget(logic_widget)
            logic_widget.deleteLater()

    def extract_brace_blocks(self, text):
        blocks = []
        depth = 0
        start = None

        for i, ch in enumerate(text):
            if ch == "{":
                if depth == 0:
                    start = i + 1
                depth += 1

            elif ch == "}":
                depth -= 1
                if depth == 0 and start is not None:
                    blocks.append(text[start:i])

        return blocks
    
    def _ast_to_string(self, node):
        """Helper to reconstruct AST nodes into clean strings for UI labels."""
        if 'variable' in node:
            var = node['variable']
            op = node['operator']
            val = node['value']
            unit = node.get('unit', '')
            
            # If it's a string match, skip the float/int math formatting
            if op == '~=':
                val_str = f"[{','.join(val)}]"
            else:
                v_list = [int(v) if isinstance(v, float) and v.is_integer() else v for v in val]
                val_str = f"[{','.join(map(str, v_list))}]"
                
            return f"{var} {op} {val_str} {unit}".strip()
            
        if 'type' in node and node['type'] == 'group':
            inner = " ".join(self._ast_to_string(n) for n in node.get('elements', []))
            return f"({inner})"
            
        if 'logic' in node:
            return node['logic']
            
        return ""
    
    def copy_query_to_clipboard(self):
        if not self.groups_data:
            print("No criteria to copy.")
            return

        query_blocks = []
        
        for i, group_name in enumerate(self.ordered_groups):
            if group_name not in self.groups_data or not self.groups_data[group_name]:
                continue
                
            group_items = self.groups_data[group_name]
            
            # The logic operator that connects this group to the previous one
            group_logic = group_items[0].get("Logical_Operator", group_items[0].get("Logical Operator", "AND"))
            
            inner_strings = []
            for j, item in enumerate(group_items):
                if item.get("Type") == "Manual":
                    cond_str = item.get("Raw_Text", "")
                else:
                    cat = item.get("Category", "")
                    conc = item.get("Concept", "")
                    rel = item.get("Relation", "")
                    val = item.get("Value", "")
                    unit = item.get("Units", "")
                    
                    unit_str = f' "{unit}"' if unit else ""
                    cond_str = f"({cat}.{conc} {rel} {val}{unit_str})".strip()

                if j == 0:
                    inner_strings.append(cond_str)
                else:
                    # Grab the inner logic that connects this condition
                    item_logic = item.get("Logical_Operator", item.get("Logical Operator", "AND"))
                    inner_strings.append(f"{item_logic} {cond_str}")
            
            group_content = " ".join(inner_strings)
            formatted_group = f"{{ {group_content} }}"
            
            # Handle group formatting
            if i == 0:
                # If the very first group was flagged as negated
                if group_logic in ["NOT", "AND NOT", "OR NOT"]:
                    query_blocks.append(f"NOT {formatted_group}")
                else:
                    query_blocks.append(formatted_group)
            else:
                query_blocks.append(f"{group_logic}\n{formatted_group}")

        final_query = "\n".join(query_blocks)
        
        from PySide6.QtGui import QGuiApplication
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(final_query)
        
        print("Successfully copied to clipboard:\n" + final_query)