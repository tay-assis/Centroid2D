# -----------------------------------------------------------------------------
# This file is the logic of buttons in the main window.
# The logically is setting the selected shape variable.
# -----------------------------------------------------------------------------
class Index:
    def __init__(self):
        self.selected_shape = None
        
    def button_circle(self, event):
        """Action for Circle button."""
        self.selected_shape = 'Circle'
        print(f'Circle selected. Variable updated: {self.selected_shape}')

    def button_rectangle(self, event):
        """Action for Rectangle button."""
        self.selected_shape = 'Rectangle'
        print(f'Rectangle selected. Variable updated: {self.selected_shape}')

    def button_triangle(self, event):
        """Action for Triangle button."""
        self.selected_shape = 'Triangle'
        print(f'Triangle selected. Variable updated: {self.selected_shape}')
    
    def get_selected_shape(self):
        """Returns the current selected shape."""
        return self.selected_shape