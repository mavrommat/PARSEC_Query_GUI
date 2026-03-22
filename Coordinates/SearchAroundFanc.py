from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PySide6.QtCore import Qt, Signal
from Coordinates.SearchAroundUI import Ui_SearchAround
from ErrorPopUp import ErrorPopup 

from Coordinates.RadiusFanc import Radius
from Coordinates.RectangularFanc import Rectagular
from Coordinates.PolygonFanc import Polygon

class SearchAround(QWidget):

    Sub_Sub_coord_signal = Signal(str)
    
    final_coords_query_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_SearchAround()
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
            QLabel {
                color: white;
                font-weight: bold;
            }
        """)
        self.ui.B_Radius_Search.clicked.connect(self.broadcast_selection)
        self.ui.B_Rect_Search.clicked.connect(self.broadcast_selection)
        self.ui.B_polyg_Search.clicked.connect(self.broadcast_selection)

        # 2. Add an instance variable to remember the target/frame/epoch settings
        self.current_info_settings = {}

        self.Radius = Radius()
        self.Rectangle = Rectagular()
        self.Polygon = Polygon()

        # Connect the confirm buttons from the shape widgets
        self.Radius.settings_info_signal.connect(self.shape_info_process)
        self.Rectangle.settings_info_signal.connect(self.shape_info_process)
        self.Polygon.settings_info_signal.connect(self.shape_info_process)


    def broadcast_selection(self):
        clicked_button = self.sender()
        
        coords_id_input = self.ui.coords_id_input.text()
        shape_name = clicked_button.text() 
        frame_choice = self.ui.frame_cb.currentText()
        units_choice = self.ui.units_cb.currentText()
        epoch_choice = self.ui.epoch_cb.currentText()
        equinox_choice = self.ui.equinox_cb.currentText()
        
        info_settings = {
            "Target": coords_id_input,
            "Shape": shape_name,
            "Units": units_choice,
            "Frame": frame_choice,
            "Epoch": epoch_choice,
            "Equinox": equinox_choice
            }
        
        self.current_info_settings = info_settings # save the settings 

        self.validate_input_data(coords_id_input, info_settings)

        self.ui.coords_id_input.clear()

    def validate_input_data(self, coords_id_input, info_settings):
        if coords_id_input == "":
            popup = ErrorPopup("Empty target", "Please enter a target")
            popup.show_popup()
            return  # Stop the function from proceeding
        
        elif coords_id_input != "":
            self.Sub_Sub_coord_signal.emit(info_settings["Shape"]) # Emit the data

    def shape_info_process(self, settings_info):
            CoordsQuerySelections = {
                "Target": self.current_info_settings.get("Target", "N/A"),
                "Shape": self.current_info_settings.get("Shape", "N/A"),
                "Vertices": settings_info.get("Vertices", "N/A"), 
                "Distance": settings_info.get("Distance", 0),      
                "Units": self.current_info_settings.get("Units", ""),       
                "Frame": self.current_info_settings.get("Frame", "N/A"),
                "Epoch": self.current_info_settings.get("Epoch", "N/A"),
                "Equinox": self.current_info_settings.get("Equinox", "N/A")
            }

            print(f"Broadcasting Final Selection: {CoordsQuerySelections}")
                
            self.final_coords_query_signal.emit(CoordsQuerySelections)