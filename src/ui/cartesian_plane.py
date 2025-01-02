# -----------------------------------------------------------------------------
# This file is responsible for creating the main window
# Cartesian plane and its configuration.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.widgets import Button

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

        # Setting the window title
        self.figure.canvas.manager.set_window_title(self.window_title)

    # def toggle_curve(self):
    #     """
    #     ---------------------------------------------------------------------
    #     Set up the visibiliy of the curve plot.
    #     The curve will be shown if it doesn't exist.
    #     This method is to inicialite the plot without curve.
    #     ---------------------------------------------------------------------
    #     """
    #     if self.plot_line is None:
    #         # Create curve if it doesn't exist
    #         self.plot_line, = self.ax.plot(self.x_axis, self.y_axis, visible=True)
    #         self.ax.legend()
    #     else:
    #         # Remove curve if it exists
    #         self.plot_line.remove()
    #         self.plot_line = None
    #         self.ax.legend().remove()  # Remove the legend

    #     self.figure.canvas.draw_idle()  # Update the window

        

    def show(self):
        plt.show()