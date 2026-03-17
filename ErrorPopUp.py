import os
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QFont  
from PySide6.QtCore import Qt

class ErrorPopup(QMessageBox):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_folder, "multimedia", "warning_icon.png")

        # 1. Setup Custom Font
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        self.setFont(font)  # Applies the font to the text and buttons in the popup

        # 2. Setup Custom Scaled Icon
        original_pixmap = QPixmap(icon_path)
        scaled_pixmap = original_pixmap.scaled(
            64, 64, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.setIconPixmap(scaled_pixmap) 
        
        # 3. Setup Window Text and Buttons
        self.setWindowTitle(title)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        # Optional: You can easily add stylesheets here if you want custom colors later
        self.setStyleSheet("QLabel { color: red; }")

    def show_popup(self):
        # Trigger the popup and halt the code until the user clicks 'Ok'
        self.exec()