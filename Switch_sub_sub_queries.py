
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
     

        self.Radius = self.AroundObject.Radius
        self.Rectangle = self.AroundObject.Rectangle
        self.Polygon = self.AroundObject.Polygon
        
        self.AdvancedRadius = self.AdvancedCoords.AdvancedRadius
        self.AdvancedRectangle = self.AdvancedCoords.AdvancedRectangle
        self.AdvancedCustom = self.AdvancedCoords.AdvancedCustom

        # --- NEW CODE: ADVANCED FLOW SUB-SUB DUPLICATION ---
        
        # Track sub-queries from the duplicate main panel
        self.SubHandler.AdvFlow_Coordinates.Sub_coord_signal.connect(self.update_sub_query)

        # Grab the duplicate sub-panels
        self.AdvFlow_AroundObject = self.SubHandler.AdvFlow_AroundObject
        self.AdvFlow_AdvancedCoords = self.SubHandler.AdvFlow_AdvancedCoords

        # Instantiate brand new shape widgets for the Advanced Flow
        self.AdvFlow_Radius = Radius()
        self.AdvFlow_Rectangle = Rectagular()
        self.AdvFlow_Polygon = Polygon()

        self.AdvFlow_Adv_Radius = AdvancedRadius()
        self.AdvFlow_Adv_Rectangle = AdvancedRectangle()
        self.AdvFlow_Adv_Custom = AdvancedCustom()

        # 1. Grab the standard shapes from the AdvFlow version of AroundObject
        self.AdvFlow_Radius = self.AdvFlow_AroundObject.Radius
        self.AdvFlow_Rectangle = self.AdvFlow_AroundObject.Rectangle
        self.AdvFlow_Polygon = self.AdvFlow_AroundObject.Polygon

        # 2. Grab the advanced shapes from the AdvFlow version of AdvancedCoords
        self.AdvFlow_Adv_Radius = self.AdvFlow_AdvancedCoords.AdvancedRadius
        self.AdvFlow_Adv_Rectangle = self.AdvFlow_AdvancedCoords.AdvancedRectangle
        self.AdvFlow_Adv_Custom = self.AdvFlow_AdvancedCoords.AdvancedCustom

        # Connect the deepest signals for the Advanced flow
        self.AdvFlow_AroundObject.Sub_Sub_coord_signal.connect(self.SwitchToAdvFlowSubSubQuery)
        self.AdvFlow_AdvancedCoords.Sub_Sub_coord_signal.connect(self.SwitchToAdvFlowSubSubQuery)

    # --- NEW METHOD FOR ADVANCED FLOW ROUTING ---
    def SwitchToAdvFlowSubSubQuery(self, SubSubQuery):
        # Note: When the user is in this flow, current_main_query is "Advanced Search"
        print(f"AdvFlow Path Check -> Target: {SubSubQuery}")
        
        if self.current_main_query == "Advanced Search" and "Searching around" in self.current_sub_query:
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Rectangle)
            elif SubSubQuery == "Polygon search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Polygon)
        
        elif self.current_main_query == "Advanced Search" and "Advanced" in self.current_sub_query:
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Adv_Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Adv_Rectangle)
            elif SubSubQuery == "Custom shape search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Adv_Custom)

    
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