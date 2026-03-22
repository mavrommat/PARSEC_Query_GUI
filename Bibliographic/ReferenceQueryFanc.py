from PySide6.QtWidgets import QWidget
from Bibliographic.ReferenceQueryUI import Ui_ReferenceQuery
from PySide6.QtCore import Qt, Signal

class Reference(QWidget):

    #ObjectID_Signal = Signal(list)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_ReferenceQuery()
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

        #self.ui.B_journal_search.clicked.connect(self.trigger_search)    
        #self.ui.B_reference_search.clicked.connect(self.trigger_search)
        #self.ui.B_reference_search.clicked.connect(self.trigger_search)
        #self.ui.B_advanced_bib_search.clicked.connect(self.trigger_search)
    