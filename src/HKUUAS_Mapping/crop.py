import geopandas as gpd
import utm
from shapely.geometry import Polygon
from osgeo import gdal

def read_shapefile(path):
    gdf = gpd.read_file(path)
    return gdf


def write_shapefile(center, width, height, path, filename = "python_rect.shp"):
    utm_center = utm.from_latlon(center[0], center[1])
    utm_x = utm_center[0]
    utm_y = utm_center[1]
    
    x_offset = width / 2.0
    y_offset = height / 2.0

    points = [(-x_offset, -y_offset), (-x_offset, y_offset), (x_offset, y_offset), (x_offset, -y_offset), (-x_offset, -y_offset)]
    coordinates = [(i[0] + utm_x, i[1] + utm_y) for i in points]

    # EPSG:4326 is the standard latlongpip
    # EPSG:32617 is UTM zone 17
    shapefile = create_polygon(coordinates, "Rectangle", 32617)
    # shapefile.to_file(path + filename)

    # print("Shapefile written and saved at " + path + filename)


def create_polygon(coordinates, polygon_name, epsg):
    ''' Create a polygon from coordinates '''
    polygon = Polygon(coordinates)
    gdf = gpd.GeoDataFrame(crs = {'init' :'epsg:' + str(epsg)})
    gdf.loc[0,'name'] = polygon_name
    gdf.loc[0, 'geometry'] = polygon
    return gdf


def crop_from_shapefile(geotiff_path, shapefile_path, save_path, filename = "python_cropped.tif"):
    # Reference from terminal command:
    #
    # gdalwarp -t_srs EPSG:32617 -of GTiff -cutline 
    # "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/rectangle.shp" 
    # -cl rectangle -crop_to_cutline 
    # "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/odm_orthophoto.original.tif" 
    # "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/cropped_orthophoto.tif"
    #
    # Command line documentation: https://gdal.org/programs/gdalwarp.html
    # Python implementation documentation (WarpOtions(), Warp()): https://gdal.org/python/osgeo.gdal-module.html#WarpOptions  
    # Python example implementation: https://www.programcreek.com/python/example/116446/gdal.Warp 

    geotiff = gdal.Open(geotiff_path)

    args = gdal.WarpOptions(
        dstSRS = "EPSG:32617",
        format = "GTiff",
        cutlineDSName = shapefile_path,
        cropToCutline = True
    )

    gdal.Warp(save_path + filename, geotiff, options = args)

    print("Cropped, saved at " + save_path + filename)


def run(map_center_coordinates, map_height):
    pass

if __name__ == "__main__":
    latlon_center = (28.039819, -82.697501)
    width = 45
    height = 80
    path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/"
    # write_shapefile(latlon_center, width, height, path)

    cropped_save_path = path
    shapefile_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/python_rect.shp"
    geotiff_path = "/Users/gjtiquia/Documents/GJ MacBookPro Documents/FYP Mapping/QGIS_sheffield_park_2_v2/odm_orthophoto.original.tif"
    # crop_from_shapefile(geotiff_path, shapefile_path, cropped_save_path)
    crop_from_shapefile(geotiff_path, shapefile_path, cropped_save_path, filename="test.tif")

    

