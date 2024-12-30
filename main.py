# Author: Taynara Araújo
# Date: 2024-12-29
# Description: This is the main file of the project.
# It is responsible for starting the application.

from src.ui.graphics_window import GraphicsWindow

window = GraphicsWindow(600, 600, "Centroid Detection")

window.run()