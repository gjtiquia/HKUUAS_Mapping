"""
Resize Module
"""

from PIL import Image
import os
import threading

if __name__ == "__main__":
    import transfer_exif
    import time_log
else:
    from . import transfer_exif
    from . import time_log


def resize_all(path, new_path, resize_ratio):
    """
    Resizes all the images from one directory by a resize ratio.
    Saves the resized images into another directory.

    Arguments:
        path: directory of images to resize, must end with /
        new_path: directory to save the resized images, must end with /
        resize_ratio: the resize ratio
    """
    dirs = os.listdir(path)
    for item in dirs:

        if os.path.isfile(path + item):
            resize_thread = ResizeThread(path, new_path, item, resize_ratio)
            resize_thread.start()


def resize_one(path, new_path, item, resize_ratio):
    print("[{}] Resizing {}...".format(time_log.get_time(), item))
    image = Image.open(path + item)

    new_image_height = int(image.size[0] / (1 / resize_ratio))
    new_image_length = int(image.size[1] / (1 / resize_ratio))

    image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
    image.save(new_path + item, 'JPEG', quality=90)

    transfer_exif.gps(path + item, new_path + item)

    print("[{}] Finished {}".format(time_log.get_time(), item))


class ResizeThread(threading.Thread):
    def __init__(self, path, new_path, item, resize_ratio):
        threading.Thread.__init__(self)
        self.path = path
        self.new_path = new_path
        self.item = item
        self.resize_ratio = resize_ratio

    def run(self):
        resize_one(self.path, self.new_path, self.item, self.resize_ratio)


# Test resize
if __name__ == "__main__":
    import sys
    sys.path.append(".")

    # Specify image directory paths
    # Note: - directory path MUST END WITH "/"
    #       - resized images should be saved in a folder called "images" for orthophoto generation
    images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2/images/"
    resized_images_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/test_directory/sheffield_park_2_resized/images/"

    # Step 1: Image Resize
    resize_ratio = 0.4
    resize_all(images_path, resized_images_path, resize_ratio)