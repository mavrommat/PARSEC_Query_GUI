from PySide6.QtWidgets import QWidget
from Advanced.QuestionCoordinatesUI import Ui_QuestionCoordinates
from PySide6.QtCore import Qt, Signal

class AdvancedQuestion(QWidget):
    Answer_Signal = Signal(bool)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_QuestionCoordinates()
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

        self.ui.B_yes.clicked.connect(lambda: self.BroadcastDecision(True))
        self.ui.B_no.clicked.connect(lambda: self.BroadcastDecision(False))

    def BroadcastDecision(self, answer):
        self.Answer_Signal.emit(answer)