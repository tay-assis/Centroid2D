# -----------------------------------------------------------------------------
# Project: Centroid Detection 2D
# Author: Taynara Araújo
# Date: 2024-12-29
# Description: This is the main file of the project.
# It is responsible for starting the application.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

if __name__ == "__main__":
    """
    ---------------------------------------------------------------------------
    Main function 
    ---------------------------------------------------------------------------
    """

    class Index:
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

    x_axis = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    y_axis = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

    # Plotting the Cartesian Plane
    # This is setting up of the plane
    figure, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x_axis, y_axis, color="black", visible=False)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("Cartesian Plane")
    figure.canvas.manager.set_window_title("Centroid Detection")
    ax.grid(True)

    # Adjust the layout to make space for buttons
    figure.subplots_adjust(bottom=0.3)

    # Initialize selected shape variable
    selected_shape = None

    current_index = Index()

    # Create buttons ----------------------------------------------------------
    # Circle button
    ax_button_circle = figure.add_axes([0.1, 0.05, 0.2, 0.075])
    btn_circle = Button(ax_button_circle, "Circle", color='lightblue', hovercolor='lightgreen')
    btn_circle.on_clicked(current_index.button_circle)

    # Rectangle button
    ax_button_rectangle = figure.add_axes([0.4, 0.05, 0.2, 0.075])
    btn_rectangle = Button(ax_button_rectangle, "Rectangle", color='lightblue', hovercolor='lightgreen')
    btn_rectangle.on_clicked(current_index.button_rectangle)

    # Triangle button
    ax_button_triangle = figure.add_axes([0.7, 0.05, 0.2, 0.075])
    btn_triangle = Button(ax_button_triangle, "Triangle", color='lightblue', hovercolor='lightgreen')
    btn_triangle.on_clicked(current_index.button_triangle)
    # -------------------------------------------------------------------------

    plt.show()