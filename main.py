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
    

    # 4. Payload Aggregator setup
    payload_aggregator = PayloadAggregator()
    
    # A. Advanced Flow Capture 
    def capture_advanced_constraints(constraints_dict):
        print("Main: Captured Advanced Constraints.")
        payload_aggregator.update_constraints(constraints_dict)

    def capture_display_options(display_payload):
        print("Main: Captured Display Options.")
        payload_aggregator.update_display_options(display_payload)

    SubQueryHandler.Advanced.Constraints_query_signal.connect(capture_advanced_constraints)
    SubQueryHandler.DisplayOptions.Displayed_concepts_signal.connect(capture_display_options)
    
    # 3. Execution Controller setup
    info_view_widget = SubQueryHandler.DisplayOptions
    
    execution_manager = ExecutionController(
        coord_info_grabber=CoordInfoGrabber,
        standard_coords_widget=MainQueryHandler.Coordinates, 
        info_view_widget=info_view_widget 
    )
    
    results_window = ResultsWindow(window)
    execution_manager.Execution_completed_signal.connect(results_window.display_results) 



    # B. Universal Execution Capture 
    def finalize_execution_payload(result_list):
        print("Main: Execution complete. Extracting IDs...")
        
        # current metadata
        master_coord_payload = CoordInfoGrabber.get_master_payload()
        current_mode = master_coord_payload.get("Query_Mode", "Coordinates")
        
        # If this is a Standard Coordinate search wipe out any lingering Data 
        if current_mode == "Coordinates":
            print("Main: Standard search detected. Scrubbing stale advanced data...")
            payload_aggregator.update_constraints({})
            payload_aggregator.update_display_options({})
        
        #  consistent metadata
        payload_aggregator.update_databases(master_coord_payload.get("Databases", []))
        payload_aggregator.update_main_query_type(current_mode)
        
        # 4. Extract and format the IDs
        clean_results = []
        id_column_name = 'id' 
        for df in result_list:
            if hasattr(df, 'columns') and id_column_name in df.columns:
                clean_results.extend(df[id_column_name].tolist())
                
        unique_clean_results = list(set(clean_results))
        payload_aggregator.update_found_ids(unique_clean_results)
        
        payload_aggregator.save_to_json_file("final_search_payload.json")

    execution_manager.Execution_completed_signal.connect(finalize_execution_payload)


    # C. Object ID Execution Capture 
    def finalize_object_id_payload(id_list):
        payload_aggregator.reset_payload()
        payload_aggregator.update_databases(MainQueryHandler.Databases)
        payload_aggregator.update_main_query_type("Object ID")
        payload_aggregator.update_found_ids(id_list)
        payload_aggregator.save_to_json_file("final_object_id_payload.json")

    MainQueryHandler.ObjectID.ObjectID_Signal.connect(finalize_object_id_payload)

    # D. Bibliographic Execution Capture
    def finalize_bibliographic_payload(bib_dict):
        search_type = bib_dict.get("Search", "Unknown Bib Search")
        print(f"Main: Captured Bibliographic Search -> {search_type}")
        
        # Wipe out any stale Coordinate/Advanced data
        payload_aggregator.reset_payload()
        
        payload_aggregator.update_databases(MainQueryHandler.Databases)
        payload_aggregator.update_main_query_type("Bibliography")
        
        # 3. Inject bibliographic dictionary
        payload_aggregator.update_bibliography(bib_dict)
        
        payload_aggregator.save_to_json_file("final_bibliographic_payload.json")

    # Connect the signals from all 5 Bibliographic sub-widgets
    SubQueryHandler.Journal.Bibliography_Signal.connect(finalize_bibliographic_payload)
    SubQueryHandler.Reference.Bibliography_Signal.connect(finalize_bibliographic_payload)
    SubQueryHandler.Bibcode.Bibliography_Signal.connect(finalize_bibliographic_payload)
    SubQueryHandler.AdvancedBibl.Bibliography_Signal.connect(finalize_bibliographic_payload)
    SubQueryHandler.AdvancedSemantic.Bibliography_Signal.connect(finalize_bibliographic_payload)


    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  