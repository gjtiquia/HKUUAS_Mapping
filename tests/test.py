"""
Test

For testing code
"""

from src.HKUUAS_Mapping.resize import resize_all


__author__ = "GJTiquia"
__email__ = "GJTiquia"


if __name__ == "__main__":
    # Specify image directory paths
    # MUST END WITH "\"
    images_path = ""
    resized_images_path = ""

    # Step 1: Image Resize
    resize_ratio = 0.4
    resize_all(images_path, resized_images_path, resize_ratio)

    




