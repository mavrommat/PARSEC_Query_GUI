from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from Results.SourcesMeasurementsUI import Ui_ConceptMeasurements 
from Results.MeasurementViewWidget import Ui_IndividualMeasurement 
from Results.SingleMeasurementFanc import SingleMeasurementWidget

class AllMeasurementsWidget(QWidget):
    back_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConceptMeasurements()
        self.ui.setupUi(self)
        
        self.setObjectName("SearchWrapper")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            QWidget#SearchWrapper { 
                background-color: hsla(0, 0%, 12%, 150); 
                border-radius: 8px; 
            }
            QScrollArea { border: none; background: transparent; }
            QWidget#scrollAreaWidgetContents { background: transparent; }
            QGroupBox#caterory_concept_gb { border: none; background: transparent; }
            QLabel { color: white; font-size: 14px; }
            
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
        """)
        
        self.current_object_data = None
        self.concept_map = {}

    def load_measurements(self, object_data):       
        self.current_object_data = object_data
        self.concept_map = {}
        
        # Parse standard concepts while preserving the full measurement dictionary
        cats = object_data.get("catalogues", [])
        for cat in cats:
            source_name = cat.get("catalogue_name", "Unknown Source")
            for meas in cat.get("measurements", []):
                concept = meas.get("concept", "Unknown")
                category = meas.get("category", "Default") 
                
                sort_key = f"{category}_{concept}"
                
                if sort_key not in self.concept_map:
                    self.concept_map[sort_key] = {
                        "category": category,
                        "concept": concept,
                        "sources": {}
                    }
                
                if source_name not in self.concept_map[sort_key]["sources"]:
                    self.concept_map[sort_key]["sources"][source_name] = []
                    
                self.concept_map[sort_key]["sources"][source_name].append(meas)

        self.render_az_preview()

    def render_az_preview(self):
        """State 1: Renders the A-Z list of available concepts."""
        try: self.ui.B_back.clicked.disconnect()
        except: pass
        
        self.ui.B_back.setText("Back to Overview")
        self.ui.B_back.clicked.connect(self.back_signal.emit)
        
        obj_id = self.current_object_data.get("object_id", "Unknown ID")
        
        self.ui.category_label.setText(f"Object: {obj_id}")
        self.ui.concept_label.setText("All Available Measurements (A-Z)")
        
        scroll_contents = self.ui.catalogs_scroll_area.widget()
        if not scroll_contents.layout():
            scroll_contents.setLayout(QVBoxLayout())
            scroll_contents.layout().setContentsMargins(0, 0, 0, 0)
            scroll_contents.layout().setSpacing(8)
            
        self.clear_layout(scroll_contents.layout())
        
        sorted_keys = sorted(self.concept_map.keys())
        for key in sorted_keys:
            data = self.concept_map[key]
            
            card_widget = QWidget()
            card_ui = Ui_IndividualMeasurement()
            card_ui.setupUi(card_widget)
            card_widget.setStyleSheet("QWidget { background: transparent; }")
            
            card_ui.category_feature_label.setText(f"{data['category']} - {data['concept']}")
            
            n_sources = len(data['sources'])
            card_ui.sources_label.setText(f"{n_sources} source" if n_sources == 1 else f"{n_sources} sources")
            
            card_ui.main_gb.setStyleSheet("""
                QGroupBox { 
                    background-color: transparent; 
                    border: none;
                    border-bottom: 1px solid hsla(0, 0%, 100%, 20); /* Subtle separator line */
                    border-radius: 0px; 
                }
            """)
            
            # Catch the B_view_measurements signal and drill down into the specific concept
            card_ui.B_view_measurements.clicked.connect(
                lambda checked=False, k=key: self.render_concept_measurements(k)
            )
            
            scroll_contents.layout().addWidget(card_widget)
            
        scroll_contents.layout().addStretch()

    def render_concept_measurements(self, concept_key):
        """State 2: Renders individual measurements grouped by catalog for the selected concept."""
        data = self.concept_map[concept_key]
        
        try: self.ui.B_back.clicked.disconnect()
        except: pass
        
        self.ui.B_back.setText("Back to Concepts")
        self.ui.B_back.clicked.connect(self.render_az_preview)
        
        self.ui.concept_label.setText(f"Viewing: {data['category']} - {data['concept']}")
        
        scroll_contents = self.ui.catalogs_scroll_area.widget()
        self.clear_layout(scroll_contents.layout())
        
        for source_name, measurements in data['sources'].items():
            header = QLabel(f"<h3 style='color: #a0a0ff; margin-top: 10px; margin-bottom: 2px;'>{source_name}</h3>")
            scroll_contents.layout().addWidget(header)
            
            for meas in measurements:
                meas_widget = SingleMeasurementWidget(meas)
                scroll_contents.layout().addWidget(meas_widget)
                
        scroll_contents.layout().addStretch()

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()