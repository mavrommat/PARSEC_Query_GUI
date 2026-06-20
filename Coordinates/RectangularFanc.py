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

    def update_units_label(self, selected_units):
        # Update both unit labels to keep them in sync
        self.ui.width_units_label.setText(selected_units)
        self.ui.height_units_label.setText(selected_units)

    def pass_settings(self, checked=False):
        # Grab width and height from the new spinboxes
        rect_width = float(self.ui.width_sb.value())
        rect_height = float(self.ui.height_sb.value())
        
        # Grab the text directly from one of the visual labels
        current_units = self.ui.width_units_label.text()

        settings_info = {
            "Advanced": False,
            "Width": rect_width,
            "Height": rect_height,
            "Units": current_units,
            "Vertices": 4
        }
        
        self.validate_input_data(rect_width, rect_height, settings_info)
        

    def validate_input_data(self, rect_width, rect_height, settings_info):
        # Ensure both dimensions are strictly positive
        if rect_width <= 0 or rect_height <= 0:
            popup = ErrorPopup("Invalid Value", "Please enter width and height values > 0")
            popup.show_popup()
            return  # Stop the function from proceeding
        else:
            # Emit the data!
            self.settings_info_signal.emit(settings_info)