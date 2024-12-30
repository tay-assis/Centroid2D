# This file is responsible for creating the Cartesian 
# plane and its configuration.

import matplotlib.pyplot as plt

class CartesianPlane:
    def __init__(self, x_axis, y_axis, x_label, y_label, title):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

        # Plotting the Cartesian Plane
        plt.plot(self.x_axis, self.y_axis)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)

        plt.plot(self.x_axis, self.y_axis)

    def show(self):
        plt.show()