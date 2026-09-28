import sys
import subprocess
from pathlib import Path
from datetime import date
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

    create_mock_db() # Create a mock database with objects around the sky. We will change it to the PARSEC query

    # Checks if an ontology exists if not extracts it and record the date 
    # if it is a different date than recorded it re-extracts it
    run_ontology_extraction() 
    
    # Main handlers
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
    
    # State tracking variables
    is_advanced_flow = False
    do_coord_search = True
    display_output = False  # Track query completion state

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

    # Connect initial advanced/settings captures
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

    # B. Unified Execution Capture Handler
    def handle_query_completion(query_mode, payload_data):
        nonlocal is_advanced_flow, do_coord_search, display_output
        print(f"Main: Execution complete for {query_mode}. Finalizing Payload...")

        if query_mode == "Coordinates":
            master_coord_payload = CoordInfoGrabber.get_master_payload()
            current_mode = master_coord_payload.get("Query_Mode", "Coordinates")
            
            if current_mode == "Coordinates" and not is_advanced_flow:
                print("Main: Standard search detected. Scrubbing stale advanced data...")
                payload_aggregator.update_constraints({})
                payload_aggregator.update_display_options({})
            
            payload_aggregator.update_databases(master_coord_payload.get("Databases", []))
            payload_aggregator.update_main_query_type(current_mode)
            
            clean_results = []
            if do_coord_search:
                print("Main: Extracting IDs...")
                id_column_name = 'id' 
                for df in payload_data:
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

        elif query_mode == "Object ID":
            payload_aggregator.reset_payload()
            payload_aggregator.update_databases(MainQueryHandler.Databases)
            payload_aggregator.update_main_query_type("Object ID")
            payload_aggregator.update_found_ids(payload_data)
            payload_aggregator.save_to_json_file("final_object_id_payload.json")

        elif query_mode == "Bibliography":
            search_type = payload_data.get("Search", "Unknown Bib Search")
            print(f"Main: Captured Bibliographic Search -> {search_type}")
            
            payload_aggregator.reset_payload()
            payload_aggregator.update_databases(MainQueryHandler.Databases)
            payload_aggregator.update_main_query_type("Bibliography")
            payload_aggregator.update_bibliography(payload_data)
            payload_aggregator.save_to_json_file("final_bibliographic_payload.json")

        # Flip the universal execution state
        display_output = True
        print("Main: display_output is now set to True.")
        window.load_json_results(filename="test_results.json")


    # C. Wired completions (with strict order)
    
    # payload finalization data is saved before rendering
    execution_manager.Execution_completed_signal.connect(lambda result_list: handle_query_completion("Coordinates", result_list))
    
    # Connect ResultsWindow display 
    execution_manager.Execution_completed_signal.connect(results_window.display_results)

    # Connect Object ID signals
    MainQueryHandler.ObjectID.ObjectID_Signal.connect(lambda id_list: handle_query_completion("Object ID", id_list))

    # Connect Bibliographic signals
    SubQueryHandler.Journal.Bibliography_Signal.connect(lambda bib_dict: handle_query_completion("Bibliography", bib_dict))
    SubQueryHandler.Reference.Bibliography_Signal.connect(lambda bib_dict: handle_query_completion("Bibliography", bib_dict))
    SubQueryHandler.Bibcode.Bibliography_Signal.connect(lambda bib_dict: handle_query_completion("Bibliography", bib_dict))
    SubQueryHandler.AdvancedBibl.Bibliography_Signal.connect(lambda bib_dict: handle_query_completion("Bibliography", bib_dict))
    SubQueryHandler.AdvancedSemantic.Bibliography_Signal.connect(lambda bib_dict: handle_query_completion("Bibliography", bib_dict))

    window.show()
    sys.exit(app.exec())


def run_ontology_extraction():
    # get the root directory 
    root_dir = Path(__file__).parent.resolve()
    
    # Build absolute paths
    script_path = root_dir / "Concepts" / "Extract_Concepts_from_Ontology_integrated.py"
    ontology_path = root_dir / "Concepts" / "Ontology" / "PARSEC_model_v.7.5.ttl"
    out_dir = root_dir / "Concepts" / "data" / "concepts"
    
    # Path for the date tracker text file
    tracker_file = root_dir / "Concepts" / "data" / "last_update.txt"
    
    today_str = str(date.today())
    should_run = False
    
    # Check if the output directory exists and has files in it
    if not out_dir.exists() or not any(out_dir.iterdir()):
        should_run = True
        print("Output files missing. Triggering extraction.")
        
    # Check the date in the tracker file
    elif not tracker_file.exists():
        should_run = True
        print("Tracker file missing. Triggering extraction.")
    else:
        with open(tracker_file, 'r') as f:
            last_run_date = f.read().strip()
            
        if last_run_date != today_str:
            should_run = True
            print(f"Date changed (Last: {last_run_date}, Today: {today_str}). Triggering update.")
    
    # If everything is up to date skip extraction 
    if not should_run:
        print("Ontology files are up-to-date. Skipping extraction.")
        return

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
        
        # Ensure the directory exists before writing the tracker file
        tracker_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write today's date to the tracker file upon success
        with open(tracker_file, 'w') as f:
            f.write(today_str)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: Extraction script failed with exit code {e.returncode}")
    except FileNotFoundError:
        print("Error: Could not find the python executable or the extraction script.")

if __name__ == "__main__":
    main()