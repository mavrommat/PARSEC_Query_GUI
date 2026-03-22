from PySide6.QtWidgets import QWidget
from Coordinates.PolygonUI import Ui_Polygon
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup 

class Polygon(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        
        # Attach the blueprint
        self.ui = Ui_Polygon()
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
        poly_dist = self.ui.polyg_hypot_sb.value()
        poly_dist = float(poly_dist)

        vertices = self.ui.vertices_sb.value()
        vertices = int(vertices)

        # Grab the text directly from the visual label!
        current_units = self.ui.units_label.text()

        settings_info = {
            "Advanced": False,
            "Distance": poly_dist,
            "Units": current_units,
            "Vertices": vertices
            }
        
        self.validate_input_data(poly_dist, vertices, settings_info)
        

    def validate_input_data(self, poly_dist, vertices, settings_info):
        if poly_dist <= 0:
            popup = ErrorPopup("Unvalid Value", "Please enter a angular value > 0")
            popup.show_popup()
            return  # Stop the function from proceeding
        elif vertices == 4 or vertices <= 2:
            popup = ErrorPopup("Unvalid Value", "Please enter vertices > 2 and not 4")
            popup.show_popup()
            return  # Stop the function from proceeding

        elif poly_dist > 0 and (vertices >= 2 and vertices != 4):
            # Emit the data!
            self.settings_info_signal.emit(settings_info)


    