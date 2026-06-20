import pandas as pd
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableView, QLabel
from DisplayOutput.PandasTableModel import PandasTableModel
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication

class ResultsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Query Results")
        self.resize(900, 600)
        
        self.layout = QVBoxLayout(self)
        
        self.status_label = QLabel("Waiting for results...")
        self.status_label.setStyleSheet("color: white; font-weight: bold;")
        self.layout.addWidget(self.status_label)

        self.table_view = QTableView()
        self.table_view.setStyleSheet("""
            QTableView {
                background-color: hsla(0, 0%, 12%, 150);
                color: white;
                gridline-color: gray;
            }
            QHeaderView::section {
                background-color: hsla(248, 24%, 38%, 200);
                color: white;
                font-weight: bold;
                padding: 4px;
            }
        """)
        self.layout.addWidget(self.table_view)

        self.copy_shortcut = QShortcut(QKeySequence.StandardKey.Copy, self.table_view)
        self.copy_shortcut.activated.connect(self.copy_to_clipboard)

    def display_results(self, filtered_results_list):        
        if not filtered_results_list:
            self.status_label.setText("Search completed, but no objects were found in the selected areas.")
            self.show()
            return
            
        # For multiple areas at once -> combine the results 
        if len(filtered_results_list) > 1:
            final_df = pd.concat(filtered_results_list, ignore_index=True)
            # Optional: drop duplicates if areas overlap
            final_df = final_df.drop_duplicates(subset=['ra', 'dec']) 
        else:
            final_df = filtered_results_list[0]

        total_objects = len(final_df)
        self.status_label.setText(f"Success: Found {total_objects} objects.")

        self.model = PandasTableModel(final_df)
        self.table_view.setModel(self.model)
        
        self.show()

    def copy_to_clipboard(self):
        selection = self.table_view.selectionModel()
        indexes = selection.selectedIndexes()

        if not indexes:
            return

        # Sort the selected cells by row, then by column
        indexes.sort(key=lambda idx: (idx.row(), idx.column()))

        copy_text = ""
        current_row = indexes[0].row()

        for idx in indexes:
            # If we've moved to a new row, add a newline
            if idx.row() != current_row:
                copy_text += "\n"
                current_row = idx.row()
            # If we are in the same row (but not the first item), add a tab
            elif idx != indexes[0]: 
                copy_text += "\t"
            
            # Grab the raw text from the model
            copy_text += str(self.model.data(idx))

        # Push the formatted text to the system clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(copy_text)
        
        self.status_label.setText(f"Copied {len(indexes)} cells to clipboard.")