from PySide6.QtWidgets import QWidget
from Coordinates.AdvancedRectanlgleUI import Ui_AdvancedRectangle
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 
import re
class AdvancedRectangle(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_AdvancedRectangle()
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
        raw_vertices = self.ui.vertices_ra_dec_input.text().strip()

        # 2. Use RegEx to extract the pairs
        # This pattern looks for: (number, number) and handles decimals and negative signs
        matches = re.findall(r'\(\s*([+-]?\d*\.?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*\)', raw_vertices)

        # 3. Validate! (Assuming you expect exactly 2 points for opposite corners)
        if len(matches) != 2:
            popup = ErrorPopup(
                "Invalid Coordinate Format", 
                "Please enter exactly two coordinate pairs.\nFormat: (ra1, dec1), (ra2, dec2)"
            )
            popup.show_popup()
            return  # Stop the function 

        # 4. Convert text strings into float tuples
        vertices_list = [(float(ra), float(dec)) for ra, dec in matches]

        # Grab the text directly from the visual label
        current_units = self.ui.units_label.text()

        settings_info = {
            "dist": vertices_list,
            "units": current_units,
            "Vertices": 4
        }
        
        self.settings_info_signal.emit(settings_info)

    