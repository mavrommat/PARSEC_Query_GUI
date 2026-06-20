from curses import window
import sys
from PySide6.QtWidgets import QApplication
from MainWindowFunc import MainWindow
from Switch_main_queries import SwitchMainQueries
from Logic_Object_ID import Logic_Object_ID
from Switch_sub_queries import SwitchSubQueries
from Switch_sub_sub_queries import SwitchSubSubQueries
from Coordinate_info import GetCoordinateInfo
from CoordinateQueryEngine.ExecutionController import ExecutionController
from DisplayOutput.ResultsWindow import ResultsWindow
from PayloadAggregator import PayloadAggregator

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # main handler
    MainQueryHandler = SwitchMainQueries(window) 
    SubQueryHandler = SwitchSubQueries(window, MainQueryHandler)
    SubSubQueryHandler = SwitchSubSubQueries(window, MainQueryHandler, SubQueryHandler)

    ObjectIDHandler = Logic_Object_ID(MainQueryHandler.ObjectID)
    
    # 2. Data Aggregator
    CoordInfoGrabber = GetCoordinateInfo(
        window=window, 
        around_object=SubSubQueryHandler.AroundObject,
        manual_coords=SubQueryHandler.ManualCoords,
        draw_sky=SubQueryHandler.DrawSky,               
        coordinates_main=MainQueryHandler.Coordinates,
        adv_around_object=SubQueryHandler.AdvFlow_AroundObject,
        adv_manual_coords=SubQueryHandler.AdvFlow_ManualCoords,
        adv_draw_sky=SubQueryHandler.AdvFlow_DrawSky    
    )
    
    # 3. Execution Controller setup
    info_view_widget = SubQueryHandler.DisplayOptions
    
    execution_manager = ExecutionController(
        coord_info_grabber=CoordInfoGrabber,
        standard_coords_widget=MainQueryHandler.Coordinates, 
        info_view_widget=info_view_widget 
    )
    
    results_window = ResultsWindow(window)
    execution_manager.Execution_completed_signal.connect(results_window.display_results) 

    # 4. Payload Aggregator setup
    payload_aggregator = PayloadAggregator()
    
    # Coordinate Execution Capture
    def finalize_coordinate_payload(result_list):        
 
        payload_aggregator.reset_payload()  # Reset aggregator
        
        master_coord_payload = CoordInfoGrabber.get_master_payload()
        
        payload_aggregator.update_databases(master_coord_payload.get("Databases", []))
        payload_aggregator.update_main_query_type(master_coord_payload.get("Query_Mode", "Coordinates"))
        
        clean_results = []
        id_column_name = 'id' 
        
        for df in result_list:
            if hasattr(df, 'columns') and id_column_name in df.columns:
                clean_results.extend(df[id_column_name].tolist())
                
        unique_clean_results = list(set(clean_results))
        payload_aggregator.update_found_ids(unique_clean_results)
        payload_aggregator.save_to_json_file("final_search_payload.json")

    execution_manager.Execution_completed_signal.connect(finalize_coordinate_payload)

    
    # Object ID Execution Capture
    def finalize_object_id_payload(id_list):

        payload_aggregator.reset_payload()  # Reset aggregator
        
        payload_aggregator.update_databases(MainQueryHandler.Databases)
        payload_aggregator.update_main_query_type("Object ID")
        
        payload_aggregator.update_found_ids(id_list)
        payload_aggregator.save_to_json_file("final_object_id_payload.json")

    MainQueryHandler.ObjectID.ObjectID_Signal.connect(finalize_object_id_payload)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  