from PySide6.QtWidgets import QWidget
from Advanced.ConstraintsUI import Ui_Constraints
from PySide6.QtCore import Qt, Signal

class Constraints(QWidget):
    Answer_Signal = Signal(bool)

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
        """)

        