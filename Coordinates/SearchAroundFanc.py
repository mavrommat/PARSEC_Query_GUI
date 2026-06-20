import pandas as pd
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PySide6.QtCore import Qt, Signal
from Coordinates.SearchAroundUI import Ui_SearchAround
from ErrorPopUp import ErrorPopup 

from Coordinates.RadiusFanc import Radius
from Coordinates.RectangularFanc import Rectagular
from Coordinates.PolygonFanc import Polygon

from Coordinates.Resolver import ObjectResolver

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

        # Read the database file into a pandas DataFrame first
        try:
            df = pd.read_parquet("Database/astro_10k.parquet")
            self.Resolver = ObjectResolver(df=df)
        except Exception as e:
            print(f"Failed to load database: {e}")
            # You might want to trigger an ErrorPopup here if the file is missing!

        self.ui.B_Radius_Search.clicked.connect(self.broadcast_selection)
        self.ui.B_Rect_Search.clicked.connect(self.broadcast_selection)
        self.ui.B_polyg_Search.clicked.connect(self.broadcast_selection)

        self.ui.B_resolved.clicked.connect(self.resolver_process)

        # Add an instance variable to remember the target/frame/epoch settings
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

        # Pushing the unit text to the child widgets 
        self.Radius.ui.units_label.setText(units_choice)
        
        # Using the exact UI element names we set up earlier
        self.Rectangle.ui.width_units_label.setText(units_choice)
        self.Rectangle.ui.height_units_label.setText(units_choice)
        self.Polygon.ui.side_units_label.setText(units_choice)
        
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
        if coords_id_input.strip() == "":
            popup = ErrorPopup("Empty target", "Please enter a target")
            popup.show_popup()
            return  
        
        # Attempt to resolve the object before proceeding to search shapes
        try:
            payload = self.Resolver.resolve(coords_id_input)
            self.display_resolved_payload(payload)
            
            # GATE: If not resolved, we stop here and do not proceed to the search
            if payload.get("status") == "Not Found":
                return 
                
        except Exception as e:
            popup = ErrorPopup("Resolver Error", f"An error occurred: {str(e)}")
            popup.show_popup()
            return

        # Emit the data to proceed to the shape search options.
        self.Sub_Sub_coord_signal.emit(info_settings["Shape"])

    def shape_info_process(self, settings_info):
        # Base settings from the main panel
        CoordsQuerySelections = {
            "Target": self.current_info_settings.get("Target", "N/A"),
            "Shape": self.current_info_settings.get("Shape", "N/A"),
            "Units": self.current_info_settings.get("Units", ""),       
            "Frame": self.current_info_settings.get("Frame", "N/A"),
            "Epoch": self.current_info_settings.get("Epoch", "N/A"),
            "Equinox": self.current_info_settings.get("Equinox", "N/A")
        }

        # --- DYNAMICALLY append the parameters based on the incoming dictionary ---
        
        # From Radius
        if "Distance" in settings_info:
            CoordsQuerySelections["Distance"] = settings_info["Distance"]
            
        # From Rectangle
        if "Width" in settings_info and "Height" in settings_info:
            CoordsQuerySelections["Width"] = settings_info["Width"]
            CoordsQuerySelections["Height"] = settings_info["Height"]
            
        # From Polygon
        if "Side_Length" in settings_info:
            CoordsQuerySelections["Side_Length"] = settings_info["Side_Length"]
            
        # From Polygon and Rectangle
        if "Vertices" in settings_info:
            CoordsQuerySelections["Vertices"] = settings_info["Vertices"]

        print(f"Broadcasting Final Selection: {CoordsQuerySelections}")
            
        self.final_coords_query_signal.emit(CoordsQuerySelections)
    
    def resolver_process(self):
        input_text = self.ui.coords_id_input.text().strip()

        if not input_text:
            popup = ErrorPopup("Empty Input", "Please enter a target or coordinates to resolve.")
            popup.show_popup()
            return

        try:
            payload = self.Resolver.resolve(input_text)
        except Exception as e:
            popup = ErrorPopup("Resolver Error", f"An error occurred: {str(e)}")
            popup.show_popup()
            return

        # Update the UI with the payload data
        self.display_resolved_payload(payload)

    def display_resolved_payload(self, payload):
        """Clears the old output and displays the new resolved payload dynamically with aligned columns."""
        layout = self.ui.verticalLayout_resolved

        # Clear any existing widgets from previous searches
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

        # Handle 'Not Found' status
        if payload.get("status") == "Not Found":
            error_label = QLabel(f"Could not resolve: '{payload.get('search_term')}'")
            error_label.setStyleSheet("color: #ff4c4c; font-weight: bold;") # Red text
            layout.addWidget(error_label)
            return

        # --- Create a Grid Layout for aligned tabular data ---
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setHorizontalSpacing(15) # Space between Title and Value columns
        grid_layout.setVerticalSpacing(8)

        # Helper function to easily add rows to our grid
        def add_aligned_row(row_idx, title, value, value_color="white"):
            title_lbl = QLabel(title)
            title_lbl.setStyleSheet("color: #aaaaaa; font-weight: bold;") 
            val_lbl = QLabel(value)
            val_lbl.setStyleSheet(f"color: {value_color}; font-weight: bold;")
            
            # Align title to the right, value to the left
            grid_layout.addWidget(title_lbl, row_idx, 0, Qt.AlignmentFlag.AlignRight)
            grid_layout.addWidget(val_lbl, row_idx, 1, Qt.AlignmentFlag.AlignLeft)

        # 1. Status
        add_aligned_row(0, "Status:", "Resolved", "#4CAF50")
        row = 1

        # 2. Display Object ID if it exists
        obj_id = payload.get("object_id")
        if obj_id is not None:
            add_aligned_row(row, "Object ID:", str(obj_id))
            row += 1

        # 3. Display ICRS Equatorial Coordinates
        icrs = payload.get("icrs_equatorial")
        if icrs:
            val_str = f"RA {icrs.get('ra_hms')} | DEC {icrs.get('dec_dms')}  ({icrs.get('ra_deg'):.4f}°, {icrs.get('dec_deg'):.4f}°)"
            add_aligned_row(row, "ICRS:", val_str)
            row += 1

        # 4. Display Galactic Coordinates
        gal = payload.get("galactic")
        if gal:
            val_str = f"l {gal.get('l_deg'):.4f}° | b {gal.get('b_deg'):.4f}°"
            add_aligned_row(row, "Galactic:", val_str)
            row += 1

        # 5. Display Ecliptic Coordinates
        ecl = payload.get("ecliptic")
        if ecl:
            val_str = f"lon {ecl.get('lon_deg'):.4f}° | lat {ecl.get('lat_deg'):.4f}°"
            add_aligned_row(row, "Ecliptic:", val_str)

        # Add the fully populated grid widget to the main vertical layout
        layout.addWidget(grid_widget)