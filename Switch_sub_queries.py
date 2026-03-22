
from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.AdvancedCoordsSearchFanc import AdvancedCoordsSearch

from Bibliographic.JournalFanc import Journal
from Bibliographic.ReferenceQueryFanc import Reference
from Bibliographic.BibcodeSearchFanc import Bibcode
from Bibliographic.AdvancedBibliographicFanc import AdvancedBibliographic
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

    def handle_completed_search_area(self, final_dict):
        # 1. Send the dictionary to the scroll widget to update the UI
        self.Coordinates.add_area_to_scroll_widget(final_dict)
        
        # 2. Switch the screen BACK to the main Coordinates widget!
        self.main_window.SwitchQueryWidget(self.Coordinates)