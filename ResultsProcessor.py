# -*- coding: utf-8 -*-
import json
import os
from PySide6.QtCore import QObject, Signal

class ResultsProcessor(QObject):
    # Emits the fully structured list of dictionaries for the UI to render
    Processed_data_signal = Signal(list)

    def __init__(self):
        super().__init__()
        self.master_results = []      # The untouched master dataset
        self.current_view_data = []   # The actively sorted/filtered dataset

    def load_from_json(self, filepath):
        """Loads and structures data from a local JSON mockup."""
        try:
            if not os.path.exists(filepath):
                print(f"Processor Error: File '{filepath}' not found.")
                return
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Extract root array and store state
            self.master_results = data.get("results", [])
            self.current_view_data = self.master_results.copy()
            
            # Dispatch to the UI
            self.Processed_data_signal.emit(self.current_view_data)
        except Exception as e:
            print(f"Processor Error loading JSON: {e}")

    def apply_sort(self, sort_key):
        # Sort the cards based on the input
        if not self.current_view_data:
            return

        if sort_key == "Object ID":
            self.current_view_data.sort(
                key=lambda x: x.get("object", {}).get("object_id", "").lower()
            )
        elif sort_key == "RA (Coordinates)":
            self.current_view_data.sort(
                key=lambda x: x.get("object", {}).get("coordinates", {}).get("ra", "")
            )
        
        # Broadcast to ResultsObjectsFanc
        self.Processed_data_signal.emit(self.current_view_data)

    def process_dataframes(self, df_list):
        """
        Transforms raw Pandas DataFrames into the nested hierarchical dictionary.
        Will replace load_from_json when executing real queries via main.py.
        """
        structured_payload = []
        
        # TODO: Implement DataFrame grouping logic here. 
        # Example flow:
        # 1. Group by object_id
        # 2. Nest catalogues and measurements inside the object dict
        # 3. Append to structured_payload
        
        self.master_results = structured_payload
        self.current_view_data = self.master_results.copy()
        self.Processed_data_signal.emit(self.current_view_data)