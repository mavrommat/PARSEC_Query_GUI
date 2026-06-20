from PySide6.QtWidgets import QWidget
from Bibliographic.BibliographicSearchUI import Ui_BibliographicSearch
from PySide6.QtCore import Qt, Signal

class BibliographicSearch(QWidget):

    Sub_coord_signal = Signal(str)
    # master signal to pass the gathered data out 
    Master_Search_Signal = Signal(dict) 

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
        print(f"EMITTING SIGNAL: '{button_text}'")
        self.Sub_coord_signal.emit(str(button_text))

    # 2. Add the central receiving method
    def receive_search_data(self, search_data: dict):
        print(f"BibliographicSearch received data: {search_data}")
        # Pass it forward to the backend or main window
        self.Master_Search_Signal.emit(search_data)
        
 