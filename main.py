# Author: Taynara Araújo
# Date: 2024-12-29
# Description: This is the main file of the project.
# It is responsible for starting the application.

from src.ui.cartesian_plane import CartesianPlane

if __name__ == "__main__":
    
    x_axis = [-5, -4 ,-3 , -2, -1, 1, 2, 3, 4, 5]
    y_axis = [-5, -4 ,-3 , -2, -1, 1, 2, 3, 4, 5]
    x_label = "X Axis"
    y_label = "Y Axis"
    title = "Cartesian Plane"
    window_title = "Centroid Detection"
    figsize = (6, 5)
    
    cartesian_plane = CartesianPlane(
        x_axis = x_axis, 
        y_axis = y_axis, 
        x_label = x_label, 
        y_label = y_label, 
        title = title, 
        window_title = window_title, 
        figsize = figsize
    )
    
    cartesian_plane.show()