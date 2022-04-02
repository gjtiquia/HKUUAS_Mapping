"""
Camera Specification Class
"""

__author__ = "GJTiquia"
__email__ = "gershom.tiqui@gmail.com"


class CameraSpecs:
    def __init__(self, focal_length: float = None):
        self.focal_length = focal_length
    
    def __str__(self) -> str:
        output = "Camera Specifications:"
        output += "\n- Focal Length: " + str(self.focal_length)
        return output