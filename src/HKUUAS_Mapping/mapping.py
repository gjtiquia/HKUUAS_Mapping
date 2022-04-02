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

    def runODM(self):
        odm.run(self.resized_images_path)

