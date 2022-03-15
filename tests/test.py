"""
Test

For testing code
"""
# Add access to the parent directory to access src folder
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.insert(0, str(path_root))

# import package src/HKUUAS_Mapping
from src.HKUUAS_Mapping import resize

__author__ = "GJTiquia"
__email__ = "GJTiquia"


if __name__ == "__main__":
    # Specify image directory paths
    # Note: - directory path MUST END WITH "/"
    #       - resized images should be saved in a folder called "images" for orthophoto generation
    images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2/images/"
    resized_images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2_resized/images/"

    # Step 1: Image Resize
    resize_ratio = 0.4
    resize.resize_all(images_path, resized_images_path, resize_ratio)

    # Step 2: Orthophoto generation from ODM
    # resized images must be in <path>/images/
    

    # Step 3: Crop generated orthophoto
    # 

    




