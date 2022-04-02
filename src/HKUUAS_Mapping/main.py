"""
Package Usage Example
"""
# import package src/HKUUAS_Mapping
from mapping import Mapping
from camera_specs import CameraSpecs
from competition_info import CompetitionInfo

__author__ = "GJTiquia"
__email__ = "GJTiquia"

if __name__ == "__main__":
    # Remember to first Run OpenDroneMap Docker Container
    # Check README.md for more details

    # Competition Information from Interoperability Server
    competition_info = CompetitionInfo(
        boundary_coordinate_list = [],
        map_center_coordinates = (28.039819, -82.697501),
        map_height = 300 # in feet
    )
    
    # Camera Specs
    camera_specs = CameraSpecs(
        focal_length = 5
    )

    # User-specified paths
    images_path = "../../test_directory/images"
    save_directory = "../../test_directory"

    # Create Mapping object
    mapping = Mapping(
        camera_specs,
        competition_info,
        images_path, 
        save_directory
    )

    # Get Waypoint coordinates
    # Output:
    #   Waypoints
    #   Checkpoints
    #   Flight Altitude
    waypoint_list, checkpoint_list, flight_altitude = mapping.get_flight_info()

    # Map Generation
    use_default_parameters = False
    if use_default_parameters:
        # Use default parameters to generate map
        mapping.generate_map()
    
    else:
        # Use custom parameters in each step of the map generation
        #
        # Step 1: Image Resize
        print("Step 1: Image Resize")
        mapping.resize(
            original_images_path = images_path,
            resized_images_path = save_directory + "/resized_images/",
            resize_ratio = 0.5
        )

        # Step 2: Orthophoto generation from ODM
        print("Step 2: Orthophoto generation")
        parameters = {
            "fast-orthophoto": True,
            "feature-quality": "low", # ultra | high | medium | low | lowest
            "max-concurrency": 4,
            "pc-quality": "low", # ultra | high | medium | low | lowest
            "orthophoto-resolution": 4,
            "pc-tile": True,
            "skip-report": True,
        }

        mapping.runODM(
            resized_images_path = save_directory + "/resized_images/", 
            odm_parameters = parameters
        )

        # Step 3: Crop generated orthophoto
        print("Step 3: Crop orthophoto")
        mapping.crop_map(
            geotiff_path = save_directory + "/odm_orthophoto/odm_orthophoto.tif",
            save_directory = save_directory
        )