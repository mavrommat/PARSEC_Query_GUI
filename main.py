from curses import window
import sys
import subprocess
from pathlib import Path

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

from Database.mock_database import create_mock_db

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1800, 1000)

    create_mock_db() # Create a mock database with objects around the sky. We will cahnge it to the PARSEC query

    run_ontology_extraction() # Comment it if the ontology is up to date and dont need process the concepts again
    
    # main handler
    MainQueryHandler = SwitchMainQueries(window) 
    SubQueryHandler = SwitchSubQueries(window, MainQueryHandler)
    SubSubQueryHandler = SwitchSubSubQueries(window, MainQueryHandler, SubQueryHandler)

    ObjectIDHandler = Logic_Object_ID(MainQueryHandler.ObjectID)
    
    # Data Aggregator
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
    
    # Payload Aggregator initiation
    payload_aggregator = PayloadAggregator()
    
    is_advanced_flow = False
    do_coord_search = True

    # A. Advanced Flow Capture 
    def capture_advanced_constraints(constraints_dict):
        nonlocal is_advanced_flow
        is_advanced_flow = True
        print("Main: Captured Advanced Constraints.")
        payload_aggregator.update_constraints(constraints_dict)

    def capture_display_options(display_payload):
        nonlocal is_advanced_flow
        is_advanced_flow = True
        print("Main: Captured Display Options.")
        payload_aggregator.update_display_options(display_payload)

    def handle_coord_search_decision(decision):
        nonlocal do_coord_search
        do_coord_search = decision
        print(f"Main: Coordinate search active state set to {decision}")

    # CONNECT CAPTURES FIRST 
    SubQueryHandler.Advanced.Constraints_query_signal.connect(capture_advanced_constraints)
    SubQueryHandler.DisplayOptions.Displayed_concepts_signal.connect(capture_display_options)
    MainQueryHandler.CoordQuestion.Answer_Signal.connect(handle_coord_search_decision)
    
    # EXECUTION CONTROLLER 
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
        nonlocal is_advanced_flow, do_coord_search
        print("Main: Execution complete. Finalizing Payload...")
        
        # current metadata
        master_coord_payload = CoordInfoGrabber.get_master_payload()
        current_mode = master_coord_payload.get("Query_Mode", "Coordinates")
        
        if current_mode == "Coordinates" and not is_advanced_flow:
            print("Main: Standard search detected. Scrubbing stale advanced data...")
            payload_aggregator.update_constraints({})
            payload_aggregator.update_display_options({})
        
        # consistent metadata
        payload_aggregator.update_databases(master_coord_payload.get("Databases", []))
        payload_aggregator.update_main_query_type(current_mode)
        
        # Check if the user decided to skip the coordinate search
        clean_results = []
        if do_coord_search:
            print("Main: Extracting IDs...")
            id_column_name = 'id' 
            for df in result_list:
                if hasattr(df, 'columns') and id_column_name in df.columns:
                    clean_results.extend(df[id_column_name].tolist())
        else:
            print("Main: Coordinate search deactivated. Bypassing ID extraction.")
                
        unique_clean_results = list(set(clean_results))
        payload_aggregator.update_found_ids(unique_clean_results)
        
        payload_aggregator.save_to_json_file("final_search_payload.json")

        # Reset state flags for the next query cycle
        is_advanced_flow = False
        do_coord_search = True

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


def run_ontology_extraction():
        # get the root directory 
        root_dir = Path(__file__).parent.resolve()
        
        # Build  absolute paths
        script_path = root_dir / "Concepts" / "Extract_Concepts_from_Ontology_integrated.py"
        ontology_path = root_dir / "Concepts" / "Ontology" / "PARSEC_model_v.7.5.ttl"
        out_dir = root_dir / "Concepts" / "data" / "concepts"
        
        cmd = [
            sys.executable, 
            str(script_path),
            "--ontology", str(ontology_path),
            "--out-dir", str(out_dir)
        ]
        
        print("Starting Ontology Extraction...")
        try:
            subprocess.run(cmd, check=True)
            print("Ontology extraction completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error: Extraction script failed with exit code {e.returncode}")
        except FileNotFoundError:
            print("Error: Could not find the python executable or the extraction script.")

if __name__ == "__main__":
    main()