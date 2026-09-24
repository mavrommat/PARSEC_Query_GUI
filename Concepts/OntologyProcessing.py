import json
import requests
from collections import defaultdict

from PySide6.QtWidgets import QMenu, QToolButton
from PySide6.QtGui import QAction


class OntologyParser:
    # Explicitly define valid auxiliary concepts 
    VALID_AUXILIARY = {
        "_chi-square", "_CI_error", "_CI_lower_error", "_CI_upper_error", 
        "_comment", "_errorflag", "_lower_error", "_method", 
        "_normalization", "_provenance", "_reliability", 
        "_signal_to_noise_ratio", "_stDev", "_upper_error"
    }

    def __init__(
        self, 
        file_path="Concepts/data/concepts/concepts_for_metadata.json", 
        url="http://139.91.183.61:8000/concepts",
        offline_api_file="Concepts/offline_API_ontology.json"
    ):
        self.file_path = file_path
        self.url = url
        self.offline_api_file = offline_api_file
        self._category_dict = defaultdict(dict)

    def build_dictionary(self):
        # Clear dictionary
        self._category_dict.clear()
        
        # 1. Fetch Units from API or fallback to offline API file
        unit_map = {}
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            api_data = response.json()
            
            print(f"Downloaded {len(api_data)} concepts from API for units.")
            for item in api_data:
                name = item.get("Name", "").strip()
                if name:
                    unit_map[name] = item.get("Unit", [])
                    
        except Exception as e:
            print(f"API failed to fetch units: {e}")
            print(f"Attempting to load offline units from {self.offline_api_file}...")
            
            try:
                with open(self.offline_api_file, mode='r', encoding='utf-8') as offline_file:
                    offline_data = json.load(offline_file)
                    print(f"Loaded {len(offline_data)} concepts from offline file for units.")
                    for item in offline_data:
                        name = item.get("Name", "").strip()
                        if name:
                            unit_map[name] = item.get("Unit", [])
            except Exception as fallback_error:
                print(f"Failed to load offline units file: {fallback_error}")

        # 2. Read Concepts from the main local metadata JSON structure
        if not self.file_path:
            raise ValueError("No main metadata JSON file path provided.")

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                self._parse_data(data, unit_map)
                print(f"Loaded {len(data)} concepts from main local JSON.")
                
        except Exception as e:
            print(f"Failed to load main local JSON file: {e}")

        return dict(self._category_dict)
        
    def _parse_data(self, data, unit_map):
        for item in data:
            feature = item.get("Name", "").strip()

            if not feature:
                continue

            categories = item.get("Categories", [])
            if not categories:
                categories = ["Unknown"]

            char_dicts = item.get("Characterizations", [])
            characterizations = [c.get("name") for c in char_dicts if c.get("name")]

            is_aux = "Yes" if feature in self.VALID_AUXILIARY else "No"

            # Inject Units from the unit map (API or Offline File)
            units = unit_map.get(feature, [])
            
            not_allowed_aux = item.get("Not_Allowed_Metadata_Concepts", [])

            for category in categories:
                if category.startswith("_"):
                    continue
                
                self._category_dict[category][feature] = {
                    "Characterizations": characterizations,
                    "Auxiliary": is_aux,
                    "Unit": units,
                    "Not_Allowed_Auxiliary": not_allowed_aux
                }

    def get_categories(self):
        return list(self._category_dict.keys())

    def get_feature_attributes(self, category, feature):
        return self._category_dict.get(category, {}).get(feature, {})

    def get_feature_characterizations(self, category, feature):
        attributes = self.get_feature_attributes(category, feature)
        return attributes.get("Characterizations", [])

    def get_feature_auxiliary(self, category, feature):
        attributes = self.get_feature_attributes(category, feature)
        return attributes.get("Auxiliary", "No")

    def get_feature_unit(self, category, feature):
        attributes = self.get_feature_attributes(category, feature)
        return attributes.get("Unit", [])

    def handle_feature_click(self, category, feature_name):
        print(f"User clicked on: {category}/{feature_name}")

    def validate_constraint(
        self,
        auxiliary,
        category,
        feature,
        characterisation,
        units
    ):
        if category not in self._category_dict:
            return False

        if feature not in self._category_dict[category]:
            return False

        attributes = self._category_dict[category][feature]

        if auxiliary not in {"None", "Unspecified", "Any"}:
            if auxiliary not in self.VALID_AUXILIARY:
                return False
            
            if auxiliary in attributes.get("Not_Allowed_Auxiliary", []):
                return False

        if characterisation != "Unspecified":
            characterizations = attributes.get("Characterizations", [])
            if characterisation not in characterizations:
                return False

        ontology_units = attributes.get("Unit", [])

        if isinstance(ontology_units, str):
            ontology_units = [ontology_units]

        if units != "Unspecified":
            if units not in ontology_units:
                return False

        return True