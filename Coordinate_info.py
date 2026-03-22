class GetCoordinateInfo:
    def __init__(self, main_window, around_object_widget, advanced_coords_widget, coordinates_widget):
        self.current_databases = []
        self.current_query_mode = ""
        self.coordinate_areas_list = [] 

        main_window.Database_query_signal.connect(self.update_main_selections)

        # Listen to BOTH coordinate search widgets!
        around_object_widget.final_coords_query_signal.connect(self.add_coordinate_area)
        advanced_coords_widget.final_coords_query_signal.connect(self.add_coordinate_area)

        coordinates_widget.area_deleted_signal.connect(self.remove_coordinate_area)

    def update_main_selections(self, databases, query_mode):
        self.current_databases = databases
        self.current_query_mode = query_mode

    def add_coordinate_area(self, coords_dict):
        # Append the new area to our memory list
        self.coordinate_areas_list.append(coords_dict)
        self.print_current_payload()

    def remove_coordinate_area(self):
        # If there is something to remove, pop the last item off the list!
        if len(self.coordinate_areas_list) > 0:
            self.coordinate_areas_list.pop()
            print("Data Aggregator: Removed the last coordinate area.")
            self.print_current_payload()

    def print_current_payload(self):
        # Bundle everything together
        master_query_payload = {
            "Databases": self.current_databases,
            "Query_Mode": self.current_query_mode,
            "Coordinate_Settings": self.coordinate_areas_list 
        }

        print("\n--- MASTER PAYLOAD READY ---")
        print(f"Selected Databases: {master_query_payload['Databases']}")
        print(f"Query Mode: {master_query_payload['Query_Mode']}")
        print(f"Active Areas ({len(self.coordinate_areas_list)}): {master_query_payload['Coordinate_Settings']}")
        print("----------------------------\n")