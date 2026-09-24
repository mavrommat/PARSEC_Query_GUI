# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget
from Results.MeasurementDetails import Ui_MeasurementDetails

class MeasurementDetailsWidget(QWidget):
    def __init__(self, meas_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_MeasurementDetails()
        self.ui.setupUi(self)
        
        self.ui.main_gb.setStyleSheet("""
            QGroupBox { 
                background-color: hsla(248, 24%, 32%, 180); 
                border-radius: 6px; 
                border: 1px solid hsla(248, 24%, 60%, 100);
            }
            QLabel { color: #dddddd; background: transparent; }
        """)
        
        # Populate raw metadata
        self.ui.raw_value.setText(str(meas_data.get("raw_value", "N/A")))
        self.ui.raw_units.setText(str(meas_data.get("raw_unit", "N/A")))
        self.ui.table_name.setText(str(meas_data.get("table_name", "N/A")))
        self.ui.col_name.setText(str(meas_data.get("column_name", "N/A")))
        self.ui.col_descr.setText(str(meas_data.get("column_description", "N/A")))
        
        # close button to collapse widget
        self.ui.B_close_details.clicked.connect(self.hide)