import exif


def gps(image_path, new_image_path, save = True):
    """
    Copies GPS metadata from an image to another image.

    Arguments:
        image_path: path of image to copy GPS metadata.
        new_image_path: path of image to overwrite GPS metadata.
        save: save the changes.
    """

    img = exif.Image(image_path)

    # Check if image has exif info
    if not img.has_exif:
        print("No EXIF data found")
        return

    new_img = exif.Image(new_image_path)

    new_img.gps_altitude = img.get("gps_altitude")

    try:
        new_img.gps_altitude_ref = img.get("gps_altitude_ref")
    except TypeError:
        pass

    new_img.gps_latitude = img.get("gps_latitude")

    new_img.gps_latitude_ref = img.get("gps_latitude_ref")
    new_img.gps_longitude = img.get("gps_longitude")
    new_img.gps_longitude_ref = img.get("gps_longitude_ref")

    try:
        new_img.gps_version_id = img.get("gps_version_id")
    except TypeError:
        pass

    if save:
        with open(new_image_path, 'wb') as new_image_file:
            new_image_file.write(new_img.get_file())


def read_gps(image_path):
    img = exif.Image(image_path)

    print(img.has_exif)

    # Check if image has exif info
    if not img.has_exif:
        return

    print(img.get("gps_altitude_ref"))
    print(img.get("gps_altitude_ref"))
    print(img.get("gps_latitude"))
    print(img.get("gps_latitude_ref"))
    print(img.get("gps_longitude"))
    print(img.get("gps_longitude_ref"))
    print(img.get("gps_version_id"))
