"""
Competition Information Class
"""

__author__ = "GJTiquia"
__email__ = "gershom.tiqui@gmail.com"


class CompetitionInfo:
    def __init__(self, boundary_coordinate_list: list = None, map_center_coordinates: tuple = None, map_height: float = None):
        self.boundary_coordinate_list = boundary_coordinate_list
        self.map_center_coordinates = map_center_coordinates
        self.map_height = map_height
    
    def __str__(self) -> str:
        output = "Competition Information:"
        output += "\n- Boundary Coordinates: " +  str(self.boundary_coordinate_list)
        output += "\n- Map Center Coordinates: " + str(self.map_center_coordinates)
        output += "\n- Map Height: " + str(self.map_height)
        return output