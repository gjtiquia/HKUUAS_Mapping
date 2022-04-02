"""
HKUUAS Mapping Module
"""

__author__ = "Tom Mong"
__email__ = "tom@stocksgram.com"

import resize
import odm
import crop


class CameraSpecs:

    def __init__(self, focal_length = None):
        self.focal_length = focal_length

        self.gsd = self.calculate_gsd()
    

    def calculate_gsd(self):
        pass


class Mapping:
    _default_odm_parameters = {
        "fast-orthophoto": True,
        "feature-quality": "lowest",
        "max-concurrency": 4,
        "pc-quality": "lowest",
        "orthophoto-resolution": 4,
        "pc-tile": True,
        "skip-report": True
    }

    def __init__(
        self, 

        cameraSpecs,

        boundary_coordinate_list, 
        map_center_coordinate, 
        map_height,

        images_path, 
        save_directory, 

        resize_ratio=0.4, 
        odm_parameters = _default_odm_parameters
    ):

        # Initialize class variables
        self.cameraSpecs = cameraSpecs

        self.boundary_coordinate_list = boundary_coordinate_list
        self.map_center_coordinate = map_center_coordinate
        self.map_height = map_height

        self.images_path = images_path
        self.save_directory = save_directory

        self.resize_ratio = resize_ratio
        self.odm_parameters = odm_parameters

        # Add tailling stroke
        if not self.images_path.endswith('/'):
            self.images_path = self.images_path + "/"

        if not self.save_directory.endswith('/'):
            self.save_directory = self.save_directory + "/"


    def get_flight_info(self):
        waypoint_list = []
        checkpoint_list = []
        flight_altitude = 0.0

        # Aim for taking within 60 images
        # Aim for overlap of at least 50%
        # Flight altitude is capped


        return waypoint_list, checkpoint_list, flight_altitude


    def resize(self, original_images_path = None, resized_images_path = None, resize_ratio = None):
        if original_images_path == None:
            # Set default path if none specified
            original_images_path = self.images_path
        else:
            # Add tailing stroke
            if not original_images_path.endswith('/'):
                original_images_path = original_images_path + '/'

        if resized_images_path == None:
            # Set default path if none specified
            resized_images_path = self.save_directory + "resized_images/"
        else:
            # Add tailing stroke
            if not resized_images_path.endswith('/'):
                resized_images_path = resized_images_path + '/'
            
        if resize_ratio == None:
            # Set default resize ratio if none specified
            resize_ratio = self.resize_ratio

        resize.resize_all(original_images_path, resized_images_path, resize_ratio)


    def runODM(self, resized_images_path = None, odm_parameters = None):
        # Use default file path if none specified
        if resized_images_path == None:
            resized_images_path = self.save_directory + "/resized_images/"
        else:
            # Add tailing stroke
            if not resized_images_path.endswith('/'):
                resized_images_path = resized_images_path + '/'
        
        # Use default ODM parameters if none specified
        if odm_parameters == None:
            odm_parameters = self.odm_parameters

        odm.run(resized_images_path, odm_parameters)


    def crop_map(self, geotiff_path = None, save_path = None, map_center_coordinates = None, map_height = None, in_feet = True):
        

        # Use default map center if none specified
        if map_center_coordinates == None:
            map_center_coordinates = self.map_center_coordinate
        
        if map_height == None:
            map_height = self.map_height
            in_feet = True
        
        # Change map height from feet to meters
        if in_feet:
            map_height /= 3.281

        crop.run(geotiff_path, save_path, map_center_coordinates, map_height)


    def generate_map(self):
        print("Resizing Images...")
        self.resize()

        print("Generating orthophoto with ODM...")
        self.runODM()

        # print("Cropping orthophoto...")
        # self.crop_map()
