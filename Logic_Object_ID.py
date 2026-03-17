
class Logic_Object_ID:
    def __init__(self, object_id_widget):
        # Use the widget passed from main.py
        self.ObjectID = object_id_widget
        self.ObjectID.ObjectID_Signal.connect(self.Evaluate_IDs)

    def Evaluate_IDs(self, IDs_list):
        print(f"Logic Layer Received: {IDs_list}")
        # Add your database check logic here