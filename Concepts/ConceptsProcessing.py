import csv
from collections import defaultdict
from PySide6.QtWidgets import (QMenu, QToolButton)
from PySide6.QtGui import QAction

class ConceptsProcessing:

    def __init__(self, file_path):
        
        self.file_path = file_path
        self._category_dict = defaultdict(list)

    def build_dictionary(self):
        # Clear the dictionary 
        self._category_dict.clear()

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            try:
                headers = next(reader) # Read the header row
                category_index = headers.index('Category') # Dynamically find the index of the 'Category' column
            except StopIteration:
                raise ValueError("The provided CSV file is empty.")
            except ValueError:
                raise ValueError("The column 'Category' was not found in the headers.")

            # Loop through the remaining rows
            for row in reader:
                if not row:
                    continue 
                
                # ADD .strip() HERE
                feature = row[0].strip()               
                category = row[category_index].strip() 
                
                self._category_dict[category].append(feature)

        # Return as a standard dictionary
        return dict(self._category_dict)

    def get_categories(self): # Returns just the list of unique categories found.
        return list(self._category_dict.keys())
    

    # Example method to handle the clicks (if you uncomment the line above)
    def handle_feature_click(self, feature_name):
        print(f"User clicked on feature: {feature_name}")

