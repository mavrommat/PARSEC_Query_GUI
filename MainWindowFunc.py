import os
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, Signal
from MainWindowUI import Ui_MainWindow

class MainWindow(QMainWindow):

    Database_query_signal = Signal(list, str)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("PARSEC's GUI") # Window name

        # image paths
        current_folder = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_folder, "multimedia", "pismis24.png")
        icon_path = os.path.join(current_folder, "multimedia", "PARSEC_icon.png")
        
        self.setWindowIcon(QIcon(icon_path)) # Set icon

        self.original_pixmap = QPixmap(image_path)  
        
        # QLabel background canvas
        self.bg_label = QLabel(self.ui.centralwidget)
        self.bg_label.lower()  # Push it behind all widgets

        # transparent Groupboxes 
        transparent_style = "QGroupBox { background-color: transparent; border: none; }"
        self.ui.main_gb.setStyleSheet(transparent_style)
        self.ui.databases_gb.setStyleSheet(transparent_style)
        self.ui.search_by_gb.setStyleSheet(transparent_style)
        self.ui.main_query_gb.setStyleSheet(transparent_style)
        self.ui.output_gb.setStyleSheet(transparent_style)
        self.ui.db_query_selection_widget_gb.setStyleSheet(transparent_style)

        self.ui.welcome_db_query_gb.setStyleSheet("""
            QGroupBox { 
                background-color: hsla(0, 0%, 60%, 0); 
                border: none; 
            }
        """)

        button_style = """
            QPushButton:checked {
                background-color: hsla(248,24%,48%, 200);   
                border: 1px solid hsla(210, 80%, 70%, 255); 
                color: hsla(0, 0%, 100%, 255);                
            }

            QPushButton {
                background-color: hsla(0, 0%, 12%, 150);      /* Deep dark gray/black */
                color: hsla(0, 0%, 100%, 255);                /* Pure white text */
                border: 1px solid hsla(0, 0%, 30%, 255);      /* Subtle lighter gray border */
                border-radius: 6px;                           /* Slightly rounded corners */
                padding: 8px 16px;                            /* Comfortable spacing */
                font-weight: normal;
                font-family: "Source Code Pro";               /* Matches your UI font */
            }
            
            QPushButton:hover {
                background-color: hsla(0, 0%, 22%, 150);      /* Brightens up to a lighter gray on hover */
                border: 1px solid hsla(0, 0%, 45%, 150);      /* Border catches the light */
            }

            QPushButton:pressed {
                background-color: hsla(248,24%,48%, 200);   /* Turns vibrant blue when clicked! */
                border: 1px solid hsla(248,24%,48%, 200);   /* Light blue border glow */
                color: hsla(0, 0%, 100%, 255);                /* Keeps text pure white */
            }
        """

        # Apply a global style  
        self.ui.centralwidget.setStyleSheet(button_style)

        # Initialize tracking variables 
        self.current_search_mode = None
        
        # Database selection (Multiple allowed)
        self.ui.B_database_1.setCheckable(True)
        self.ui.B_database_2.setCheckable(True)

        # connect directly to broadcast
        self.ui.B_database_1.clicked.connect(self.broadcast_selections)
        self.ui.B_database_2.clicked.connect(self.broadcast_selections)

        # Search selection (Only one allowed)
        self.ui.B_objectid_search.clicked.connect(self.set_selected_one)
        self.ui.B_coordinates_search.clicked.connect(self.set_selected_one)
        self.ui.B_paper_authors_search.clicked.connect(self.set_selected_one)
        self.ui.B_advanced_search.clicked.connect(self.set_selected_one)

        self.query_layout = QVBoxLayout(self.ui.query_widget)
        self.query_layout.setContentsMargins(0, 0, 0, 0)
        
        # 1. Create the deck of cards
        self.query_stack = QStackedWidget()
        self.query_layout.addWidget(self.query_stack)

    # Resize the background picture to be compatable with change of the aspect ratio
    def resizeEvent(self, event):
        self.bg_label.resize(self.ui.centralwidget.size())
        scaled_pixmap = self.original_pixmap.scaled(
            self.ui.centralwidget.size(), 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.bg_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)

    

    def set_selected_one(self):
        self.ui.B_objectid_search.setStyleSheet("")
        self.ui.B_coordinates_search.setStyleSheet("")
        self.ui.B_paper_authors_search.setStyleSheet("")
        self.ui.B_advanced_search.setStyleSheet("")
        
        clicked_button = self.sender()
        clicked_button.setStyleSheet("""
            QPushButton { background-color: hsla(248,24%,48%, 200); border: 1px solid hsla(210, 80%, 70%, 255); color: hsla(0, 0%, 100%, 255); }
            QPushButton:hover { background-color: hsla(248,24%,60%, 200); }
            """)
        
        self.current_search_mode = clicked_button.text() # Save current search mode name
        
        self.broadcast_selections() # Announce the change to main.py

    def broadcast_selections(self):
        # Gather all currently active databases into a list
        active_dbs = []
        if self.ui.B_database_1.isChecked():
            active_dbs.append(self.ui.B_database_1.text())
        if self.ui.B_database_2.isChecked():
            active_dbs.append(self.ui.B_database_2.text())
            
        self.Database_query_signal.emit(active_dbs, str(self.current_search_mode)) # Emit the signal 

    def SwitchQueryWidget(self, widget):
        # If the widget isn't in the deck yet, add it
        if self.query_stack.indexOf(widget) == -1:
            self.query_stack.addWidget(widget)
            
        # Bring this specific widget to the top of the deck!
        self.query_stack.setCurrentWidget(widget)