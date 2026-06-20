import json
import os
from PySide6.QtCore import QObject, Slot

class PayloadAggregator(QObject):
    def __init__(self):
        super().__init__()
        self.reset_payload()

    def reset_payload(self):
        self.payload = {
            "Databases": [],
            "Query_Mode": None,
            "Found_Object_IDs": [],
            
            "Advanced_Constraints": {},
            "Display_Options": {},
            "Bibliographic_Data": {}
        }

    @Slot(str)
    def update_main_query_type(self, query_type):
        self.payload["Query_Mode"] = query_type

    @Slot(list)
    def update_databases(self, databases):
        self.payload["Databases"] = databases

    @Slot(list)
    def update_found_ids(self, id_list):
        self.payload["Found_Object_IDs"] = id_list

    @Slot(dict)
    def update_constraints(self, constraints_data):
        self.payload["Advanced_Constraints"] = constraints_data

    @Slot(dict)
    def update_display_options(self, display_data):
        self.payload["Display_Options"] = display_data

    @Slot(dict)
    def update_bibliography(self, bib_data):
        self.payload["Bibliographic_Data"] = bib_data

    def get_clean_payload(self):
        clean_data = {
            "Databases": self.payload.get("Databases", []),
            "Query_Mode": self.payload.get("Query_Mode", ""),
            "Found_Object_IDs": self.payload.get("Found_Object_IDs", [])
        }
        
        for key in ["Advanced_Constraints", "Display_Options", "Bibliographic_Data"]:
            if self.payload.get(key):
                clean_data[key] = self.payload[key]

        return clean_data

    def generate_json_string(self):
        return json.dumps(self.get_clean_payload(), indent=4)

    def save_to_json_file(self, filename="master_query_payload.json"):
        cleaned_payload = self.get_clean_payload()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(cleaned_payload, f, indent=4)
            print(f"Successfully compiled and saved payload to {filename}")
        except Exception as e:
            print(f"Failed to save JSON payload: {e}")