from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from Results.ObjectOverviewUI import Ui_ObjectOverview
from astropy.coordinates import SkyCoord
import astropy.units as u

class ObjectOverviewWidget(QWidget):
    navigate_signal = Signal(str, dict) 
    home_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ObjectOverview()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("OverviewWrapper")
        
        self.setStyleSheet("""
            QWidget#OverviewWrapper {
                background-color: hsla(0, 0%, 12%, 150); 
                border-radius: 8px;   
            }
            QGroupBox {
                background-color: transparent;
                border: none;
            }
            QLabel {
                color: white;
            }
            QScrollArea#identifiers_scroll_area {
                background-color: transparent;
                border: none;
            }
            QScrollArea#identifiers_scroll_area > QWidget > QWidget {
                background-color: transparent;
            }
            
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
            
            QPushButton#B_close { 
                background-color: hsla(0, 0%, 100%, 20); 
                color: #dddddd; 
                font-weight: bold; 
                border: 1px solid hsla(0, 0%, 100%, 40); 
            }
            QPushButton#B_close:hover { 
                background-color: hsla(0, 0%, 100%, 40); 
                color: white; 
                border: 1px solid hsla(0, 0%, 100%, 60); 
            }
            QPushButton#B_close:pressed {
                background-color: hsla(0, 0%, 100%, 10);
            }
        """)
        
        

        self.ui.B_close.clicked.connect(self.home_signal.emit)
        self.ui.format_cb.currentIndexChanged.connect(self.update_coordinates)
        self.ui.frame_cb.currentIndexChanged.connect(self.update_coordinates)
        self.ui.B_view_all.clicked.connect(self._on_view_all_clicked) 
        
        
        self.base_coords = None
        self.current_object_data = {} 

    def load_object_data(self, item_data):
        self.current_object_data = item_data.get("object", {})
        obj = self.current_object_data
        
        self.ui.ObjectId.setText(f"Object's ID: {obj.get('object_id', 'N/A')}")
        self.ui.object_type_label.setText(f"Object Type: {obj.get('object_type', 'N/A')}")
        
        id_scroll_contents = self.ui.identifiers_scroll_area.widget()
        if not id_scroll_contents.layout():
            id_scroll_contents.setLayout(QVBoxLayout())
        self.clear_layout(id_scroll_contents.layout())
        
        for ident in obj.get("identifiers", []):
            label_text = f"{ident.get('catalogue', 'Unknown')}: {ident.get('id', 'N/A')}"
            lbl = QLabel(label_text)
            id_scroll_contents.layout().addWidget(lbl)
        id_scroll_contents.layout().addStretch()
        
        coords = obj.get("coordinates", {})
        ra_str = coords.get("ra", "")
        dec_str = coords.get("dec", "")
        frame_str = coords.get("frame", "ICRS").lower()
        
        idx = self.ui.frame_cb.findText(frame_str, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchCaseSensitive)
        if idx >= 0:
            self.ui.frame_cb.blockSignals(True)
            self.ui.frame_cb.setCurrentIndex(idx)
            self.ui.frame_cb.blockSignals(False)

        try:
            unit = (u.hourangle, u.deg) if ":" in str(ra_str) else (u.deg, u.deg)
            self.base_coords = SkyCoord(ra=ra_str, dec=dec_str, frame=frame_str, unit=unit)
        except Exception as e:
            self.base_coords = None
            self.ui.ra_val.setText(str(ra_str))
            self.ui.dec_val.setText(str(dec_str))
        
        self.update_coordinates()
            
       #  Sources and Popular Measurements Population 
        cats = obj.get("catalogues", [])
        meas_count = sum(len(c.get("measurements", [])) for c in cats)
        self.ui.measurements_sources_label.setText(f"{meas_count} Measurements - {len(cats)} Sources")
        
        # Find the most popular measurements by Category AND Concept
        concept_counts = {}
        for cat in cats:
            for meas in cat.get("measurements", []):
                concept = meas.get("concept", "")
                category = meas.get("category", "") 
                
                combined_key = f"{category} - {concept}"
                concept_counts[combined_key] = concept_counts.get(combined_key, 0) + 1
                
        # Sort combined concepts by frequency
        sorted_concepts = sorted(concept_counts.items(), key=lambda x: x[1], reverse=True)
        
        meas_labels = [
            self.ui.c_f_s_label_1, self.ui.c_f_s_label_2, self.ui.c_f_s_label_3, 
            self.ui.c_f_s_label_4, self.ui.c_f_s_label_5, self.ui.c_f_s_label_6
        ]
        
        for i, label in enumerate(meas_labels):
            if i < len(sorted_concepts):
                # Unpack the combined string and the count
                combined_name, count = sorted_concepts[i]
                plural = "source" if count == 1 else "sources"
                label.setText(f"• {combined_name} (in {count} {plural})")
                label.show()
            else:
                label.hide() # Deactivate label if there are fewer than 6 measurements

        # Populate clickable source 
        sources_scroll_contents = self.ui.sources_scroll.widget()
        if not sources_scroll_contents.layout():
            sources_scroll_contents.setLayout(QVBoxLayout())
        self.clear_layout(sources_scroll_contents.layout())
        
        for i, cat in enumerate(cats):
            cat_name = cat.get('catalogue_name', f'Catalog {i+1}')
            cat_version = cat.get('catalogue_version', 'N/A')
            n_meas = len(cat.get('measurements', []))
            
            btn_text = f"{cat_name} ({cat_version}) - {n_meas} measurements"
            
            card_btn = QPushButton(btn_text)
            card_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            card_btn.setStyleSheet("""
                QPushButton {
                    background-color: hsla(0, 0%, 100%, 10);
                    color: white;
                    border-radius: 6px;
                    padding: 12px;
                    text-align: left;
                    border: 1px solid hsla(0, 0%, 100%, 20);
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: hsla(0, 0%, 100%, 20);
                    border: 1px solid hsla(0, 0%, 100%, 50);
                }
            """)
            
            card_btn.clicked.connect(lambda checked=False, c=cat: self.on_catalog_clicked(c))
            sources_scroll_contents.layout().addWidget(card_btn)
            
        sources_scroll_contents.layout().addStretch()

    def on_catalog_clicked(self, catalog_data):
        # Create a copy of the current object data 
        filtered_payload = dict(self.current_object_data)
        
        # Overwrite the catalogues list to ONLY contain the clicked catalog
        filtered_payload["catalogues"] = [catalog_data]
        
        self.navigate_signal.emit("Measurements", filtered_payload)

    def update_coordinates(self):
        if not self.base_coords:
            return
            
        target_frame = self.ui.frame_cb.currentText().lower()
        format_type = self.ui.format_cb.currentText()
        
        try:
            transformed_coords = self.base_coords.transform_to(target_frame)
        except Exception:
            transformed_coords = self.base_coords
            
        if target_frame == "galactic":
            lon_name = "Gal. l"
            lat_name = "Gal. b"
        else:
            lon_name = "RA"
            lat_name = "DEC"
            
        if "Sexagesimal" in format_type:
            ra_unit = u.hour if target_frame in ['icrs', 'fk5', 'fk4'] else u.degree
            ra_text = transformed_coords.spherical.lon.to_string(unit=ra_unit, sep=':', precision=2)
            dec_text = transformed_coords.spherical.lat.to_string(unit=u.degree, sep=':', precision=2, alwayssign=True)
            
            lon_unit_label = "(hms):" if ra_unit == u.hour else "(dms):"
            lat_unit_label = "(dms):"
        else: # Decimal degrees
            ra_text = f"{transformed_coords.spherical.lon.degree:.6f}"
            dec_text = f"{transformed_coords.spherical.lat.degree:+.6f}"
            
            lon_unit_label = "(deg):"
            lat_unit_label = "(deg):"
            
        self.ui.ra_val.setText(ra_text)
        self.ui.dec_val.setText(dec_text)
        self.ui.label_4.setText(f"{lon_name} {lon_unit_label}")
        self.ui.label_5.setText(f"{lat_name} {lat_unit_label}")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()


    def _on_view_all_clicked(self):
        if self.current_object_data:
            self.navigate_signal.emit("Measurements", self.current_object_data)