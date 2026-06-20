from PySide6.QtCore import QObject, Signal, Slot
from CoordinateQueryEngine.CoordinateQueryExecution import QueryExecutionEngine

class ExecutionController(QObject):
    Execution_completed_signal = Signal(list) 

    def __init__(self, coord_info_grabber, standard_coords_widget, info_view_widget):
        super().__init__()
        
        self.coord_info_grabber = coord_info_grabber
        self.engine = QueryExecutionEngine() # Initializes the parquet DB and Astropy logic
        
        # Standard Flow 
        standard_coords_widget.Next_step_signal.connect(self.execute_standard_flow)
        
        # Advanced Flow
        info_view_widget.Displayed_concepts_signal.connect(self.execute_advanced_flow)

    @Slot(str)
    def execute_standard_flow(self, step_info):
        print(f"Execution Controller: Triggered by Standard Flow -> {step_info}")
        master_payload = self.coord_info_grabber.get_master_payload()
        self._run_query(master_payload)

    @Slot(dict)
    def execute_advanced_flow(self, concepts_dict):
        print("Execution Controller: Triggered by Advanced Flow (Info View Selection).")
        master_payload = self.coord_info_grabber.get_master_payload()
        
        # Inject the displayed concepts into the payload
        master_payload["Displayed_Concepts"] = concepts_dict
        
        self._run_query(master_payload)

    def _run_query(self, master_payload):
        print("Execution Controller: Initiating execution...")
        
        filtered_results_list = self.engine.execute_payload(master_payload)
        
        print(f"Execution Controller: Query complete. Found {len(filtered_results_list)} result sets.")
        
        self.Execution_completed_signal.emit(filtered_results_list)