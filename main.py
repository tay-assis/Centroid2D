# -----------------------------------------------------------------------------
# Project: Centroid Detection 2D
# Author: Taynara Araújo
# Description: This project is the simple calculator 
# of centroid of 2D figures on the Cartesian Plane.
# The user can draw actually three types of shapes:
#   -> Circle, Rectangle and Triangle.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from src.services.index import Index
from src.services.draw_shapes import DrawShapes

if __name__ == "__main__":
    """
    This function is responsible for setting up the
    Cartesian Plane and start others aplications of 
    the project.
    """
    # Setting up the Cartesian Plane
    x_axis = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    y_axis = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

    figure, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x_axis, y_axis, color="black", visible=False)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("Cartesian Plane")
    figure.canvas.manager.set_window_title("Centroid Detection")
    ax.grid(True)
    figure.subplots_adjust(bottom=0.3)

    # Instancing the Index
    current_index = Index()

    # Creating buttons
    ax_button_circle = figure.add_axes([0.1, 0.05, 0.2, 0.075])
    btn_circle = Button(ax_button_circle, "Circle", color='lightblue', hovercolor='lightgreen')
    btn_circle.on_clicked(current_index.button_circle)

    ax_button_rectangle = figure.add_axes([0.4, 0.05, 0.2, 0.075])
    btn_rectangle = Button(ax_button_rectangle, "Rectangle", color='lightblue', hovercolor='lightgreen')
    btn_rectangle.on_clicked(current_index.button_rectangle)

    ax_button_triangle = figure.add_axes([0.7, 0.05, 0.2, 0.075])
    btn_triangle = Button(ax_button_triangle, "Triangle", color='lightblue', hovercolor='lightgreen')
    btn_triangle.on_clicked(current_index.button_triangle)

    # Instancing the DrawShapes
    draw_shapes = DrawShapes(figure, ax, current_index)

    plt.show()
