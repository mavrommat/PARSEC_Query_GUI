from Switch_main_queries import SwitchMainQueries
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Coordinates.SearchAroundFanc import SearchAround
from Coordinates.RadiusFanc import Radius
from Coordinates.RectangularFanc import Rectagular
from Coordinates.PolygonFanc import Polygon

class SwitchSubSubQueries:
    def __init__(self, window, main_handler, sub_handler):
        self.main_window = window
        self.QueryHandler = main_handler
        self.SubHandler = sub_handler 
        
        # Main state trackers
        self.current_main_query = ""
        self.QueryHandler.Query_signal.connect(self.update_main_query)

        self.current_sub_query = ""
        self.SubHandler.Coordinates.Sub_coord_signal.connect(self.update_sub_query)

        self.AroundObject = self.SubHandler.AroundObject 
        self.Radius = self.AroundObject.Radius
        self.Rectangle = self.AroundObject.Rectangle
        self.Polygon = self.AroundObject.Polygon

        self.AroundObject.Sub_Sub_coord_signal.connect(self.SwitchToSubSubQuery)
        
        if hasattr(self.SubHandler, 'AdvFlow_AroundObject'):
            self.SubHandler.AdvFlow_Coordinates.Sub_coord_signal.connect(self.update_sub_query)
            
            self.AdvFlow_AroundObject = self.SubHandler.AdvFlow_AroundObject
            self.AdvFlow_Radius = self.AdvFlow_AroundObject.Radius
            self.AdvFlow_Rectangle = self.AdvFlow_AroundObject.Rectangle
            self.AdvFlow_Polygon = self.AdvFlow_AroundObject.Polygon
            
            self.AdvFlow_AroundObject.Sub_Sub_coord_signal.connect(self.SwitchToAdvFlowSubSubQuery)

    def update_main_query(self, query_name):
        self.current_main_query = query_name
        print(f"Main Level: {query_name}")

    def update_sub_query(self, sub_query_name):
        self.current_sub_query = sub_query_name
        print(f"Sub Level: {sub_query_name}")

    def SwitchToSubSubQuery(self, SubSubQuery):
        print(f"Path Check -> Main: {self.current_main_query} | Sub: {self.current_sub_query} | Target: {SubSubQuery}")
        
        if self.current_main_query == "Coordinates" and "Searching around" in self.current_sub_query:
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.Rectangle)
            elif SubSubQuery == "Polygon search":
                self.main_window.SwitchQueryWidget(self.Polygon)

    def SwitchToAdvFlowSubSubQuery(self, SubSubQuery):
        print(f"AdvFlow Path Check -> Target: {SubSubQuery}")
        
        if self.current_main_query == "Advanced Search" and "Searching around" in self.current_sub_query:
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Rectangle)
            elif SubSubQuery == "Polygon search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Polygon)

        if hasattr(self.SubHandler, 'AdvFlow_Coordinates'):
            self.SubHandler.AdvFlow_Coordinates.Sub_coord_signal.connect(self.update_sub_query)

        if hasattr(self.SubHandler, 'AdvFlow_AroundObject'):
            self.AdvFlow_AroundObject = self.SubHandler.AdvFlow_AroundObject
            
            # shapes directly from the AdvFlow 
            self.AdvFlow_Radius = self.AdvFlow_AroundObject.Radius
            self.AdvFlow_Rectangle = self.AdvFlow_AroundObject.Rectangle
            self.AdvFlow_Polygon = self.AdvFlow_AroundObject.Polygon

            self.AdvFlow_AroundObject.Sub_Sub_coord_signal.connect(self.SwitchToAdvFlowSubSubQuery)

    def SwitchToAdvFlowSubSubQuery(self, SubSubQuery):
        print(f"AdvFlow Path Check -> Target: {SubSubQuery}")
        
        if self.current_main_query == "Advanced Search" and "Searching around" in self.current_sub_query:
            if SubSubQuery == "Radius search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Radius)
            elif SubSubQuery == "Rectangle search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Rectangle)
            elif SubSubQuery == "Polygon search":
                self.main_window.SwitchQueryWidget(self.AdvFlow_Polygon)