from PySide6.QtWidgets import QWidget
from Coordinates.RectangularUI import Ui_Rectagular
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 

class Rectagular(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_Rectagular()
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

    # --- ADD THIS METHOD TO CHANGE THE VISUAL LABEL ---
    def update_units_label(self, selected_units):
        self.ui.units_label.setText(selected_units)

    def pass_settings(self, checked=False):
        rectangular_dist = self.ui.hypot_sb.value()
        rectangular_dist = float(rectangular_dist)
        
        # Grab the text directly from the visual label!
        current_units = self.ui.units_label.text()

        settings_info = {
            "dist": rectangular_dist,
            "units": current_units,
            "vertices": 4
            }
        
        self.validate_input_data(rectangular_dist, settings_info)
        

    def validate_input_data(self, rectangular_dist, settings_info):
        if rectangular_dist <= 0:
            popup = ErrorPopup("Unvalid Value", "Please enter a hypotenuse value > 0")
            popup.show_popup()
            return  # Stop the function from proceeding
        elif rectangular_dist > 0:
            # Emit the data!
            self.settings_info_signal.emit(settings_info)


    