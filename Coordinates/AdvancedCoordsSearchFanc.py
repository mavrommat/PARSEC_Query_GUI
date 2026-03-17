from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PySide6.QtCore import Qt, Signal
from Coordinates.AdvancedCoordsSearchUI import Ui_AdvancedCoordsSearch





class AdvancedCoordsSearch(QWidget):

    shape_area_combo_boxes_signal = Signal(dict)
    Sub_Sub_coord_signal = Signal(str)
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
        #self.ui.coords_id_input.returnPressed.connect(self.broadcast_selection) 

    def broadcast_selection(self):
        clicked_button = self.sender()
        
        shape_name = clicked_button.text() 
        frame_choice = self.ui.frame_cb.currentText()
        units_choice = self.ui.units_cb.currentText()
        epoch_choice = self.ui.epoch_cb.currentText()
        equinox_choice = self.ui.equinox_cb.currentText()

        print(f"Sending -> Shape: {shape_name}, Frame: {frame_choice}, Units: {units_choice}, Epoch: {epoch_choice}, Equinox: {equinox_choice}")
        info_settings = {
            "Shape": shape_name,
            "Units": units_choice,
            "Frame": frame_choice,
            "Epoch": epoch_choice,
            "Equinox": equinox_choice
            }
        self.shape_area_combo_boxes_signal.emit(info_settings)
        self.Sub_Sub_coord_signal.emit(info_settings["Shape"])

    