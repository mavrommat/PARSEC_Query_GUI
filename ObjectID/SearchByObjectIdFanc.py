from PySide6.QtWidgets import QWidget
from ObjectID.SearchByObjectIdUI import Ui_SearchByObjectId
from PySide6.QtCore import Qt, Signal

class SearchByObjectIdWidget(QWidget):

    ObjectID_Signal = Signal(list)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_SearchByObjectId()
        self.ui.setupUi(self)
        
        # --- 2. THE MAGIC FIX ---
        # Force the custom QWidget to actually render background stylesheets
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        # ------------------------
        
        # Give this wrapper a unique Object Name
        self.setObjectName("SearchWrapper")
        
        # Apply the dark background ONLY to the wrapper
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

        self.ui.object_id_input.returnPressed.connect(self.trigger_search)    
        self.ui.B_objectID_search.clicked.connect(self.trigger_search)

    def trigger_search(self):
        # Grab the exact string the user typed into the box
        user_input = self.ui.object_id_input.text()

        object_list = [obj.strip() for obj in user_input.split(",") if obj.strip()]

        # Print input objects
        if len(object_list) > 0: 
            print(f"Searching for: {user_input}")
            self.ObjectID_Signal.emit(object_list)
            
            # Clear the box 
            self.ui.object_id_input.clear()


    
