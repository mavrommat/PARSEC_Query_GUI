from PySide6.QtWidgets import QWidget, QTableWidgetItem
from Coordinates.ManualCoordsUI import Ui_ManualCoords
from PySide6.QtCore import Qt, Signal
from ErrorPopUp import ErrorPopup
from astropy.coordinates import SkyCoord
import astropy.units as u

class ManualCoords(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()

        # Attach the blueprint
        self.ui = Ui_ManualCoords()
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

        # SIGNAL CONNECTIONS
        # Change coordinate labels when frame changes
        self.ui.frame_cb.currentTextChanged.connect(self.update_coordinate_headers)

        self.ui.B_add_vertex.clicked.connect(self.add_vertex_row) # Add/remove rows
        self.ui.B_del_vertex.clicked.connect(self.remove_vertex_row)

        self.update_coordinate_headers(self.ui.frame_cb.currentText()) # Initialize headers
        self.refresh_order_column() # Initialize order column

        self.ui.B_submit_shape.clicked.connect(self.submit_data)


    def update_coordinate_headers(self, frame_name):
        if frame_name in ["ICRS", "FK5", "FK4"]:
            col1 = "RA"
            col2 = "DEC"

        elif frame_name == "Galactic":
            col1 = "l"
            col2 = "b"

        elif frame_name == "Barycentric True Ecliptic":
            col1 = "Longitude"
            col2 = "Latitude"

        else:
            col1 = "Lon"
            col2 = "Lat"

        self.ui.Coordinates_Table.horizontalHeaderItem(0).setText(col1)
        self.ui.Coordinates_Table.horizontalHeaderItem(1).setText(col2)


    def add_vertex_row(self):
        table = self.ui.Coordinates_Table

        current_rows = table.rowCount()

        table.insertRow(current_rows)

        # Vertical label
        table.setVerticalHeaderItem(current_rows,QTableWidgetItem(f"Coordinates #{current_rows + 1}"))

        # Default active state
        table.setItem(current_rows, 2, QTableWidgetItem("1"))

        # Order column
        table.setItem(current_rows, 3, QTableWidgetItem(str(current_rows + 1)))


    def remove_vertex_row(self):
        table = self.ui.Coordinates_Table

        current_rows = table.rowCount()

        # minimum polygon size
        if current_rows <= 3:
            popup = ErrorPopup(
                "Minimum Vertices",
                "A polygon requires at least 3 vertices."
            )
            popup.show_popup()
            return

        table.removeRow(current_rows - 1)

        self.refresh_order_column()


    def refresh_order_column(self):
        table = self.ui.Coordinates_Table

        for row in range(table.rowCount()):

            # Vertical labels
            table.setVerticalHeaderItem(row, QTableWidgetItem(f"Coordinates #{row + 1}"))

            # Order column
            table.setItem(row, 3, QTableWidgetItem(str(row + 1)))


    def validate_and_get_coordinates(self):
        table = self.ui.Coordinates_Table
        valid_coordinates = []
        
        # 1. Map UI dropdown names to Astropy frame strings
        ui_frame = self.ui.frame_cb.currentText()
        frame_mapping = {
            "ICRS": "icrs",
            "FK5": "fk5",
            "FK4": "fk4",
            "Galactic": "galactic",
            "Barycentric True Ecliptic": "barycentrictrueecliptic"
        }
        astropy_frame = frame_mapping.get(ui_frame, "icrs") # Default to icrs just in case

        # Map UI dropdown names to Astropy unit strings
        ui_unit = self.ui.units_cb.currentText()
        unit_mapping = {
            "Degrees": "deg",
            "Arcseconds": "arcsec",
            "Arcminutes": "arcmin"
        }
        astropy_unit = unit_mapping.get(ui_unit, "deg") # Default to deg just in case

        for row in range(table.rowCount()):
            item_c1 = table.item(row, 0)
            item_c2 = table.item(row, 1)

            # 2. Check for empty cells
            if not item_c1 or not item_c1.text().strip():
                self._show_error("Missing Data", f"Row {row + 1} is missing the first coordinate.")
                return False
            
            if not item_c2 or not item_c2.text().strip():
                self._show_error("Missing Data", f"Row {row + 1} is missing the second coordinate.")
                return False

            c1_text = item_c1.text().strip()
            c2_text = item_c2.text().strip()

            # Validate using Astropy SkyCoord
            try:
                # dynamic astropy_unit 
                coord = SkyCoord(c1_text, c2_text, frame=astropy_frame, unit=astropy_unit)
                
                c1_val = coord.spherical.lon.deg
                c2_val = coord.spherical.lat.deg
                
            except ValueError as e:
                self._show_error(
                    "Astropy Validation Error", 
                    f"Row {row + 1} contains an invalid format.\n\nDetails: {str(e)}"
                )
                return False

            # 4. Package the valid data
            active_item = table.item(row, 2)
            active_state = active_item.text().strip() if active_item else "1"

            valid_coordinates.append({
                "c1": c1_val,
                "c2": c2_val,
                "active": active_state,
                "order": row + 1
            })

        return valid_coordinates

    def _show_error(self, title, message):
        popup = ErrorPopup(title, message, parent=self)
        popup.show_popup()

    def submit_data(self):
        coords = self.validate_and_get_coordinates()
        
        if coords is False:
            return 
            
        submission_data = {
            "Target": "Manual Entry",
            "Shape": "Custom Polygon",
            "Distance": str(len(coords)), # Shows vertex count instead of distance
            "Units": self.ui.units_cb.currentText(), 
            "frame": self.ui.frame_cb.currentText(),
            "input_units": self.ui.units_cb.currentText(), # Optional: Explicitly tell backend what units were typed
            "coordinates": coords # Note: These are converted to decimal degrees by Astropy!
        }
        
        self.settings_info_signal.emit(submission_data)
        print("Coordinates successfully verified by Astropy and submitted!")