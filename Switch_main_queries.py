from PySide6.QtCore import QObject, Signal #
from MainWindowFunc import MainWindow
from ObjectID.SearchByObjectIdFanc import SearchByObjectIdWidget
from Coordinates.CoordinatesSearchFanc import SearchByCoordinatesWidget
from Bibliographic.BibliographicSearchFanc import BibliographicSearch

class SwitchMainQueries(QObject): 

    Query_signal = Signal(str)

    def __init__(self, window):
        super().__init__() 

        self.Databases = []
        self.Query = ""

        self.main_window = window
        self.main_window.Database_query_signal.connect(self.Signal_Separation)
    
        # Query Modes
        self.ObjectID = SearchByObjectIdWidget()
        self.Coordinates = SearchByCoordinatesWidget()
        self.Bibliography = BibliographicSearch()

    def Signal_Separation(self, Databases, Query):
        self.Databases = Databases
        self.Query = Query
        print(f"Active Databases: {Databases} | Query Mode: {Query}")
        self.Identify_Query(Query)

    def Identify_Query(self, Query):
        if Query == "Object ID":
            self.main_window.SwitchQueryWidget(self.ObjectID)
        elif Query == "Coordinates":
            self.main_window.SwitchQueryWidget(self.Coordinates)
        elif Query == "Bibliography":
            self.main_window.SwitchQueryWidget(self.Bibliography)

        self.Query_signal.emit(str(Query)) 