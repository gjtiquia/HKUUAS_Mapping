"""
HKUUAS Mapping Module
"""

__author__ = "Tom Mong"
__email__ = "tom@stocksgram.com"

import resize
import odm
import crop
from camera_specs import CameraSpecs
from competition_info import CompetitionInfo


class Mapping:
    _default_odm_parameters = {
        "fast-orthophoto": True,
        "feature-quality": "low",
        "max-concurrency": 4,
        "pc-quality": "low",
        "orthophoto-resolution": 4,
        "pc-tile": True,
        "skip-report": True
    }

    def __init__(
        self, 
        camera_specs: CameraSpecs,
        competition_info: CompetitionInfo,
        images_path: str, 
        save_directory: str, 

        resize_ratio = 0.5, 
        odm_parameters: dict = _default_odm_parameters
    ):

        # Initialize class variables
        self.camera_specs = camera_specs
        self.competition_info = competition_info
        self.images_path = self._format_path(images_path, images_path)
        self.save_directory = self._format_path(save_directory, save_directory)

        self.resize_ratio = resize_ratio
        self.odm_parameters = odm_parameters

        print(self)

    def __str__(self) -> str:
        output = ""
        output += str(self.camera_specs)
        output += '\n' + str(self.competition_info)
        output += "\nImages Path: " + self.images_path
        output += "\nSave Directory: " + self.save_directory

        output += "\nResize Ratio: " + str(self.resize_ratio)
        output += "\nODM Parameters: " + str(self.odm_parameters)

        return output

    def get_flight_info(self):
        waypoint_list = []
        checkpoint_list = []
        flight_altitude = 0.0

        # Aim for taking within 60 images
        # Aim for overlap of at least 50%
        # Flight altitude is capped between the minimum and maximum specified by the competition

        return waypoint_list, checkpoint_list, flight_altitude


    def resize(self, original_images_path = None, resized_images_path = None, resize_ratio = None):
        # Use default paths if none specified
        original_images_path = self._format_path(original_images_path, self.images_path)
        resized_images_path = self._format_path(resized_images_path, self.save_directory + "resized_images/")
            
        if resize_ratio == None:
            # Set default resize ratio if none specified
            resize_ratio = self.resize_ratio

        resize.resize_all(original_images_path, resized_images_path, resize_ratio)


    def runODM(self, resized_images_path = None, odm_parameters = None):
        # Use default path if none specified
        resized_images_path = self._format_path(resized_images_path, self.save_directory + "resized_images/")
        
        # Use default ODM parameters if none specified
        if odm_parameters == None:
            odm_parameters = self.odm_parameters

        odm.run(resized_images_path, odm_parameters)


    def crop_map(
        self, geotiff_path: str = None, save_directory: str = None, 
        map_center_coordinates: tuple = None, map_height: float = None, in_feet = True
    ):

        # Use default paths if none specified
        save_directory = self._format_path(save_directory, self.save_directory)
        if geotiff_path == None:
            geotiff_path = self.save_directory + "odm_orthophoto/odm_orthophoto.tif"
        

        # Use default map center if none specified
        if map_center_coordinates == None:
            map_center_coordinates = self.competition_info.map_center_coordinates
        
        # Use default map height if none specified
        if map_height == None:
            map_height = self.competition_info.map_height
            in_feet = True
        
        # Change map height from feet to meters
        if in_feet:
            map_height /= 3.281

        crop.run(geotiff_path, save_directory, map_center_coordinates, map_height)


    def generate_map(self):
        # print("Resizing Images...")
        # self.resize()

        # print("Generating orthophoto with ODM...")
        # self.runODM()

        print("Cropping orthophoto...")
        self.crop_map()
    
    def _format_path(self, path: str, default_path: str) -> str:
        # Returns default path if none specified
        if path == None:
            return default_path
        
        # Adds tailing stroke
        if not path.endswith('/'):
            return path + '/'
        
        return path
