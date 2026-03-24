from PySide6.QtWidgets import QWidget
from Bibliographic.BibcodeSearchUI import Ui_BibliocodeSearch
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 
from PySide6.QtWidgets import (
    QLineEdit, QTextEdit, QRadioButton, QWidget)
class Bibcode(QWidget):

    Bibliography_Signal = Signal(dict)


    def __init__(self):
        super().__init__()
        
        self.ui = Ui_BibliocodeSearch()
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

        self.ui.B_submit.clicked.connect(self.validate_input_data)
        self.ui.B_clear_all.clicked.connect(self.clear_all_inputs)

    
    def clear_all_inputs(self):
        # Clear QLineEdit
        for widget in self.ui.main_gb.findChildren(QLineEdit):
            widget.clear()

        # Clear QTextEdit
        for widget in self.ui.main_gb.findChildren(QTextEdit):
            widget.clear()

    
    def validate_input_data(self):
        raw_input = self.ui.Input_bibcodes.toPlainText().strip()

        if not raw_input:
            self.show_error("Empty Input", "Please enter at least one Bibcode.")
            return

        # The rest of your logic remains the same
        bibcode_list = [code.strip() for code in raw_input.split(",") if code.strip()]
        invalid_codes = [c for c in bibcode_list if len(c) != 19]
        if invalid_codes:
            self.show_error("Invalid Format", 
                            f"Bibcodes must be 19 characters. Found errors: {', '.join(invalid_codes)}")
            return

        search_data = {"bibcodes": bibcode_list}
        self.Bibliography_Signal.emit(search_data)
        print(f"Emitting {len(bibcode_list)} bibcodes for search.")

    def show_error(self, title, message):
        popup = ErrorPopup(title, message)
        popup.show_popup()
    