"""
For testing code
"""
# import package src/HKUUAS_Mapping
import resize
import odm

__author__ = "GJTiquia"
__email__ = "GJTiquia"


if __name__ == "__main__":
    # Remember to first start a NodeODM node in docker with the command
    #   docker run -ti -p 3000:3000 opendronemap/nodeodm

    # Specify image directory paths
    # Note: - directory path MUST END WITH "/"
    #       - resized images should be saved in a folder called "images" for orthophoto generation
    images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2/images/"
    resized_images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2_resized/images/"
    orthophoto_save_path = ""

    # Step 1: Image Resize
    print("Step 1: Image Resize")
    resize_ratio = 0.4
    resize.resize_all(images_path, resized_images_path, resize_ratio)

    # Step 2: Orthophoto generation from ODM
    # resized images must be in <path>/images/
    # results will be saved at <path>
    print("Step 2: Orthophoto generation")
    odm.run()

    # Step 3: Crop generated orthophoto
    # 

    




