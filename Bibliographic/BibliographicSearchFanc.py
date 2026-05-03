from PySide6.QtWidgets import QWidget
from Bibliographic.BibliographicSearchUI import Ui_BibliographicSearch
from PySide6.QtCore import Qt, Signal

class BibliographicSearch(QWidget):

    Sub_coord_signal = Signal(str)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_BibliographicSearch()
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

        self.ui.B_journal_search.clicked.connect(self.trigger_search)    
        self.ui.B_reference_search.clicked.connect(self.trigger_search)
        self.ui.B_bibcode_search.clicked.connect(self.trigger_search)
        self.ui.B_advanced_bib_search.clicked.connect(self.trigger_search)
        self.ui.B_advanced_semantic_search.clicked.connect(self.trigger_search)

    def trigger_search(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        print(f"EMITTING SIGNAL: '{button_text}'") # Verify exact text here
        self.Sub_coord_signal.emit(str(button_text))
