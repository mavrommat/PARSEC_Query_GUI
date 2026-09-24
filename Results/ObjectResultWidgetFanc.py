from PySide6.QtWidgets import QWidget, QMenu, QHBoxLayout
from PySide6.QtCore import Signal, Qt
from Results.ObjectResultWidgetUI import Ui_ObjectWidget
class ObjectResultWidget(QWidget):
    # Only emits the data payload now. The parent list will determine the routing string.
    request_view_signal = Signal(dict)
    
    def __init__(self, item_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_ObjectWidget()
        self.ui.setupUi(self)

        # Move the View Object button
        self.ui.gridLayout.addWidget(self.ui.B_view_obj, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight)
        self.ui.B_view_obj.setFixedSize(120, 32)
        
        self.item_data = item_data
        
        purplish_button_style = """
            QPushButton { 
                background-color: hsla(248, 24%, 42%, 180); 
                color: white; 
                border-radius: 4px; 
                padding: 6px 12px;
                border: 1px solid hsla(248, 24%, 60%, 150); 
            }
            QPushButton:hover { 
                background-color: hsla(248, 24%, 52%, 220); 
                border: 1px solid hsla(248, 24%, 70%, 200);
            }
            QPushButton:pressed {
                background-color: hsla(248, 24%, 32%, 255); 
                border: 1px solid hsla(248, 24%, 70%, 255);
            }
        """
        self.ui.main_gb.setStyleSheet(purplish_button_style)


        self.populate_data()
        self.ui.B_view_obj.clicked.connect(self.emit_view_request)

    def populate_data(self):
        obj = self.item_data.get("object", {})
        self.ui.id_code_label.setText(obj.get("object_id", "N/A"))
        self.ui.object_type_label.setText(obj.get("object_type", "N/A"))
        
        coords = obj.get("coordinates", {})
        ra = coords.get("ra", "N/A")
        dec = coords.get("dec", "N/A")
        frame = coords.get("frame", "N/A")
        self.ui.ra_dec_frame_label.setText(f"RA: {ra} | DEC: {dec} | Frame: {frame}")
        
        identifiers = obj.get("identifiers", [])
        names = ", ".join([f"{i.get('catalogue')}: {i.get('id')}" for i in identifiers[:2]]
    + ([f"... (+{len(identifiers) - 2} more)"] if len(identifiers) > 2 else []))
        self.ui.other_names_label.setText(names if names else "N/A")
        
        cats = obj.get("catalogues", [])
        meas_count = sum(len(c.get("measurements", [])) for c in cats)
        self.ui.measurements_sources_label.setText(f"{meas_count} Measurements - {len(cats)} Sources")

    def emit_view_request(self):
        # Signal the raw data up to Results_Objects to handle the routing string
        self.request_view_signal.emit(self.item_data)