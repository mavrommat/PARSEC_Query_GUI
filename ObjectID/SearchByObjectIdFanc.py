import pandas as pd
from PySide6.QtWidgets import QWidget
from ObjectID.SearchByObjectIdUI import Ui_SearchByObjectId
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup

# Import the ObjectResolver
from Coordinates.Resolver import ObjectResolver

class SearchByObjectIdWidget(QWidget):

    ObjectID_Signal = Signal(list)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_SearchByObjectId()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        # ------------------------
        
        # Give this wrapper a unique Object Name
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

        # --- 3. LOAD DATABASE & INITIALIZE RESOLVER ---
        try:
            df = pd.read_parquet("Database/astro_10k.parquet")
            self.Resolver = ObjectResolver(df=df)
        except Exception as e:
            print(f"Failed to load database in Object ID Search: {e}")

        self.ui.object_id_input.returnPressed.connect(self.trigger_search)    
        self.ui.B_objectID_search.clicked.connect(self.trigger_search)

    def trigger_search(self):
        user_input = self.ui.object_id_input.text()
        object_list = [obj.strip() for obj in user_input.split(",") if obj.strip()]

        if not object_list:
            popup = ErrorPopup("Empty Input", "Please enter at least one Object ID.")
            popup.show_popup()
            return

        # VALIDATE IDs 
        invalid_ids = []
        
        for obj in object_list:
            try:
                payload = self.Resolver.resolve(obj)
                if payload.get("status") == "Not Found":
                    invalid_ids.append(obj)
            except Exception as e:
                popup = ErrorPopup("Resolver Error", f"An error occurred while resolving {obj}: {str(e)}")
                popup.show_popup()
                return

        # If any IDs were not found show popup
        if invalid_ids:
            missing_str = ", ".join(invalid_ids)
            popup = ErrorPopup("Invalid Object IDs", f"The following IDs were not found in the database:\n{missing_str}")
            popup.show_popup()
            return

        print(f"Searching for verified objects: {object_list}")
        self.ObjectID_Signal.emit(object_list)
        
        # Clear the box 
        self.ui.object_id_input.clear()