from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.ManualCoordsFanc import ManualCoords
from Coordinates.DrawOnSky import DrawOnSky

from Bibliographic.JournalFanc import Journal
from Bibliographic.ReferenceQueryFanc import Reference
from Bibliographic.BibcodeSearchFanc import Bibcode
from Bibliographic.AdvancedBibliographicFanc import AdvancedBibliographic
from Bibliographic.AdvancedSemanticFanc import AdvancedSemantic

from Advanced.ConstraintsFanc import Constraints
from Advanced.InfoViewSelectionFanc import InfoViewSelection
class SwitchSubQueries:
    def __init__(self, window, main_handler):
        self.main_window = window
        self.QueryHandler = main_handler
        
        self.current_main_query = ""
        self.QueryHandler.Query_signal.connect(self.update_main_query)

        # --- COORDINATES ROUTING ---
        self.Coordinates = self.QueryHandler.Coordinates 
        self.Coordinates.Sub_coord_signal.connect(self.SwitchToSubQuery)

        self.AroundObject = SearchAround()
        self.ManualCoords = ManualCoords()
        self.DrawSky = DrawOnSky()
        self.AroundObject.final_coords_query_signal.connect(self.handle_completed_search_area)
        self.ManualCoords.settings_info_signal.connect(self.handle_completed_search_area)
        self.DrawSky.settings_info_signal.connect(self.handle_completed_search_area)

        # --- BIBLIOGRAPHY ROUTING ---
        self.Bibliography = self.QueryHandler.Bibliography 
        self.Bibliography.Sub_coord_signal.connect(self.SwitchToSubQuery)

        self.Journal = Journal()
        self.Reference = Reference()
        self.Bibcode = Bibcode()
        self.AdvancedBibl = AdvancedBibliographic()
        self.AdvancedSemantic = AdvancedSemantic()
        
        # Yes/No signal
        self.CoordQuestion = self.QueryHandler.CoordQuestion 
        self.CoordQuestion.Answer_Signal.connect(self.handle_advanced_question_answer)

        # Create Advanced Flow
        self.AdvFlow_Coordinates = SearchByCoordinatesWidget()
        self.AdvFlow_AroundObject = SearchAround()
        self.AdvFlow_ManualCoords = ManualCoords()
        self.AdvFlow_DrawSky = DrawOnSky()

        self.Advanced = Constraints()
        self.AdvFlow_Coordinates.ui.B_submit_coord_search.setText("Submit Coordinates: Next Step")
        self.AdvFlow_Coordinates.ui.B_submit_coord_search.clicked.connect(self.route_to_constraints)

        # Connect advanced flow sub-signals
        self.AdvFlow_Coordinates.Sub_coord_signal.connect(self.SwitchToSubQuery)

        self.Advanced = Constraints()
        # Connect advanced flow sub-signals
        self.AdvFlow_Coordinates.Sub_coord_signal.connect(self.SwitchToSubQuery)
        
        self.AdvFlow_AroundObject.final_coords_query_signal.connect(self.handle_adv_completed_search_area)
        self.AdvFlow_ManualCoords.settings_info_signal.connect(self.handle_adv_completed_search_area)
        self.AdvFlow_DrawSky.settings_info_signal.connect(self.handle_adv_completed_search_area)

        self.DisplayOptions = InfoViewSelection()
        self.Advanced.Constraints_query_signal.connect(self.route_to_display_options)
        
        # final payload from InfoViewSelection
        self.DisplayOptions.Displayed_concepts_signal.connect(self.handle_final_advanced_query)
        
    def update_main_query(self, query_name):
        self.current_main_query = query_name

    def SwitchToSubQuery(self, SubQuery):
        print(f"SubQueryHandler reacting! Main: {self.current_main_query} | Sub: {SubQuery}")
        
        # --- STANDARD COORDINATES SWITCHING ---
        if self.current_main_query == "Coordinates" and \
           SubQuery == "Searching around an object/Specified coordinates":
            self.main_window.SwitchQueryWidget(self.AroundObject)

        elif self.current_main_query == "Coordinates" and \
           SubQuery == "Manual Coordinates":
            self.main_window.SwitchQueryWidget(self.ManualCoords)
        
        elif self.current_main_query == "Coordinates" and \
           SubQuery == "Draw on Sky":
            self.main_window.SwitchQueryWidget(self.DrawSky)

        # --- ADVANCED FLOW COORDINATES SWITCHING ---
        elif self.current_main_query == "Advanced Search" and \
             SubQuery == "Searching around an object/Specified coordinates":
            self.main_window.SwitchQueryWidget(self.AdvFlow_AroundObject)

        elif self.current_main_query == "Advanced Search" and \
             SubQuery == "Manual Coordinates":
            self.main_window.SwitchQueryWidget(self.AdvFlow_ManualCoords)

        elif self.current_main_query == "Advanced Search" and \
             SubQuery == "Draw on Sky":
            self.main_window.SwitchQueryWidget(self.AdvFlow_DrawSky)

        # --- BIBLIOGRAPHY SWITCHING ---
        elif self.current_main_query == "Bibliography" and \
           SubQuery == "Journal Search":
            self.main_window.SwitchQueryWidget(self.Journal)
        
        elif self.current_main_query == "Bibliography" and \
           SubQuery == "Reference Search":
            self.main_window.SwitchQueryWidget(self.Reference)

        elif self.current_main_query == "Bibliography" and \
           SubQuery == "Bibcode Search":
            self.main_window.SwitchQueryWidget(self.Bibcode)

        elif self.current_main_query == "Bibliography" and \
           SubQuery == "Advanced Bibliographic Search":
            self.main_window.SwitchQueryWidget(self.AdvancedBibl)
        
        elif self.current_main_query == "Bibliography" and \
           SubQuery == "Advanced Semantic Search":
            self.main_window.SwitchQueryWidget(self.AdvancedSemantic)

    def handle_completed_search_area(self, final_dict):
        # Send the dictionary to the scroll widget
        self.Coordinates.add_area_to_scroll_widget(final_dict)
        
        # Switch screen to the main Coordinates
        self.main_window.SwitchQueryWidget(self.Coordinates)

    def handle_adv_completed_search_area(self, final_dict):
        # Update UI for the Advanced Flow 
        self.AdvFlow_Coordinates.add_area_to_scroll_widget(final_dict)
        self.main_window.SwitchQueryWidget(self.AdvFlow_Coordinates)
    
    def handle_advanced_question_answer(self, wants_coordinates):
        if wants_coordinates:
            print("Advanced Flow: User clicked YES for coordinates.")
            self.main_window.SwitchQueryWidget(self.AdvFlow_Coordinates)
        else:
            print("Advanced Flow: User clicked NO for coordinates.")
            self.main_window.SwitchQueryWidget(self.Advanced)
    
    def route_to_constraints(self):
        print("Advanced Flow: Coordinates submitted. Routing to Constraints.")
        self.main_window.SwitchQueryWidget(self.Advanced)
    
    def route_to_display_options(self):
        print("Advanced Flow: Constraints submitted. Routing to Display Options.")
        self.main_window.SwitchQueryWidget(self.DisplayOptions)  # Uncomment and implement when DisplayOptions is ready

    def handle_final_advanced_query(self, display_payload):
        print("Advanced Flow Complete! Display Options Selected:")
        print(f"View Mode: {display_payload['view_mode']}")
        print(f"Features: {display_payload['features']}")