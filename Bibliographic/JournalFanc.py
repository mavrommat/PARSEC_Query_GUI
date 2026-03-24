from PySide6.QtWidgets import QWidget
from Bibliographic.JournalUI import Ui_JournalSearch
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLineEdit, QTextEdit, QRadioButton, QWidget)
from PySide6.QtGui import QIntValidator
from ErrorPopUp import ErrorPopup 
from datetime import datetime
class Journal(QWidget):

    Bibliography_Signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_JournalSearch()
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
        self.ui.Input_year.setMaxLength(4)
        self.ui.Input_year.setValidator(QIntValidator(1800, datetime.now().year, self))

        self.ui.B_clear_all.clicked.connect(self.clear_all_inputs)
        self.ui.B_submit.clicked.connect(self.validate_input_data)
        
    def clear_all_inputs(self):
        # Clear QLineEdit
        for widget in self.ui.main_gb.findChildren(QLineEdit):
            widget.clear()

        # Clear QTextEdit
        for widget in self.ui.main_gb.findChildren(QTextEdit):
            widget.clear()
    
    def validate_input_data(self):
        year = self.ui.Input_year.text().strip()
        page_id = self.ui.Input_page_id.text().strip()
        volume = self.ui.Input_volume.text().strip()
        Journal = self.ui.Input_publ_abbr.text()
        
        if year and not self.is_valid_year(year):
            self.show_error("Invalid Year", f"Please enter a valid 4-digit year between 1800 and {datetime.now().year}.")
            return  # Stop execution here

        if not any([year, page_id, volume]):
             self.show_error("Empty Search", "Please fill in at least one field to search.")
             return

        print(f"Validation Successful: Journal={Journal}, Year={year}, Vol={volume}, Page={page_id}")

        input_dict = {
            "Search": "Journal Search",
            "Journal": Journal,
            "Year": year,
            "Volume": volume,
            "PageID": page_id
        }
        self.Bibliography_Signal.emit(input_dict)

    def is_valid_year(self, year_str):
        if year_str.isdigit() and len(year_str) == 4:
            year_int = int(year_str)
            if 1800 <= year_int <= datetime.now().year:
                return True
        return False

    def show_error(self, title, message):
        popup = ErrorPopup(title, message)
        popup.show_popup()