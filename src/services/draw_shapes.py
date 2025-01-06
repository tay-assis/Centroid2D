# -----------------------------------------------------------------------------
# This file is logic to draw any types of shapes
# in the Cartesian Plane with the moviments of mouse.
# -----------------------------------------------------------------------------

import matplotlib.patches as patches
import numpy as np

class DrawShapes:
    def __init__(self, fig, ax, index):
        self.ax = ax
        self.fig = fig
        self.index = index  # Load the index class
        self.start_point = None
        self.end_point = None

        # Connect the events with mouse
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

    def on_press(self, event):
        """Capture the initial point on click of mouse."""
        selected_shape = self.index.get_selected_shape()
        if event.inaxes and selected_shape:
            self.start_point = (event.xdata, event.ydata)
            if selected_shape == 'Circle':
                self.end_point = patches.Circle(
                    (self.start_point), 0.5, 
                    edgecolor='black', 
                    facecolor='none'
                )
                self.ax.add_patch(self.end_point)

    def on_motion(self, event):
        """Update the draw while mouse is moving."""
        selected_shape = self.index.get_selected_shape()
        if event.inaxes and self.start_point and selected_shape == 'Circle':
            dx = event.xdata - self.start_point[0]
            dy = event.ydata - self.start_point[1]
            radius = np.sqrt(dx**2 + dy**2)

            self.end_point.set_radius(radius)
            self.fig.canvas.draw_idle()

    def on_release(self, event):
        """Finalize the draw when releasing the mouse button."""
        selected_shape = self.index.get_selected_shape()
        if self.start_point and selected_shape == 'Circle':
            self.start_point = None
            self.index.selected_shape = None
