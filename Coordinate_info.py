class GetCoordinateInfo:
    def __init__(self, window, around_object, manual_coords, draw_sky, coordinates_main, adv_around_object, adv_manual_coords, adv_draw_sky):
        self.main_window = window
        
        # Standard Flow Widgets
        self.around_object = around_object
        self.manual_coords = manual_coords
        self.coordinates_main = coordinates_main
        self.draw_sky = draw_sky

        # Advanced Flow Widgets
        self.adv_around_object = adv_around_object
        self.adv_manual_coords = adv_manual_coords
        self.adv_draw_sky = adv_draw_sky

        self.current_databases = []
        self.current_query_mode = ""
        
        # --- SEPARATE MEMORY LISTS ---
        self.coordinate_areas_list = [] 
        self.advanced_areas_list = [] 

        # Database Signal
        self.main_window.Database_query_signal.connect(self.update_main_selections)

        # 1. Connect Standard Flow
        self.around_object.final_coords_query_signal.connect(self.add_coordinate_area)
        self.manual_coords.settings_info_signal.connect(self.add_coordinate_area)
        self.draw_sky.settings_info_signal.connect(self.add_coordinate_area)

        # 2. Connect Advanced Flow to a DIFFERENT method
        self.adv_around_object.final_coords_query_signal.connect(self.add_advanced_area)
        self.adv_manual_coords.settings_info_signal.connect(self.add_advanced_area)
        self.adv_draw_sky.settings_info_signal.connect(self.add_advanced_area)

        # Deletions (Assuming standard for now)
        self.coordinates_main.area_deleted_signal.connect(self.remove_coordinate_area)

    def update_main_selections(self, databases, query_mode):
        self.current_databases = databases
        self.current_query_mode = query_mode

    # --- STANDARD FLOW METHODS ---
    def add_coordinate_area(self, coords_dict):
        coords_dict["Flow_Type"] = "Standard" # Optional tag
        self.coordinate_areas_list.append(coords_dict)
        self.print_current_payload()

    def remove_coordinate_area(self):
        if len(self.coordinate_areas_list) > 0:
            self.coordinate_areas_list.pop()
            print("Data Aggregator: Removed the last standard coordinate area.")
            self.print_current_payload()

    # --- ADVANCED FLOW METHODS ---
    def add_advanced_area(self, coords_dict):
        coords_dict["Flow_Type"] = "Advanced" # Tag it so you know exactly where it came from
        self.advanced_areas_list.append(coords_dict)
        self.print_current_payload()

    # --- PAYLOAD GENERATOR ---
    def print_current_payload(self):
        # Bundle everything together with separate views
        master_query_payload = {
            "Databases": self.current_databases,
            "Query_Mode": self.current_query_mode,
            "Standard_Coordinates": self.coordinate_areas_list,
            "Advanced_Coordinates": self.advanced_areas_list
        }

        print("\n--- MASTER PAYLOAD READY ---")
        print(f"Selected Databases: {master_query_payload['Databases']}")
        print(f"Query Mode: {master_query_payload['Query_Mode']}")
        print(f"Standard Areas ({len(self.coordinate_areas_list)}): {master_query_payload['Standard_Coordinates']}")
        print(f"Advanced Areas ({len(self.advanced_areas_list)}): {master_query_payload['Advanced_Coordinates']}")
        print("----------------------------\n")

    def get_master_payload(self):
        return {
            "Databases": self.current_databases,
            "Query_Mode": self.current_query_mode,
            "Standard_Coordinates": self.coordinate_areas_list,
            "Advanced_Coordinates": self.advanced_areas_list
        }