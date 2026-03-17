import sys
from PySide6.QtWidgets import QApplication
from MainWindowFunc import MainWindow

from Switch_main_queries import SwitchMainQueries
from Logic_Object_ID import Logic_Object_ID
from Switch_sub_queries import SwitchSubQueries
from Switch_sub_sub_queries import SwitchSubSubQueries

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # 1. Create the main handler
    MainQueryHandler = SwitchMainQueries(window) 

    ObjectIDHandler = Logic_Object_ID(MainQueryHandler.ObjectID)

    # 2. Pass the EXISTING MainQueryHandler here
    SubQueryHandler = SwitchSubQueries(window, MainQueryHandler)

    SubSubQueryHandler = SwitchSubSubQueries(window, MainQueryHandler, SubQueryHandler)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()