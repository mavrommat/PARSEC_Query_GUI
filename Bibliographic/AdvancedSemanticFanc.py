from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QRadioButton
from PySide6.QtCore import Qt, Signal
from Bibliographic.AdvancedSemanticUI import Ui_AdvancedSemantic
from ErrorPopUp import ErrorPopup 

class AdvancedSemantic(QWidget):

    # Bibliography_Signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AdvancedSemantic()
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
        """)

        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.added_widgets = []   
        self.collected_data = []  

        self.prefix_mapping = {
            "catalog ID (J/...)": "cat:",
            "file name (hatlas.dat)": "table:",
            "title": "title:",
            "abstract": "abs:",
            "keywords": "kw:",
            "general description": "desc:",
            "column name": "col:",
            "column description": "coldesc:",
            "units": "unit:",
            "authors": "author:",
            "references / bibcode": "ref:",
            "search everywhere": "text:"
        }

        self.ui.B_add.clicked.connect(self.add_entry)
        self.ui.B_del.clicked.connect(self.delete_last_entry)
        self.ui.B_submit.clicked.connect(self.validate_input_data)
        
        # Connect ComboBox change to update the LineEdit
        self.ui.cmd_cb.currentTextChanged.connect(self.update_line_edit_prefix)
        
        # Connect LineEdit Enter key 
        self.ui.lineEdit.returnPressed.connect(self.add_entry)

        # Initialize the line edit with the default combobox prefix
        self.update_line_edit_prefix(self.ui.cmd_cb.currentText())


    def update_line_edit_prefix(self, selected_text):
        new_prefix = self.prefix_mapping.get(selected_text, "text:") + " "
        current_text = self.ui.lineEdit.text()

        for old_prefix in self.prefix_mapping.values():
            if current_text.startswith(old_prefix + " "):
                current_text = current_text[len(old_prefix) + 1:]
                break
            elif current_text.startswith(old_prefix):
                current_text = current_text[len(old_prefix):]
                break

        self.ui.lineEdit.setText(new_prefix + current_text.lstrip())
        self.ui.lineEdit.setFocus()


    def add_entry(self):
        text_val = self.ui.lineEdit.text().strip()
        combo_val = self.ui.cmd_cb.currentText()
        llm_expanded = self.ui.radioButton.isChecked()
        
        # Determine the current prefix to check if the user entered actual text
        current_prefix = self.prefix_mapping.get(combo_val, "text:")

        # If the input is empty OR it's literally just the prefix with nothing else
        if not text_val or text_val == current_prefix:
            self.show_error("Empty Input", "Please enter a value before adding.")
            return

        llm_status = "Yes" if llm_expanded else "No"
        display_string = f"[{combo_val}] : {text_val} (LLM Expanded: {llm_status})"

        entry_label = QLabel(display_string)
        entry_label.setStyleSheet("""
            QLabel { 
                background-color: hsla(248, 24%, 38%, 150); 
                color: white; 
                padding: 8px; 
                border-radius: 4px; 
                margin-bottom: 4px;
            }
        """)

        self.scroll_layout.addWidget(entry_label)
        self.added_widgets.append(entry_label)

        self.collected_data.append({
            "type": combo_val,
            "value": text_val,
            "llm_expansion": llm_expanded
        })

        # --- NEW: Clear line edit and reset the prefix for the next entry ---
        self.ui.lineEdit.clear()
        self.update_line_edit_prefix(self.ui.cmd_cb.currentText())


    def delete_last_entry(self):
        if not self.added_widgets:
            return 

        last_widget = self.added_widgets.pop()
        self.scroll_layout.removeWidget(last_widget)
        last_widget.deleteLater()

        self.collected_data.pop()


    def validate_input_data(self):
        if not self.collected_data:
            self.show_error("Empty Search", "Please add at least one search parameter to the list.")
            return

        search_payload = {"semantic_queries": self.collected_data}
        # self.Bibliography_Signal.emit(search_payload)
        
        print(f"Emitting {len(self.collected_data)} constraints for search:")
        for item in self.collected_data:
            print(f" - {item}")


    def clear_all_inputs(self):
        for widget in self.ui.main_gb.findChildren(QLineEdit):
            widget.clear()

        for widget in self.ui.main_gb.findChildren(QTextEdit):
            widget.clear()


    def show_error(self, title, message):
        popup = ErrorPopup(title, message)
        popup.show_popup()