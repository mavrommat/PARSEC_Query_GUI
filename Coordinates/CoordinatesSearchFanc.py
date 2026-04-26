from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt, Signal
from Coordinates.CoordinateSearchUI import Ui_CoordinatesSearch
class SearchByCoordinatesWidget(QWidget):

    Sub_coord_signal = Signal(str)
    area_deleted_signal = Signal()
    Next_step_signal = Signal(str) 

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CoordinatesSearch()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("SearchWrapper")

        # Added QPushButton:checked logic directly to the stylesheet!
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
            QLabel {
                color: white;
                font-weight: bold;
            }
            QPushButton:checked { 
                background-color: hsla(248,24%,48%, 200); 
                border: 1px solid hsla(210, 80%, 70%, 255); 
                color: hsla(0, 0%, 100%, 255); 
            }
        """)

        self.ui.B_add_search_area.setCheckable(True)

        # Connect coord mode
        self.ui.B_coord_mode_search_around_object_specified_coords.clicked.connect(self.sub_coord_query_activation)
        self.ui.B_coord_mode_advanced_search.clicked.connect(self.sub_coord_query_activation)
        
        # delete buttons
        self.ui.B_delete_search_area.clicked.connect(self.delete_area_to_scroll_widget) 

        # scroll area
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop) 

        # Confirm button
        self.ui.B_submit_coord_search.clicked.connect(self.broadcast_next_step)
    
    # Determine UX activation
    def sub_coord_query_activation(self):
        print(f"Add button is checked: {self.ui.B_add_search_area.isChecked()}")
        if self.ui.B_add_search_area.isChecked():
            clicked_button = self.sender()
            button_text = clicked_button.text()
            print(f"EMITTING SIGNAL: '{button_text}'") # Verify exact text here
            self.Sub_coord_signal.emit(str(button_text))


    def add_area_to_scroll_widget(self, settings_dict):
        target = settings_dict.get("Target", "N/A")
        shape = settings_dict.get("Shape", "N/A")
        dist = settings_dict.get("Distance", 0) 
        units = settings_dict.get("Units", "")
        
        display_text = f"Coordinate Area -> Target: {target} | {shape}: {dist} {units}"
        
        row_label = QLabel(display_text)
        row_label.setStyleSheet("""
            QLabel { 
                background-color: hsla(248, 24%, 38%, 150); 
                color: white; 
                padding: 5px; 
                border-radius: 4px; 
                margin-top: 5px;
            }
        """)
        
        self.scroll_layout.addWidget(row_label) # Add to scroll layout
        
        self.ui.B_add_search_area.setChecked(False) # uncheck the Add button
        
        print(f"Added new search area for Target: {target}")

    def delete_area_to_scroll_widget(self):
        total_rows = self.scroll_layout.count()
        
        if total_rows > 0:
            last_item = self.scroll_layout.itemAt(total_rows - 1)
            widget_to_delete = last_item.widget()
            
            if widget_to_delete:
                widget_to_delete.deleteLater()
                print("Deleted the bottom coordinate row!")
                
                self.area_deleted_signal.emit() 
        else:
            print("No rows left to delete!")

    def broadcast_next_step(self):
        self.Next_step_signal.emit("Coord Search Completed")