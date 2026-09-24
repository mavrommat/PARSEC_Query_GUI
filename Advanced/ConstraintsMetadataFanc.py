from PySide6.QtWidgets import QWidget, QVBoxLayout
from Advanced.ConstraintsMetadataUI import Ui_Constraint_metadata

class ConstraintMetadataWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Constraint_metadata()
        self.ui.setupUi(self)
        self.master_dict = {}
        
        self.ui.constraints_cb.currentIndexChanged.connect(self.display_constraint)

    def filter_by_group(self, master_dict, group_index):
        self.master_dict = master_dict
        
        self.ui.constraints_cb.blockSignals(True)
        self.ui.constraints_cb.clear()
        
        # Filter constraints belonging only to the currently selected group
        group_constraints = {cid: data for cid, data in self.master_dict.items() if data.get("Group_Index") == group_index}
        
        for const_id, const_data in group_constraints.items():
            display_text = f"Constraint {const_id}: {const_data.get('Category')} / {const_data.get('Feature')}"
            self.ui.constraints_cb.addItem(display_text, const_id)
            
        self.ui.constraints_cb.blockSignals(False)

        if self.ui.constraints_cb.count() > 0:
            # Display first element when a group is selected
            self.ui.constraints_cb.setCurrentIndex(0)
            self.display_constraint(0)
        else:
            # Clear to N/A for empty groups
            self.clear_labels()

    def display_constraint(self, index):
        if index < 0:
            self.clear_labels()
            return
            
        const_id = self.ui.constraints_cb.itemData(index)
        if const_id not in self.master_dict:
            return
            
        data = self.master_dict[const_id]
        
        # Base metadata
        self.ui.label_category.setText(str(data.get("Category", "N/A")))
        self.ui.label_feature.setText(str(data.get("Feature", "N/A")))
        self.ui.label_characterisation.setText(str(data.get("Characterisation", "N/A")))
        self.ui.label_auxilary.setText(str(data.get("Auxiliary", "N/A")))
        self.ui.label_operator.setText(str(data.get("Math_Operator", "N/A")))
        self.ui.label_constraint_val.setText(str(data.get("Constraint_Val", "N/A")))
        self.ui.label_unit.setText(str(data.get("Units", "N/A")))

        # Contextual Operations Logic
        group_idx = data.get("Group_Index")
        ingroup_idx = data.get("Ingroup_Index")

        # Find adjacent constraints inside the current group
        group_peers = [c for c in self.master_dict.values() if c.get("Group_Index") == group_idx]
        next_in_group = next((c for c in group_peers if c.get("Ingroup_Index") == ingroup_idx + 1), None)
        
        # Find the first constraint of the next group
        next_group_first = next((c for c in self.master_dict.values() if c.get("Group_Index") == group_idx + 1 and c.get("Ingroup_Index") == 0), None)

        # Set Previous/Next for constraints
        prev_op = "First in Group" if ingroup_idx == 0 else data.get("Ingroup_Logic_Operator", "N/A")
        next_op = next_in_group.get("Ingroup_Logic_Operator", "N/A") if next_in_group else "Last in Group"

        # Set Previous/Next for groups
        prev_grp_op = "First Group" if group_idx == 1 else data.get("Outgroup_Logic_Operator", "N/A")
        next_grp_op = next_group_first.get("Outgroup_Logic_Operator", "N/A") if next_group_first else "Last Group"

        self.ui.label_op_prev_constraint.setText(str(prev_op))
        self.ui.label_op_next_constraint.setText(str(next_op))
        self.ui.label_op_prev_group.setText(str(prev_grp_op))
        self.ui.label_op_next_group.setText(str(next_grp_op))

    def clear_labels(self):
        labels = [
            self.ui.label_category, self.ui.label_feature, self.ui.label_characterisation, 
            self.ui.label_auxilary, self.ui.label_operator, self.ui.label_constraint_val, 
            self.ui.label_unit, self.ui.label_op_prev_group, self.ui.label_op_next_group, 
            self.ui.label_op_prev_constraint, self.ui.label_op_next_constraint
        ]
        for label in labels:
            label.setText("N/A")