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
        self.ui.B_AND.clicked.connect(self.set_selected_one)
        self.ui.B_OR.clicked.connect(self.set_selected_one)
        self.ui.B_NOT.clicked.connect(self.set_selected_one)

        self.ui.relation_cb.currentTextChanged.connect(self.Constrain_logic)

    def set_selected_one(self):
        self.ui.B_AND.setStyleSheet("")
        self.ui.B_OR.setStyleSheet("")
        self.ui.B_NOT.setStyleSheet("")
        
        clicked_button = self.sender()
        clicked_button.setStyleSheet("""
            QPushButton { background-color: hsla(248,24%,48%, 200); border: 1px solid hsla(210, 80%, 70%, 255); color: hsla(0, 0%, 100%, 255); }
            QPushButton:hover { background-color: hsla(248,24%,60%, 200); }
            """)
        
        self.current_search_mode = clicked_button.text() # Save current search mode name

    def Constrain_logic(self, relation):

        def clear_inputs():
            self.ui.Manual_constrain_Input.clear()
            # Note the exact spelling from your UI file below!
            self.ui.left_constrain.clear() 
            self.ui.right_constrain.clear()

        if relation == "<=>":
            clear_inputs()
            self.ui.left_constrain.setEnabled(True)   # Fixed typo here
            self.ui.right_constrain.setEnabled(True)
        
        # A much cleaner way to check multiple conditions!
        elif relation in ["<", ">", "<=", ">=", "=!"]:
            clear_inputs()
            self.ui.left_constrain.setEnabled(True)   
            self.ui.right_constrain.setEnabled(False)

    