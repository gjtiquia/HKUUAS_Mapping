"""
For testing code
"""
# import package src/HKUUAS_Mapping
from mapping import Mapping, CameraSpecs

__author__ = "GJTiquia"
__email__ = "GJTiquia"

if __name__ == "__main__":
    # Remember to first Run OpenDroneMap Docker Container
    # Check README.md for more details

    # Information from Interoperability Server
    boundary_coordinate_list = []
    map_center_coordinate = (0,0)
    map_height = 0.0 # in feet

    # Camera Specs
    cameraSpecs = CameraSpecs(
        focal_length = 5
    )

    # User-specified paths
    images_path = "../../test_directory/images"
    save_directory = "../../test_directory"

    # Create Mapping object
    mapping = Mapping(
        cameraSpecs,
        
        boundary_coordinate_list,
        map_center_coordinate,
        map_height,

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
        odm_parameters = {
            "fast-orthophoto": True,
            "feature-quality": "low",
            "max-concurrency": 4,
            "pc-quality": "low",
            "orthophoto-resolution": 4,
            "pc-tile": True,
            "skip-report": True,
        }

        mapping.runODM(
            resized_images_path = save_directory + "/resized_images/", 
            odm_parameters = odm_parameters
        )

        # Step 3: Crop generated orthophoto
        print("Step 3: Crop orthophoto")