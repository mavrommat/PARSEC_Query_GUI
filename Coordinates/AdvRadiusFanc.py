from PySide6.QtWidgets import QWidget
from Coordinates.AdvRadiusUI import Ui_AdvRadius
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 

class AdvancedRadius(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_AdvRadius()
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

        self.ui.B_confirm_area.clicked.connect(self.pass_settings)

    def update_units_label(self, selected_units):
        self.ui.units_label.setText(selected_units)

    def pass_settings(self, checked=False):
        raw_radius = self.ui.radius_sb.value()
        radius_val = float(raw_radius)
        Coords = self.ui.AdvCoords_input.text()
        # Grab the text directly from the visual label!
        current_units = self.ui.units_label.text()

        settings_info = {
            "Coodrs": Coords,
            "dist": radius_val,
            "units": current_units,
            "Vertices": 1
            }
        
        self.validate_input_data(radius_val, settings_info)
        

    def validate_input_data(self, radius_val, settings_info):
        if radius_val <= 0:
            popup = ErrorPopup("Unvalid Value", "Please enter a angular value > 0")
            popup.show_popup()
            return  # Stop the function from proceeding
       
        elif radius_val > 0:
            # Emit the data!
            self.settings_info_signal.emit(settings_info)

    