# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Results.SingleMeasurementUI import Ui_SingleMeasurement
from Results.MeasurementDetailsFanc import MeasurementDetailsWidget

class SingleMeasurementWidget(QWidget):
    def __init__(self, meas_data, parent=None):
        super().__init__(parent)
        self.meas_data = meas_data
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)
        
        self.main_card = QWidget()
        self.ui = Ui_SingleMeasurement()
        self.ui.setupUi(self.main_card)
        
        # Apply the app-standard transparent styling
        self.ui.groupBox.setStyleSheet("""
            QGroupBox { 
                background-color: transparent; 
                border: none;
                border-bottom: 1px solid hsla(0, 0%, 100%, 20);
                padding-bottom: 8px;
            }
            QLabel { color: white; background: transparent; }
        """)
        
        self.ui.value.setText(str(meas_data.get("value", "N/A")))
        self.ui.units.setText(str(meas_data.get("unit", "N/A")))
        self.ui.characterisation.setText(str(meas_data.get("characterisation", "N/A")))
        
        aux_list = meas_data.get("auxiliary", [])
        aux_text = ", ".join([f"{a.get('concept')} = {a.get('value')}" for a in aux_list]) if aux_list else "None"
        self.ui.auxiliary.setText(aux_text)
        
        self.layout.addWidget(self.main_card)
        self.details_card = None
        
        self.ui.B_details.clicked.connect(self.toggle_details)

    def toggle_details(self):
        """Spawns the detail card if it doesn't exist, or toggles its visibility."""
        if self.details_card is None:
            self.details_card = MeasurementDetailsWidget(self.meas_data)
            self.layout.addWidget(self.details_card)
        elif self.details_card.isHidden():
            self.details_card.show()
        else:
            self.details_card.hide()