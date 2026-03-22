from PySide6.QtWidgets import QWidget
from Coordinates.AdvancedCustomUI import Ui_AdvancedCustom
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 
import re

class AdvancedCustom(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_AdvancedCustom()
        self.ui.setupUi(self)

        self.ui.custom_coords_input.setPlaceholderText("(RA1,DEC1),(RA2,DEC2),...,(RAn,DECn)")
        
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
        raw_vertices = self.ui.custom_coords_input.text().strip()

        # RegEx to extract the pairs (number, number) 
        matches = re.findall(r'\(\s*([+-]?\d*\.?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*\)', raw_vertices)

        if len(matches) < 2:
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
            "Advanced": True,
            "Distance": vertices_list,
            "Units": current_units,
            "Vertices": len(vertices_list)
        }
        
        self.settings_info_signal.emit(settings_info)