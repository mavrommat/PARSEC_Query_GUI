from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PySide6.QtCore import Qt, Signal
from Coordinates.AdvancedCoordsSearchUI import Ui_AdvancedCoordsSearch

from Coordinates.AdvRadiusFanc import AdvancedRadius
from Coordinates.AdvancedRectangleFanc import AdvancedRectangle
from Coordinates.AdvancedCustomFanc import AdvancedCustom

class AdvancedCoordsSearch(QWidget):

    Sub_Sub_coord_signal = Signal(str)
    final_coords_query_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AdvancedCoordsSearch()
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
        self.ui.B_Custom_Search.clicked.connect(self.broadcast_selection)

        # 2. Add an instance variable to remember the target/frame/epoch settings
        self.current_info_settings = {}

        self.AdvancedRadius = AdvancedRadius()
        self.AdvancedRectangle = AdvancedRectangle()
        self.AdvancedCustom = AdvancedCustom()

        # Connect the confirm buttons from the shape widgets
        self.AdvancedRadius.settings_info_signal.connect(self.shape_info_process)
        self.AdvancedRectangle.settings_info_signal.connect(self.shape_info_process)
        self.AdvancedCustom.settings_info_signal.connect(self.shape_info_process)

    def broadcast_selection(self):
        clicked_button = self.sender()
        
        shape_name = clicked_button.text() 
        frame_choice = self.ui.frame_cb.currentText()
        units_choice = self.ui.units_cb.currentText()
        epoch_choice = self.ui.epoch_cb.currentText()
        equinox_choice = self.ui.equinox_cb.currentText()

        # Push the unit text to the child widgets
        self.AdvancedRadius.ui.units_label.setText(units_choice)
        self.AdvancedRectangle.ui.unit_label.setText(units_choice)
        self.AdvancedCustom.ui.units_label.setText(units_choice)

        print(f"Sending -> Shape: {shape_name}, Frame: {frame_choice}, Units: {units_choice}, Epoch: {epoch_choice}, Equinox: {equinox_choice}")
        info_settings = {
            "Shape": shape_name,
            "Units": units_choice,
            "Frame": frame_choice,
            "Epoch": epoch_choice,
            "Equinox": equinox_choice
            }
        
        self.current_info_settings = info_settings # save the settings 

        self.Sub_Sub_coord_signal.emit(info_settings["Shape"])

    def shape_info_process(self, settings_info):
            if settings_info["Advanced"] is False:
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
            elif settings_info["Advanced"] is True:
                CoordsQuerySelections = {
                    "Target": settings_info.get("Target", "N/A"),
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