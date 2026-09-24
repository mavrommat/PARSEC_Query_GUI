# -*- coding: utf-8 -*-
from PySide6.QtCore import QObject, Signal, Slot

class ResultsController(QObject):
    returned_home_signal = Signal()
    navigated_signal = Signal(str)

    def __init__(self, stack_widget, default_widget=None):
        super().__init__()
        self.stack = stack_widget
        self.default_widget = default_widget
        self.modules = {}
        self.history = []
        
        # State Tracking
        self.current_mode = "Object ID"  # Hardcoded default 
        
        
        self.routing_table = {
            "Object ID": {
                "Overview": "OverviewModule",
                "Measurements": "MeasurementsModule"
            },
            "Coordinates": {
                "Overview": "OverviewModule",
                "Measurements": "MeasurementsModule"
            },
            "Advanced Search": {
                "Overview": "OverviewModule",
                "Measurements": "MeasurementsModule"
            },
            "Bibliography": {
                "Overview": "OverviewModule",
                "Measurements": "MeasurementsModule"
            }
        }

    def set_mode(self, mode_name):
        self.current_mode = mode_name

    def register_module(self, name, widget):
        self.modules[name] = widget
        if self.stack.indexOf(widget) == -1:
            self.stack.addWidget(widget)
        self._bind_signals(widget)

    def _bind_signals(self, widget):
        if hasattr(widget, 'navigate_signal'):
            widget.navigate_signal.connect(self.route_action)
        if hasattr(widget, 'back_signal'):
            widget.back_signal.connect(self.route_back)
        if hasattr(widget, 'home_signal'):
            widget.home_signal.connect(self.route_home)

    @Slot(str, dict)
    def route_action(self, action_name, payload=None):
        mode_routes = self.routing_table.get(self.current_mode, {})
        target_name = mode_routes.get(action_name, action_name)
        
        if target_name not in self.modules:
            print(f"Controller Error: Target '{target_name}' not mapped for action '{action_name}' in mode '{self.current_mode}'.")
            return
            
        target_widget = self.modules[target_name]
        current = self.stack.currentWidget()
        
        # history for back-tracking
        if current and current != self.default_widget and current != target_widget:
            self.history.append(current)

        # Duck-type data injection
        if payload is not None:
            if hasattr(target_widget, "load_object_data"):
                target_widget.load_object_data(payload)
            elif hasattr(target_widget, "load_measurements"):
                target_widget.load_measurements(payload)
            elif hasattr(target_widget, "load_data"):
                target_widget.load_data(payload)

        self.stack.setCurrentWidget(target_widget)
        self.navigated_signal.emit(target_name)

    @Slot()
    def route_back(self):
        # Pops the last view from history
        if self.history:
            prev_widget = self.history.pop()
            self.stack.setCurrentWidget(prev_widget)
        else:
            self.route_home()

    @Slot()
    def route_home(self):
        # Clears history and restores the default query interface
        self.history.clear()
        if self.default_widget:
            self.stack.setCurrentWidget(self.default_widget)
        self.returned_home_signal.emit()