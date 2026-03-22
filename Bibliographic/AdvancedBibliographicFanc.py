from PySide6.QtWidgets import QWidget
from Bibliographic.AdvancedBibliographicUI import Ui_AdvancedBibliographic
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLineEdit, QTextEdit, QRadioButton, QWidget)
from ErrorPopUp import ErrorPopup 

class AdvancedBibliographic(QWidget):

    #ObjectID_Signal = Signal(list)

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

        #self.ui.B_journal_search.clicked.connect(self.trigger_search)    
        #self.ui.B_reference_search.clicked.connect(self.trigger_search)
        #self.ui.B_reference_search.clicked.connect(self.trigger_search)
        #self.ui.B_advanced_bib_search.clicked.connect(self.trigger_search)
    
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

        print("Validation passed. Proceeding with search...")

    def is_valid_month(self, input_str):
        if input_str.isdigit():
            val = int(input_str)
            return 1 <= val <= 12
        return False

    def show_error(self, title, message):
        popup = ErrorPopup(title, message)
        popup.show_popup()