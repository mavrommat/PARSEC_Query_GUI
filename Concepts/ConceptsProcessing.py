from collections import defaultdict
import requests
import csv

from PySide6.QtWidgets import QMenu, QToolButton
from PySide6.QtGui import QAction


class ConceptsProcessing:

    def __init__(
        self,
        file_path="Parsec_concepts v.1.1 - sifis_current_version.csv",
        url="http://139.91.183.61:8000/concepts"
    ):

        self.file_path = file_path
        self.url = url
        self._category_dict = defaultdict(list)

    def build_dictionary(self):

        # Clear dictionary
        self._category_dict.clear()

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            data = response.json()

            print(f"Downloaded {len(data)} concepts from API.")

            for item in data:
                category = item.get("Category", "Unknown").strip()
                feature = item.get("Name", "").strip()

                if not feature:
                    continue

                if feature not in self._category_dict[category]:
                    self._category_dict[category].append(feature)

            return dict(self._category_dict)

        except Exception as e:
            print(f"API failed: {e}")

  
        if not self.file_path:
            raise ValueError("No CSV file path provided.")

        print("Falling back to CSV loading...")

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            try:
                headers = next(reader)
                category_index = headers.index('Category')

            except StopIteration:
                raise ValueError("The provided CSV file is empty.")

            except ValueError:
                raise ValueError(
                    "The column 'Category' was not found in the headers."
                )

            for row in reader:
                if not row:
                    continue

                feature = row[0].strip()
                category = row[category_index].strip()

                if feature not in self._category_dict[category]:
                    self._category_dict[category].append(feature)

        return dict(self._category_dict)
        
    def get_categories(self):
        return list(self._category_dict.keys())

    def handle_feature_click(self, feature_name):
        print(f"User clicked on feature: {feature_name}")