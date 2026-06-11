import os
import json
import socket
import threading
import http.server
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
from PySide6.QtCore import Qt, Signal, QObject, Slot, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PySide6.QtWebChannel import QWebChannel
from astropy.coordinates import SkyCoord
import astropy.units as u

from Coordinates.ManualCoordsUI import Ui_ManualCoords
from ErrorPopUp import ErrorPopup


class DebugWebPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, line, sourceID):
        print(f"MAP JS ERROR: {message} (Line {line})")


class MapBridge(QObject):
    coordinate_clicked = Signal(float, float)
    delete_requested = Signal()

    @Slot(float, float)
    def receive_click(self, ra, dec):
        self.coordinate_clicked.emit(ra, dec)

    @Slot()
    def request_delete_last(self):
        """Triggered by Javascript 'X' keypress"""
        self.delete_requested.emit()


class DrawOnSky(QWidget):
    settings_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()

        self.ui_widget = QWidget()
        self.ui = Ui_ManualCoords()
        self.ui.setupUi(self.ui_widget)

        #  Lock the Frame and Units  
        self.ui.frame_cb.setEnabled(False)
        self.ui.units_cb.setEnabled(False)

        # 2. instructions
        instruction_text = "Instructions: Point at a sky region and press Shift+Q to add a vertex. To delete the last vertex, press Shift+X. Do not change frame or units while using the map."
        self.instruction_label = QLabel(instruction_text)
        self.instruction_label.setWordWrap(True)
        self.instruction_label.setStyleSheet("color: white; font-weight: bold; margin-top: 10px;")
        self.ui.gridLayout_2.addWidget(self.instruction_label, 4, 0, 1, 1)

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

        # 2. Map Integration 
        self.browser = QWebEngineView()
        self.debug_page = DebugWebPage(self.browser)
        self.browser.setPage(self.debug_page)
        
        # Web Engine Settings
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.bridge = MapBridge()
        self.channel = QWebChannel()
        self.channel.registerObject("backend", self.bridge)
        self.browser.page().setWebChannel(self.channel)
        
        # Local Background Web Server
        self.start_local_server()
        
        # Browser to new local server
        map_url = f"http://localhost:{self.port}/aladin_map.html"
        print(f"Loading map from local server: {map_url}")
        self.browser.setUrl(QUrl(map_url))

        # 3. Main Layout Construction
        main_layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.browser) 
        splitter.addWidget(self.ui_widget) 
        splitter.setStretchFactor(0, 7) #70%
        splitter.setStretchFactor(1, 3) # 30%
        main_layout.addWidget(splitter)

        # 4. Signal Connections 
        self.ui.frame_cb.currentTextChanged.connect(self.update_coordinate_headers)
        self.ui.B_add_vertex.clicked.connect(self.add_blank_vertex_row)
        self.ui.B_del_vertex.clicked.connect(self.remove_vertex_row)
        self.ui.B_submit_shape.clicked.connect(self.submit_data)

        # 5. Signal Connections  JS and Python
        self.bridge.coordinate_clicked.connect(self.add_vertex_from_map)
        self.bridge.delete_requested.connect(self.remove_vertex_row)

        # 6. Initialize logic
        self.update_coordinate_headers(self.ui.frame_cb.currentText())
        self.ui.Coordinates_Table.setRowCount(0) 
        
        self.browser.loadFinished.connect(lambda ok: self.sync_map_to_table() if ok else None) # sync the map after HTML finishes loading
    
    def start_local_server(self):        
        directory = os.path.abspath("Coordinates")
        
        class SilentHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=directory, **kwargs)
            
            def log_message(self, format, *args): # Suppress terminal spam 
                pass 

        # dynamic check of port availability 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            self.port = s.getsockname()[1]

        # Spin up the server in a background thread (daemon=True ensures it dies when your app closes)
        self.httpd = http.server.HTTPServer(("", self.port), SilentHandler)
        self.server_thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.server_thread.start()

    # =========================================================
    # MAP DRAWING LOGIC
    # =========================================================

    def sync_map_to_table(self):
        table = self.ui.Coordinates_Table
        coords_list = []
        
        for row in range(table.rowCount()):
            item_c1 = table.item(row, 0)
            item_c2 = table.item(row, 1)
            
            if item_c1 and item_c2 and item_c1.text().strip() and item_c2.text().strip():
                try:
                    ra = float(item_c1.text())
                    dec = float(item_c2.text())
                    coords_list.append([ra, dec])
                except ValueError:
                    continue 
                    
        js_data = json.dumps(coords_list)
        
        # Ensure the JS function actually exists 
        js_call = f"if (typeof window.updatePolygon === 'function') {{ window.updatePolygon({js_data}); }}"
        self.browser.page().runJavaScript(js_call)

    
    # ADD / REMOVE VERTEX LOGIC
    def add_vertex_from_map(self, ra, dec): # Shift+Q click or Add Vertex
        table = self.ui.Coordinates_Table
        current_rows = table.rowCount()
        table.insertRow(current_rows)

        # Populate with 5 decimal places
        table.setItem(current_rows, 0, QTableWidgetItem(f"{ra:.5f}"))
        table.setItem(current_rows, 1, QTableWidgetItem(f"{dec:.5f}"))
        table.setItem(current_rows, 2, QTableWidgetItem("1"))
        table.setItem(current_rows, 3, QTableWidgetItem(str(current_rows + 1)))
        
        self.refresh_order_column()
        self.sync_map_to_table()

    def add_blank_vertex_row(self):
        table = self.ui.Coordinates_Table
        current_rows = table.rowCount()
        table.insertRow(current_rows)
        
        table.setItem(current_rows, 2, QTableWidgetItem("1"))
        table.setItem(current_rows, 3, QTableWidgetItem(str(current_rows + 1)))
        
        self.refresh_order_column()
        self.sync_map_to_table()

    def remove_vertex_row(self): # SHift+X click or Delete Vertex
        table = self.ui.Coordinates_Table
        current_rows = table.rowCount()

        if current_rows <= 0:
            return # Nothing to delete
            
        table.removeRow(current_rows - 1)
        self.refresh_order_column()
        self.sync_map_to_table()

    def refresh_order_column(self):
        table = self.ui.Coordinates_Table
        for row in range(table.rowCount()):
            table.setVerticalHeaderItem(row, QTableWidgetItem(f"Coordinates #{row + 1}"))
            table.setItem(row, 3, QTableWidgetItem(str(row + 1)))


    def update_coordinate_headers(self, frame_name):
        if frame_name in ["ICRS", "FK5", "FK4"]:
            col1, col2 = "RA", "DEC"
        elif frame_name == "Galactic":
            col1, col2 = "l", "b"
        elif frame_name == "Barycentric True Ecliptic":
            col1, col2 = "Longitude", "Latitude"
        else:
            col1, col2 = "Lon", "Lat"

        self.ui.Coordinates_Table.horizontalHeaderItem(0).setText(col1)
        self.ui.Coordinates_Table.horizontalHeaderItem(1).setText(col2)

  

    def validate_and_get_coordinates(self): # Validate the data using Astropy
        table = self.ui.Coordinates_Table
        valid_coordinates = []
        
        ui_frame = self.ui.frame_cb.currentText()
        frame_mapping = {
            "ICRS": "icrs", "FK5": "fk5", "FK4": "fk4",
            "Galactic": "galactic", "Barycentric True Ecliptic": "barycentrictrueecliptic"
        }
        astropy_frame = frame_mapping.get(ui_frame, "icrs")

        ui_unit = self.ui.units_cb.currentText()
        unit_mapping = {"Degrees": "deg", "Arcseconds": "arcsec", "Arcminutes": "arcmin"}
        astropy_unit = unit_mapping.get(ui_unit, "deg")

        if table.rowCount() < 3:
            self._show_error("Minimum Vertices", "A polygon requires at least 3 vertices to submit.")
            return False

        for row in range(table.rowCount()):
            item_c1 = table.item(row, 0)
            item_c2 = table.item(row, 1)

            if not item_c1 or not item_c1.text().strip():
                self._show_error("Missing Data", f"Row {row + 1} is missing the first coordinate.")
                return False
            if not item_c2 or not item_c2.text().strip():
                self._show_error("Missing Data", f"Row {row + 1} is missing the second coordinate.")
                return False

            try:
                coord = SkyCoord(item_c1.text().strip(), item_c2.text().strip(), frame=astropy_frame, unit=astropy_unit)
                c1_val = coord.spherical.lon.deg
                c2_val = coord.spherical.lat.deg
            except ValueError as e:
                self._show_error("Astropy Validation Error", f"Row {row + 1} contains an invalid format.\n\nDetails: {str(e)}")
                return False

            active_item = table.item(row, 2)
            active_state = active_item.text().strip() if active_item else "1"

            valid_coordinates.append({
                "c1": c1_val, "c2": c2_val,
                "active": active_state, "order": row + 1
            })

        return valid_coordinates

    def _show_error(self, title, message):
        popup = ErrorPopup(title, message, parent=self)
        popup.show_popup()

    def submit_data(self):
        coords = self.validate_and_get_coordinates()
        if coords is False: return 
            
        submission_data = {
            "Target": "Interactive Map",
            "Shape": "Custom Polygon",
            "Distance": str(len(coords)), 
            "Units": self.ui.units_cb.currentText(), 
            "frame": self.ui.frame_cb.currentText(),
            "input_units": self.ui.units_cb.currentText(),
            "coordinates": coords
        }
        
        self.settings_info_signal.emit(submission_data)
        print("Coordinates successfully mapped, verified, and submitted!")