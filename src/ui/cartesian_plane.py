# This file is responsible for creating the main window
# Cartesian plane and its configuration.

import matplotlib.pyplot as plt

class CartesianPlane:
    def __init__(self, x_axis, y_axis, x_label, y_label, title, window_title, figsize):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.window_title = window_title
        self.figsize = figsize

        # Plotting the Cartesian Plane
        self.figure, self.ax = plt.subplots(figsize=self.figsize)
        self.ax.plot(self.x_axis, self.y_axis)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.set_title(self.title)

        # Setting the window title
        self.figure.canvas.manager.set_window_title(self.window_title)

    def show(self):
        plt.show()