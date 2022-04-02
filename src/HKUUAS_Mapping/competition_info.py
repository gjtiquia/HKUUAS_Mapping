"""
Competition Information Class
"""

__author__ = "GJTiquia"
__email__ = "gershom.tiqui@gmail.com"


class CompetitionInfo:
    def __init__(self, boundary_coordinate_list = None, map_center_coordinates = None, map_height = None):
        self.boundary_coordinate_list = boundary_coordinate_list
        self.map_center_coordinates = map_center_coordinates
        self.map_height = map_height