
from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.AdvancedCoordsSearchFanc import AdvancedCoordsSearch
from Coordinates.RadiusFanc import Radius
from Coordinates.RectangularFanc import Rectagular
from Coordinates.PolygonFanc import Polygon
from Coordinates.AdvRadiusFanc import AdvancedRadius
from Coordinates.AdvancedRectangleFanc import AdvancedRectangle
from Coordinates.AdvancedCustomFanc import AdvancedCustom

class SwitchSubSubQueries:
    def __init__(self, window, main_handler, sub_handler):
        self.main_window = window
        self.QueryHandler = main_handler
        self.SubHandler = sub_handler # Keep a reference to the sub_handler
        
        # Main state
        self.current_main_query = ""
        self.QueryHandler.Query_signal.connect(self.update_main_query)

        self.current_sub_query = ""
        self.SubHandler.Coordinates.Sub_coord_signal.connect(self.update_sub_query)

        # Sub-Sub widgets
        self.AroundObject = self.SubHandler.AroundObject 
        self.Radius = Radius()
        self.Rectangle = Rectagular()
        self.Polygon = Polygon()

        self.AdvancedCoords = self.SubHandler.AdvancedCoords
        self.AdvancedRadius = AdvancedRadius()
        self.AdvancedRectangle = AdvancedRectangle()
        self.AdvancedCustom = AdvancedCustom()
        # Connect the deepest signal
        self.AroundObject.Sub_Sub_coord_signal.connect(self.SwitchToSubSubQuery)
        self.AdvancedCoords.Sub_Sub_coord_signal.connect(self.SwitchToSubSubQuery)

    def update_main_query(self, query_name):
        self.current_main_query = query_name
        print(f"Main Level: {query_name}")

    def update_sub_query(self, sub_query_name):
        self.current_sub_query = sub_query_name
        print(f"Sub Level: {sub_query_name}")

    def SwitchToSubSubQuery(self, SubSubQuery):
        print(f"Path Check -> Main: {self.current_main_query} | Sub: {self.current_sub_query} | Target: {SubSubQuery}")
        
        if self.current_main_query == "Coordinates" and \
           "Searching around" in self.current_sub_query:
            
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.Rectangle)
            elif SubSubQuery == "Polygon search":
                self.main_window.SwitchQueryWidget(self.Polygon)
        
        elif self.current_main_query == "Coordinates" and \
           "Advanced" in self.current_sub_query:
            
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.AdvancedRadius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.AdvancedRectangle)
            elif SubSubQuery == "Custom shape search":
                    self.main_window.SwitchQueryWidget(self.AdvancedCustom)