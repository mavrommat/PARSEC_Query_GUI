
from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.AdvancedCoordsSearchFanc import AdvancedCoordsSearch

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

    def update_main_query(self, query_name):
        self.current_main_query = query_name

    def SwitchToSubQuery(self, SubQuery):
        print(f"SubQueryHandler reacting! Main: {self.current_main_query} | Sub: {SubQuery}")
        
        if self.current_main_query == "Coordinates" and \
           SubQuery == "Searching around an object/Specified coordinates":
            self.main_window.SwitchQueryWidget(self.AroundObject)
            
        if self.current_main_query == "Coordinates" and \
           SubQuery == "Advanced coordinate search":
            self.main_window.SwitchQueryWidget(self.AdvancedCoords)
        