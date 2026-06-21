from Bibliographic.AdvancedBibliographicUI import Ui_AdvancedBibliographic
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 
from PySide6.QtWidgets import QWidget, QLineEdit, QTextEdit, QRadioButton, QButtonGroup # Added QButtonGroup
class AdvancedBibliographic(QWidget):

    Bibliography_Signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AdvancedBibliographic()
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

        self.ui.Input_start_month.setMaxLength(2)
        self.ui.Input_start_year.setMaxLength(4)
        self.ui.Input_end_month.setMaxLength(2)
        self.ui.Input_end_year.setMaxLength(4)


        self.ui.B_clear_all.clicked.connect(self.clear_all_inputs)
        self.ui.B_submit.clicked.connect(self.validate_input_data)

        # --- Fix Radio Button Exclusivity ---
        self.author_btn_group = QButtonGroup(self)
        self.author_btn_group.addButton(self.ui.R_and_author)
        self.author_btn_group.addButton(self.ui.R_or_author)

        self.object_btn_group = QButtonGroup(self)
        self.object_btn_group.addButton(self.ui.R_and_object)
        self.object_btn_group.addButton(self.ui.R_or_object)

        author_tooltip = (
            "<b>Format:</b> Last Name, First Name<br>"
            "<b>Multiple Authors:</b> Separate entries using <b>semicolons (;)</b>, <b>new lines (Enter)</b>, or <b>parentheses</b>.<br>"
            "<i>Note: Do not use commas to separate different authors.</i>"
        )
        self.ui.Input_authors.setToolTip(author_tooltip)
        
        object_tooltip = (
            "<b>Format:</b> Enter object identifiers.<br>"
            "<b>Multiple Objects:</b> Separate entries using <b>semicolons (;)</b>, <b>new lines (Enter)</b>, or <b>parentheses</b>."
        )
        self.ui.Input_objects.setToolTip(object_tooltip)

        self.ui.Input_authors.setPlaceholderText(
            "Format: Last, First. Separate entries using semicolons (;), parentheses, or new lines."
        )
        self.ui.Input_objects.setPlaceholderText(
            "Enter object identifiers. Separate entries using semicolons (;), commas, or new lines."
        )

    def clear_all_inputs(self):
        # Clear QLineEdit
        for widget in self.ui.main_gb.findChildren(QLineEdit):
            widget.clear()

        # Clear QTextEdit
        for widget in self.ui.main_gb.findChildren(QTextEdit):
            widget.clear()

        # Reset radio buttons
        for rb in self.ui.main_gb.findChildren(QRadioButton):
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.setAutoExclusive(True)


    def validate_input_data(self):
        s_m = self.ui.Input_start_month.text().strip()
        e_m = self.ui.Input_end_month.text().strip()
        s_y = self.ui.Input_start_year.text().strip()
        e_y = self.ui.Input_end_year.text().strip()

        # Validate Month values if they are not empty
        if s_m and not self.is_valid_month(s_m):
            return self.show_error("Invalid Start Month", "Month must be 01-12")
        if e_m and not self.is_valid_month(e_m):
            return self.show_error("Invalid End Month", "Month must be 01-12")

        # Years to integers 
        start_year = int(s_y) if s_y.isdigit() else None
        end_year = int(e_y) if e_y.isdigit() else None

        if start_year and end_year:
            if end_year < start_year:
                return self.show_error("Date Range Error", "End year is before start year.")
            
            # If years are the same, check that end month isn't before start month
            if start_year == end_year and s_m and e_m:
                if int(e_m) < int(s_m):
                    return self.show_error("Date Range Error", "End month is before start month.")

        # --- Extract and Parse Text Fields ---
        raw_authors = self.ui.Input_authors.toPlainText().strip()
        raw_objects = self.ui.Input_objects.toPlainText().strip()
        
        authors_list = [a.strip() for a in raw_authors.replace(';', '\n').replace('(', '\n').replace(')', '\n').split('\n') if a.strip()]
        objects_list = [o.strip() for o in raw_objects.replace(';', '\n').replace(',', '\n').replace('(', '\n').replace(')', '\n').split('\n') if o.strip()]
        
        title = self.ui.Input_title.text().strip()
        abstract_keywords = self.ui.Input_abstract_keywords.text().strip()

        # Logic Operators
        def get_logic_operator(and_rb, or_rb):
            if and_rb.isChecked(): return "AND"
            if or_rb.isChecked(): return "OR"
            return None 
            
        author_logic = get_logic_operator(self.ui.R_and_author, self.ui.R_or_author)
        object_logic = get_logic_operator(self.ui.R_and_object, self.ui.R_or_object)
        title_logic = get_logic_operator(self.ui.R_and_title, self.ui.R_or_title)
        abs_logic = get_logic_operator(self.ui.R_and_abs_keyw, self.ui.R_or_abs_keyw)

        print("Validation passed. Proceeding with search...")
        
        # 3. Package the parsed lists and emit
        search_data = {
            "Search": "Advanced Bibliographic",
            "Start_Month": s_m,
            "Start_Year": s_y,
            "End_Month": e_m,
            "End_Year": e_y,
            "Authors": authors_list,      
            "Author_Logic": author_logic,
            "Objects": objects_list,      
            "Object_Logic": object_logic,
            "Title": title,
            "Title_Logic": title_logic,
            "Abstract_Keywords": abstract_keywords,
            "Abstract_Logic": abs_logic
        }
        
        self.Bibliography_Signal.emit(search_data)

    def is_valid_month(self, input_str):
        if input_str.isdigit():
            val = int(input_str)
            return 1 <= val <= 12
        return False

    def show_error(self, title, message):
        popup = ErrorPopup(title, message)
        popup.show_popup()