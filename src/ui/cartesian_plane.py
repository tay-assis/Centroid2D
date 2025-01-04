# -----------------------------------------------------------------------------
# This file is responsible for creating the main window
# Cartesian plane and its configuration.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.widgets import Button

class Index:
    def button_circle(self, event):
        """Action for Circle button."""
        print("Entrou na função `button_circle`")
        self.selected_shape = 'Circle'
        print(f'Circle selected. Variable updated: {self.selected_shape}')

    def button_rectangle(self, event):
        """Action for Rectangle button."""
        self.selected_shape = 'Rectangle'
        print(f'Rectangle selected. Variable updated: {self.selected_shape}')

    def button_triangle(self, event):
        """Action for Triangle button."""
        print("Entrou na função `button_triangle`")
        self.selected_shape = 'Triangle'
        print(f'Triangle selected. Variable updated: {self.selected_shape}')

class CartesianPlane:
    def __init__(self, x_axis, y_axis, x_label, y_label, title, window_title, figsize):
        """
        ---------------------------------------------------------------------
        Initialize the Cartesian Plane with your parameters.
        ---------------------------------------------------------------------
        """
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.window_title = window_title
        self.figsize = figsize

        # Plotting the Cartesian Plane
        self.figure, self.ax = plt.subplots(figsize=self.figsize)
        self.ax.plot(self.x_axis, self.y_axis, color="black", visible=False)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.set_title(self.title)
        self.ax.grid(True)

        # Adjust the layout to make space for buttons
        self.figure.subplots_adjust(bottom=0.3)

        # Setting the window title
        self.figure.canvas.manager.set_window_title(self.window_title)

        # Initialize selected shape variable
        self.selected_shape = None

        # Circle button
        ax_circle = self.figure.add_axes([0.1, 0.05, 0.2, 0.075])
        btn_circle = Button(ax_circle, "Circle", color='lightblue', hovercolor='lightgreen')
        btn_circle.on_clicked(self.button_circle)

        # Rectangle button
        ax_rectangle = self.figure.add_axes([0.4, 0.05, 0.2, 0.075])
        btn_rectangle = Button(ax_rectangle, "Rectangle", color='lightblue', hovercolor='lightgreen')
        btn_rectangle.on_clicked(self.button_rectangle)

        # Triangle button
        ax_triangle = self.figure.add_axes([0.7, 0.05, 0.2, 0.075])
        btn_triangle = Button(ax_triangle, "Triangle", color='lightblue', hovercolor='lightgreen')
        btn_triangle.on_clicked(self.button_triangle)

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
        

    def show(self):
        """
        Display the Cartesian Plane.
        """
        plt.show()
