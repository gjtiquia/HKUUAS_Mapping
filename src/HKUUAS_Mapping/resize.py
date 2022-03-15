from PIL import Image
import os
import transfer_exif
import threading
import time_log


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

