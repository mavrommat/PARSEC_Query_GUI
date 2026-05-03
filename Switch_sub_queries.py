
from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.AdvancedCoordsSearchFanc import AdvancedCoordsSearch

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

        self.Coordinates = self.QueryHandler.Coordinates 
        self.Coordinates.Sub_coord_signal.connect(self.SwitchToSubQuery)

        self.AroundObject = SearchAround()
        self.AdvancedCoords = AdvancedCoordsSearch()
        self.AroundObject.final_coords_query_signal.connect(self.handle_completed_search_area)
        self.AdvancedCoords.final_coords_query_signal.connect(self.handle_completed_search_area)


        self.Bibliography = self.QueryHandler.Bibliography 
        self.Bibliography.Sub_coord_signal.connect(self.SwitchToSubQuery)

        self.Journal = Journal()
        self.Reference = Reference()
        self.Bibcode = Bibcode()
        self.AdvancedBibl = AdvancedBibliographic()
        self.AdvancedSemantic = AdvancedSemantic()
        

        #  ADVANCED FLOW DUPLICATION 
        # Yes/No signal
        self.QueryHandler.CoordQuestion.Answer_Signal.connect(self.route_adv_question)

        # duplicate main panel 
        self.AdvFlow_Coordinates = self.QueryHandler.AdvFlow_Coordinates
        self.AdvFlow_Coordinates.Sub_coord_signal.connect(self.SwitchToAdvFlowSubQuery)

        self.AdvFlow_Coordinates.ui.B_submit_coord_search.setText("Confirm areas: Next Process")
        
        #--- 1. CONNECT THE COORDS COMPLETION SIGNAL
        self.AdvFlow_Coordinates.Next_step_signal.connect(self.handle_adv_coords_completed)
        
        # independent duplicates of the sub-panels
        self.AdvFlow_AroundObject = SearchAround()
        self.AdvFlow_AdvancedCoords = AdvancedCoordsSearch()
        self.Constraints = Constraints()
        self.ViewSelection = InfoViewSelection()

        #--- 2. CONNECT THE CONSTRAINTS COMPLETION SIGNAL
        self.Constraints.Constraints_query_signal.connect(self.handle_constraints_completed)

        # signals back to the duplicate main panel
        self.AdvFlow_AroundObject.final_coords_query_signal.connect(self.handle_adv_flow_completed)
        self.AdvFlow_AdvancedCoords.final_coords_query_signal.connect(self.handle_adv_flow_completed)

    def route_adv_question(self, wants_coords):
        if wants_coords:
            self.main_window.SwitchQueryWidget(self.AdvFlow_Coordinates)

    def SwitchToAdvFlowSubQuery(self, SubQuery):
        print(f"AdvFlow SubQuery triggered: {SubQuery}")
        if SubQuery == "Searching around an object/Specified coordinates":
            self.main_window.SwitchQueryWidget(self.AdvFlow_AroundObject)
        elif SubQuery == "Advanced coordinate search":
            self.main_window.SwitchQueryWidget(self.AdvFlow_AdvancedCoords)

    def handle_adv_flow_completed(self, final_dict):
        # Add the completed area to the DUPLICATE scroll widget, then switch back
        self.AdvFlow_Coordinates.add_area_to_scroll_widget(final_dict)
        self.main_window.SwitchQueryWidget(self.AdvFlow_Coordinates)

    # --- 

    def update_main_query(self, query_name):
        self.current_main_query = query_name

    def SwitchToSubQuery(self, SubQuery):
        print(f"SubQueryHandler reacting! Main: {self.current_main_query} | Sub: {SubQuery}")
        
        if self.current_main_query == "Coordinates" and \
           SubQuery == "Searching around an object/Specified coordinates":
            self.main_window.SwitchQueryWidget(self.AroundObject)

        elif self.current_main_query == "Coordinates" and \
           SubQuery == "Advanced coordinate search":
            self.main_window.SwitchQueryWidget(self.AdvancedCoords)

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
        # 1. Send the dictionary to the scroll widget to update the UI
        self.Coordinates.add_area_to_scroll_widget(final_dict)
        
        # 2. Switch the screen BACK to the main Coordinates widget!
        self.main_window.SwitchQueryWidget(self.Coordinates)
    
    def route_adv_question(self, wants_coords):
        if wants_coords:
            # User clicked "Yes"
            self.main_window.SwitchQueryWidget(self.AdvFlow_Coordinates)
        else:
            # User clicked "No" -> Route straight to Constraints
            print("Skipping Coordinates. Routing to next advanced step...")
            self.main_window.SwitchQueryWidget(self.Constraints)
    
    def handle_adv_coords_completed(self, status_string):
        """Catches the Next_step_signal from AdvFlow_Coordinates."""
        if status_string == "Coord Search Completed":
            print("AdvFlow Coordinates finished! Routing to Constraints...")
            self.main_window.SwitchQueryWidget(self.Constraints)

    def handle_constraints_completed(self, groups_data):
        """Catches the Constraints_query_signal from Constraints."""
        print(f"Constraints finished with data: {groups_data}")
        print("Routing to the Next Step...")
        self.main_window.SwitchQueryWidget(self.ViewSelection)