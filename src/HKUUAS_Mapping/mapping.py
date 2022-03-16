"""
HKUUAS Mapping Module
"""

__author__ = "Tom Mong"
__email__ = "tom@stocksgram.com"

class Mapping:
    def __init__(self,images_path,resized_images_path, resize_ratio=0.4):
        self.images_path = images_path
        self.resized_images_path = resized_images_path
        self.resize_ratio = resize_ratio


        # Add tailling stroke
        if not self.images_path.endswith('/'):
            self.images_path = self.images_path + "/"

        if not self.resized_images_path.endswith('/'):
            self.resized_images_path = self.resized_images_path + "/"

    def resize(self):
        resize.resize_all(self.images_path, self.resized_images_path, self.resize_ratio)

    images_path = "../../img/"
    resized_images_path = "../../resized/"

    # Step 1: Image Resize
    print("Step 1: Image Resize")
    resize_ratio = 0.4
    resize.resize_all(images_path, resized_images_path, resize_ratio)

    # Step 2: Orthophoto generation from ODM
    # resized images must be in <path>/images/
    # results will be saved at <path>
    print("Step 2: Orthophoto generation")
    odm.run(resized_images_path)

    # Step 3: Crop generated orthophoto
    print("Step 3: Crop orthophoto")
