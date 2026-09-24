from ast import operator
import re
import pprint
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QDoubleValidator
from PySide6.QtWidgets import QWidget, QMenu, QToolButton, QLabel, QVBoxLayout, QGroupBox, QButtonGroup, QApplication
from matplotlib import units
# Assuming these are custom modules in your project
from Advanced.ConstraintsUI import Ui_Constraints
#from Advanced.QueryParser import QueryParser

from Concepts.OntologyProcessing import OntologyParser
from Advanced.ConstraintsMetadataFanc import ConstraintMetadataWidget
from Advanced.Regex_parser import parse_custom_query, validate_constraint_values
class Constraints(QWidget):
    Constraints_query_signal = Signal(object)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Constraints()
        self.ui.setupUi(self)

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
            QLabel {
                color: white;
                font-weight: bold;
            }
            QPushButton:checked { 
                background-color: hsla(248,24%,48%, 200); 
                border: 1px solid hsla(210, 80%, 70%, 255); 
                color: hsla(0, 0%, 100%, 255); 
            }
        """)

        self.Ontology = OntologyParser()

        self.MASTER_DICT = { }
        self.constraint_id = 0
        self.current_ingroup_logic_operator = "AND"
        self.current_outgroup_logic_operator = "AND"
        self.current_group_index = 1
        self.total_groups = 1 
        self.current_ingroup_index = 0
        self.current_category = None
        self.current_feature = None
        self.current_characterization = None
        self.current_auxiliary = None
        self.current_math_operator = None
        self.current_constraint_val = None
        self.current_units = None

        self.lock_left_input = True
        self.ui.left_constraint_val.setDisabled(True)

        #self.ui.B_add_manual.clicked.connect(self.add_manual_constraits)
        # In-Group Logic Operators (AND, OR, AND NOT)
        self.ui.B_AND.clicked.connect(lambda: self.set_ingroup_logic_operator("AND"))
        self.ui.B_OR.clicked.connect(lambda: self.set_ingroup_logic_operator("OR"))
        self.ui.B_AND_NOT.clicked.connect(lambda: self.set_ingroup_logic_operator("AND NOT"))
        self.ingroup_btn_group = QButtonGroup(self)
        for btn in [self.ui.B_AND, self.ui.B_OR, self.ui.B_AND_NOT]:
            btn.setCheckable(True)
            self.ingroup_btn_group.addButton(btn)
        
        self.ui.B_AND.setChecked(True) # default selection
        self.populate_categories_features()
        self.ui.Concept_Characterisation_cb.currentTextChanged.connect(self.set_characterisation)
        self.ui.Auxiliary_Concept_cb.currentTextChanged.connect(self.set_auxiliary)
        self.ui.Operator_symbol.currentTextChanged.connect(self.set_math_operator)
        self.ui.menu_units.currentTextChanged.connect(self.set_units)

        # Out-Group Logic Operators (AND, OR, NOT)
        self.ui.B_add_gr.clicked.connect(self.add_group)
        self.ui.B_del_gr.clicked.connect(self.del_group)
        self.ui.Group_cb.currentIndexChanged.connect(self.select_group)
        self.ui.B_and_gr.clicked.connect(lambda: self.group_logic_operator("AND"))
        self.ui.B_or_gr.clicked.connect(lambda: self.group_logic_operator("OR"))
        self.ui.B_not_gr.clicked.connect(lambda: self.group_logic_operator("AND NOT"))
        self.outgroup_btn_group = QButtonGroup(self)
        for btn in [self.ui.B_and_gr, self.ui.B_or_gr, self.ui.B_not_gr]:
            btn.setCheckable(True)
            self.outgroup_btn_group.addButton(btn)
            
        self.ui.B_and_gr.setChecked(True) # default selection

        self.ui.Operator_symbol.currentTextChanged.connect(self.collect_value_specifics)

        self.ui.add_constraint.clicked.connect(self.add_constraint)

        # Initialize defaults from the UI before any user interaction
        self.current_math_operator = self.ui.Operator_symbol.currentText()
        self.current_units = self.ui.menu_units.currentText()
        self.current_auxiliary = self.ui.Auxiliary_Concept_cb.currentText()
        self.current_characterisation = self.ui.Concept_Characterisation_cb.currentText()

        self.ui.B_add_manual.clicked.connect(self.add_manual_constraints)
        self.ui.B_copy_constraints.clicked.connect(self.copy_constraints_to_clipboard)

        #===============================================
        # Replace scroll area with the metadata widget
        #===============================================
        self.metadata_widget = ConstraintMetadataWidget()
        self.ui.verticalLayout_4.replaceWidget(self.ui.constrains_scroll_area, self.metadata_widget)
        self.ui.constrains_scroll_area.hide()
        self.ui.constrains_scroll_area.deleteLater()
        #===============================================
        self.metadata_widget.ui.B_del_constraint.clicked.connect(self.delete_current_constraint)

        self.ui.Confirm_constraints_next_step.clicked.connect(self.emit_constraints)

    def disable_left_input(self, disable):
        self.lock_left_input = disable
        self.ui.left_constraint_val.setDisabled(disable)

    def set_ingroup_logic_operator(self, operator):
        self.current_ingroup_logic_operator = operator

    def populate_categories_features(self):
        categories_dict = self.Ontology.build_dictionary()
        main_menu = QMenu(self)
        
        # 1. Add Categories and Features directly to the main menu
        for category, features in categories_dict.items():
            if not features:
                continue
                
            category_menu = main_menu.addMenu(category)
            
            for feature in features.keys():
                action = QAction(feature, self)
                action.triggered.connect(
                    lambda checked=False, c=category, f=feature: self.set_category_feature(c, f)
                )
                category_menu.addAction(action)
                
        # Attach the constructed menu to the Concepts_cb button
        self.ui.Concepts_cb.setMenu(main_menu)
        self.ui.Concepts_cb.setPopupMode(QToolButton.InstantPopup)
        
        # Populate the Auxiliary Combobox directly from the Ontology constant
        self.ui.Auxiliary_Concept_cb.clear()
        self.ui.Auxiliary_Concept_cb.addItems(["None", "Unspecified"])
        
        # Fetch the VALID_AUXILIARY from OntologyParser
        global_auxiliaries = list(self.Ontology.VALID_AUXILIARY)
        if global_auxiliaries:
            # Sort alphabetically for better UX
            self.ui.Auxiliary_Concept_cb.addItems(sorted(global_auxiliaries))

    def set_category_feature(self, category, feature):
        # Update class variables
        self.current_category = category
        self.current_feature = feature
        
        # Update the button text to display the user's selection
        self.ui.Concepts_cb.setText(f"{category} / {feature}")
        print(f"User selected: {category} / {feature}")
        
        # Trigger the individual population functions
        self.update_characterisations(category, feature)
        self.update_units(category, feature)

    def update_characterisations(self, category, feature):
        # Reset to default UI state
        self.ui.Concept_Characterisation_cb.clear()
        self.ui.Concept_Characterisation_cb.addItem("Unspecified")
        
        # Fetch and add feature-specific characterizations
        characterizations = self.Ontology.get_feature_characterizations(category, feature)
        if isinstance(characterizations, list) and characterizations:
            self.ui.Concept_Characterisation_cb.addItems(characterizations)

    def set_characterisation(self, characterisation):
        self.current_characterisation = characterisation

    def set_auxiliary(self, auxiliary):
        self.current_auxiliary = auxiliary

    def set_math_operator(self, operator):
        self.current_math_operator = operator

    def set_units(self, units):
        self.current_units = units

    def update_units(self, category, feature):
        # Reset to default UI state
        self.ui.menu_units.clear()
        self.ui.menu_units.addItem("Unspecified")
        
        # Fetch and add feature-specific units
        units = self.Ontology.get_feature_unit(category, feature)
        if isinstance(units, list) and units:
            self.ui.menu_units.addItems(units)

    def collect_value_specifics(self):
        operator = self.ui.Operator_symbol.currentText()

        # String
        if operator == "str":
            self.ui.left_constraint_val.setDisabled(True)
            value = self.ui.right_constraint_val.text().strip()

            if not value:
                return None

            return [value]

        # Range
        if operator == "<=>":
            self.ui.left_constraint_val.setDisabled(False)
            left_text = self.ui.left_constraint_val.text().strip()
            right_text = self.ui.right_constraint_val.text().strip()

            try:
                left_value = float(left_text)
                right_value = float(right_text)
            except ValueError:
                return None

            return [left_value, right_value]

        # Normal numeric operator
        self.ui.left_constraint_val.setDisabled(True)
        right_text = self.ui.right_constraint_val.text().strip()

        try:
            right_value = float(right_text)
        except ValueError:
            return None

        return [right_value]

    def add_group(self):
        self.total_groups += 1
        self.ui.Group_cb.addItem(f"Group {self.total_groups}")
        self.current_group_index = self.total_groups
        self.ui.Group_cb.setCurrentIndex(self.current_group_index - 1)
        
    def select_group(self, index):
        self.current_group_index = index + 1

    def group_logic_operator(self, operator):
        self.current_outgroup_logic_operator = operator

    def del_group(self):
        if self.total_groups > 1:
            self.ui.Group_cb.removeItem(self.current_group_index - 1)
            self.total_groups -= 1
            for i in range(self.current_group_index - 1, self.total_groups):
                self.ui.Group_cb.setItemText(i, f"Group {i + 1}")

            self.current_group_index = min(self.current_group_index, self.total_groups)
            self.ui.Group_cb.setCurrentIndex(self.current_group_index - 1)


    def select_group(self, index):
        self.current_group_index = index + 1
        # Synchronize ingroup index for new groups
        group_items = [c for c in self.MASTER_DICT.values() if c["Group_Index"] == self.current_group_index]
        self.current_ingroup_index = len(group_items)
        # Push to widget
        self.metadata_widget.filter_by_group(self.MASTER_DICT, self.current_group_index)

    def add_constraint(self):
        constraint_val = self.collect_value_specifics()
        if constraint_val is None:
            return

        constraint = {
            "ID": self.constraint_id,
            "Category": self.current_category,
            "Feature": self.current_feature,
            "Characterisation": self.current_characterisation,
            "Auxiliary": self.current_auxiliary,
            "Math_Operator": self.current_math_operator,
            "Constraint_Val": constraint_val,
            "Units": self.current_units,
            "Ingroup_Logic_Operator": self.current_ingroup_logic_operator,
            "Outgroup_Logic_Operator": self.current_outgroup_logic_operator,
            "Group_Index": self.current_group_index,
            "Ingroup_Index": self.current_ingroup_index
        }

        self.MASTER_DICT[self.constraint_id] = constraint
        self.constraint_id += 1
        self.current_ingroup_index += 1

        print(f"Added constraint: {constraint}")

        # Update UI and jump to the newly added constraint
        self.metadata_widget.filter_by_group(self.MASTER_DICT, self.current_group_index)
        self.metadata_widget.ui.constraints_cb.setCurrentIndex(self.metadata_widget.ui.constraints_cb.count() - 1)

    def delete_current_constraint(self):
        current_index = self.metadata_widget.ui.constraints_cb.currentIndex()
        if current_index < 0: return

        const_id = self.metadata_widget.ui.constraints_cb.itemData(current_index)
        if const_id not in self.MASTER_DICT: return

        del self.MASTER_DICT[const_id]
        self.reindex_constraints()
        self.metadata_widget.filter_by_group(self.MASTER_DICT, self.current_group_index)

    def del_group(self):
        if self.total_groups > 1:
            # Wipe dictionary items associated with this group
            keys_to_delete = [k for k, v in self.MASTER_DICT.items() if v["Group_Index"] == self.current_group_index]
            for k in keys_to_delete:
                del self.MASTER_DICT[k]

            self.reindex_constraints(group_deleted=self.current_group_index)

            # Prevent signaling during UI adjustments
            self.ui.Group_cb.blockSignals(True)
            self.ui.Group_cb.removeItem(self.current_group_index - 1)
            self.total_groups -= 1

            for i in range(self.ui.Group_cb.count()):
                self.ui.Group_cb.setItemText(i, f"Group {i + 1}")

            self.current_group_index = min(self.current_group_index, self.total_groups)
            self.ui.Group_cb.setCurrentIndex(self.current_group_index - 1)
            self.ui.Group_cb.blockSignals(False)

            self.select_group(self.current_group_index - 1)

    def reindex_constraints(self, group_deleted=None):
        # Sort remaining dictionaries mathematically to preserve sequences
        sorted_items = sorted(self.MASTER_DICT.items(), key=lambda x: (x[1]["Group_Index"], x[1]["Ingroup_Index"]))

        new_dict = {}
        new_id = 0
        current_grp = -1
        ingroup_idx = 0

        for old_id, data in sorted_items:
            grp = data["Group_Index"]
            # Shift group index down if a preceding group was deleted
            if group_deleted is not None and grp > group_deleted:
                grp -= 1

            # Reset ingroup index when moving to a new group iteration
            if grp != current_grp:
                current_grp = grp
                ingroup_idx = 0

            data["ID"] = new_id
            data["Group_Index"] = grp
            data["Ingroup_Index"] = ingroup_idx

            new_dict[new_id] = data
            ingroup_idx += 1
            new_id += 1

        self.MASTER_DICT = new_dict
        self.constraint_id = new_id

        # Safely align current insertion index for active group
        group_items = [c for c in self.MASTER_DICT.values() if c["Group_Index"] == self.current_group_index]
        self.current_ingroup_index = len(group_items)

    def add_manual_constraints(self):
        # Extract text from the UI widget
        raw_text = self.ui.Manual_constrain_Input.toPlainText().strip()
        if not raw_text:
            return

        try:
            # Parse structural syntax and validate against the ontology instance
            parsed_constraints = parse_custom_query(raw_text, self.Ontology)
            
            if not parsed_constraints:
                return

            # Shift parsed group indices to append after existing UI groups
            is_empty = len(self.MASTER_DICT) == 0
            group_offset = 0 if is_empty else self.total_groups
            max_group_added = 0

            for constraint in parsed_constraints:
                # Validate extracted values against the math operator rules
                if not validate_constraint_values(constraint["Math_Operator"], constraint["Constraint_Val"]):
                    print(f"Value mismatch for parsed constraint {constraint['ID']}")
                    continue

                # Align regex 0-based indices with GUI 1-based logic
                new_group_index = group_offset + constraint["Group_Index"] + 1
                max_group_added = max(max_group_added, new_group_index)

                constraint["Group_Index"] = new_group_index
                constraint["ID"] = self.constraint_id

                # Push to the main orchestrator state
                self.MASTER_DICT[self.constraint_id] = constraint
                self.constraint_id += 1

            # Update the Group Combobox if new groups were created
            if max_group_added > self.total_groups:
                # Avoid duplicating group numbers if overwriting an empty default group 1
                start_idx = self.total_groups + 1 if not is_empty else 2 
                for i in range(start_idx, max_group_added + 1):
                    self.ui.Group_cb.addItem(f"Group {i}")
                self.total_groups = max_group_added

            # Navigate GUI to the last added group
            self.current_group_index = self.total_groups
            self.ui.Group_cb.setCurrentIndex(self.current_group_index - 1)
            
            # Align ingroup index for further UI additions
            group_items = [c for c in self.MASTER_DICT.values() if c["Group_Index"] == self.current_group_index]
            self.current_ingroup_index = len(group_items)

            # Push the updated dictionary to the metadata widget
            self.metadata_widget.filter_by_group(self.MASTER_DICT, self.current_group_index)
            self.metadata_widget.ui.constraints_cb.setCurrentIndex(self.metadata_widget.ui.constraints_cb.count() - 1)
            
            # Clear text field on success
            self.ui.Manual_constrain_Input.clear()
            print(f"Successfully appended {len(parsed_constraints)} manual constraints.")

        except ValueError as e:
            print(f"Query Parsing Error: {e}")

    def copy_constraints_to_clipboard(self):
        if not self.MASTER_DICT:
            print("No constraints to copy.")
            return

        # Group all constraints by Group_Index
        groups = {}
        for const_id, data in self.MASTER_DICT.items():
            grp = data["Group_Index"]
            if grp not in groups:
                groups[grp] = []
            groups[grp].append(data)

        sorted_group_keys = sorted(groups.keys())
        final_query_parts = []

        for i, grp_key in enumerate(sorted_group_keys):
            constraints = groups[grp_key]
            constraints = sorted(constraints, key=lambda x: x["Ingroup_Index"])
            
            group_string_parts = []
            for j, const in enumerate(constraints):
                aux = const.get("Auxiliary", "None")
                cat = const.get("Category", "")
                feat = const.get("Feature", "")
                char = const.get("Characterisation", "Unspecified")
                op = const.get("Math_Operator", "")
                units = const.get("Units", "Unspecified")
                
                vals = const.get("Constraint_Val", [])
                val_str = ", ".join(str(v) for v in vals)
                
                # regex compatible tuple
                const_str = f"({aux}|{cat}|{feat}|{char} {op} [{val_str}] \"{units}\")"
                
                # Append the ingroup operator if this is not the last constraint in the group
                if j < len(constraints) - 1:
                    next_in_op = constraints[j+1].get("Ingroup_Logic_Operator", "AND")
                    const_str += f" {next_in_op}"
                
                group_string_parts.append(const_str)
            
            # ingroup parts are wrapped in curly braces
            group_inner = " ".join(group_string_parts)
            group_str = f"{{{group_inner}}}"
            
            # Append the outgroup operator if this is not the last group
            if i < len(sorted_group_keys) - 1:
                next_grp_key = sorted_group_keys[i+1]
                # The operator linking to the NEXT group is stored in the NEXT group's first constraint
                out_op = groups[next_grp_key][0].get("Outgroup_Logic_Operator", "AND")
                group_str += f" {out_op}"
                
            final_query_parts.append(group_str)
            
        # final string
        final_query_string = " ".join(final_query_parts)
        
        QApplication.clipboard().setText(final_query_string)
        print(f"Copied syntax to clipboard: {final_query_string}")

    def emit_constraints(self):
        if not self.MASTER_DICT:
            print("Error: Cannot proceed. The constraints list is empty.")
            return 
            
        self.Constraints_query_signal.emit(self.MASTER_DICT)
        print(f"Emitted {len(self.MASTER_DICT)} constraints to the main pipeline.")