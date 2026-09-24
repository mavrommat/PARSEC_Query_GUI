from curses import window
import os
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QStackedWidget, QWidget
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, Signal
from MainWindowUI import Ui_MainWindow
from Results.ResultsObjectsFanc import Results_Objects
from Results.ObjectOverviewFanc import ObjectOverviewWidget
from Results.DisplayConcepts import AllMeasurementsWidget
from ResultsController import ResultsController
from ResultsProcessor import ResultsProcessor

class MainWindow(QMainWindow):

    Database_query_signal = Signal(list, str)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("PARSEC's GUI") # Window name
        # image paths
        current_folder = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_folder, "multimedia", "eso0932a.jpg")
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
        self.ui.B_bibliographic_search.clicked.connect(self.set_selected_one)
        self.ui.B_advanced_search.clicked.connect(self.set_selected_one)

        self.query_layout = QVBoxLayout(self.ui.query_widget)
        self.query_layout.setContentsMargins(0, 0, 0, 0)
        
        #====================================================================
        # Results Wiring
        #====================================================================
        self.query_stack = QStackedWidget()
        self.query_layout.addWidget(self.query_stack)
        self.empty_query_widget = QWidget()
        self.empty_query_widget.setStyleSheet("background: transparent;")
        self.query_stack.addWidget(self.empty_query_widget)
        self.output_layout = QVBoxLayout(self.ui.output_widget)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        
        # Instantiate the widgets
        self.results_widget = Results_Objects()
        self.overview_widget = ObjectOverviewWidget()
        self.all_measurements_widget = AllMeasurementsWidget()
        
        # Initialize Controller (replaces ViewRouter)
        self.controller = ResultsController(self.query_stack, self.empty_query_widget)
        
        # Register modules with abstraction names
        self.controller.register_module("OverviewModule", self.overview_widget)
        self.controller.register_module("MeasurementsModule", self.all_measurements_widget)        
        
        # Ensure Results_Objects UI knows which actions to display
        self.results_widget.set_available_views(["Overview", "Measurements"])
        
        # Route main results panel requests directly into the orchestrator
        self.results_widget.request_view_signal.connect(self.controller.route_action)
        
        # Wire UI updates to controller events
        self.controller.navigated_signal.connect(self.clear_search_modes)
        self.controller.returned_home_signal.connect(self.restore_search_modes)

        # Add the requested widgets to their respective layouts
        self.output_layout.addWidget(self.results_widget)
        
        #  Jumpstart the backend processor
        self.results_processor = ResultsProcessor()
        self.results_processor.Processed_data_signal.connect(self.results_widget.receive_processed_data)


        # 'B_execute_query' to start the process
        #self.ui.B_execute_query.clicked.connect(self.load_json_results)
        self.load_json_results()

    def SwitchQueryWidget(self, widget):
        """Adds a widget to the query stack if it doesn't exist, and brings it to the front."""
        if self.query_stack.indexOf(widget) == -1:
            self.query_stack.addWidget(widget)
        self.query_stack.setCurrentWidget(widget)

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
        self.ui.B_bibliographic_search.setStyleSheet("")
        self.ui.B_advanced_search.setStyleSheet("")
        
        clicked_button = self.sender()
        clicked_button.setStyleSheet("""
            QPushButton { background-color: hsla(248,24%,48%, 200); border: 1px solid hsla(210, 80%, 70%, 255); color: hsla(0, 0%, 100%, 255); }
            QPushButton:hover { background-color: hsla(248,24%,60%, 200); }
            """)
        
        self.current_search_mode = clicked_button.text() # Save current search mode name
        
        if hasattr(self, 'controller'):
            self.controller.set_mode(self.current_search_mode)
            
        self.broadcast_selections() # Announce to main

    def broadcast_selections(self):
        # Gather all currently active databases into a list
        active_dbs = []
        if self.ui.B_database_1.isChecked():
            active_dbs.append(self.ui.B_database_1.text())
        if self.ui.B_database_2.isChecked():
            active_dbs.append(self.ui.B_database_2.text())
            
        self.Database_query_signal.emit(active_dbs, str(self.current_search_mode)) # Emit the signal 
    
    def clear_search_modes(self, module_name): # Deselection of query buttons
        self.ui.B_objectid_search.setStyleSheet("")
        self.ui.B_coordinates_search.setStyleSheet("")
        self.ui.B_bibliographic_search.setStyleSheet("")
        self.ui.B_advanced_search.setStyleSheet("")

    def restore_search_modes(self):
        if self.current_search_mode:
            self.broadcast_selections()
            
        buttons = {
            "Object ID": self.ui.B_objectid_search,
            "Coordinates": self.ui.B_coordinates_search,
            "Bibliography": self.ui.B_bibliographic_search,
            "Advanced Search": self.ui.B_advanced_search
        }
        
        if self.current_search_mode in buttons:
            buttons[self.current_search_mode].setStyleSheet("""
                QPushButton { background-color: hsla(248,24%,48%, 200); border: 1px solid hsla(210, 80%, 70%, 255); color: hsla(0, 0%, 100%, 255); }
                QPushButton:hover { background-color: hsla(248,24%,60%, 200); }
            """)

    def load_json_results(self, filename="test_results.json"):
        if self.current_search_mode != "Object ID":
            print("Note: Currently only hardcoded to support 'Object ID' searches.")
            # return # Uncomment enforcing Object ID mode for later use
            
        current_folder = os.path.dirname(os.path.abspath(__file__))
        mockup_path = os.path.join(current_folder, filename)
        
        self.results_processor.load_from_json(mockup_path)