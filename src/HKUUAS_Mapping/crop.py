import geopandas as gpd
import utm
from shapely.geometry import Polygon
from osgeo import gdal
from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info

def get_utm_espg_code(latlon: tuple) -> int:
    # Reference from pyproj documentation: 
    # https://pyproj4.github.io/pyproj/stable/examples.html#find-utm-crs-by-latitude-and-longitude 
    utm_crs_list = query_utm_crs_info(
        datum_name="WGS 84",
        area_of_interest=AreaOfInterest(
            west_lon_degree = latlon[1],
            south_lat_degree = latlon[0],
            east_lon_degree = latlon[1],
            north_lat_degree = latlon[0],
        ),
    )
    utm_crs = CRS.from_epsg(utm_crs_list[0].code)
    epsg_code = utm_crs.to_epsg()

    print("EPSG:" + str(epsg_code))

    return epsg_code


def read_shapefile(path):
    gdf = gpd.read_file(path)
    return gdf


def write_shapefile(epsg_code: int, center: tuple, width: float, height: float, path: str, filename = "Rectangle.shp") -> str:
    utm_center = utm.from_latlon(center[0], center[1])
    utm_x = utm_center[0]
    utm_y = utm_center[1]
    
    x_offset = height / 2.0
    y_offset = width / 2.0

    points = [(-x_offset, -y_offset), (-x_offset, y_offset), (x_offset, y_offset), (x_offset, -y_offset), (-x_offset, -y_offset)]
    coordinates = [(i[0] + utm_x, i[1] + utm_y) for i in points]

    shapefile = create_polygon(coordinates, "Rectangle", epsg_code)
    shapefile.to_file(path + filename)

    print("Shapefile written and saved at " + path + filename)

    return path + filename


def create_polygon(coordinates, polygon_name, epsg):
    ''' Create a polygon from coordinates '''
    polygon = Polygon(coordinates)
    gdf = gpd.GeoDataFrame(crs = {'init' :'epsg:' + str(epsg)})
    gdf.loc[0,'name'] = polygon_name
    gdf.loc[0, 'geometry'] = polygon
    return gdf


def crop_from_shapefile(epsg_code: int, geotiff_path: str, shapefile_path: str, save_path: str, filename = "cropped_map.tif"):
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
        dstSRS = "EPSG:" + str(epsg_code),
        format = "GTiff",
        cutlineDSName = shapefile_path,
        cropToCutline = True
    )

    gdal.Warp(save_path + filename, geotiff, options = args)

    print("Map cropped, saved at " + save_path + filename)


def run(geotiff_path, save_directory, map_center_coordinates, map_height):
    # Required ratio is 16:9
    map_width = 9 * map_height / 16

    # Get UTM EPSG code from latitude and longtitude coordinate
    epsg_code = get_utm_espg_code(map_center_coordinates)

    shapefile_path = write_shapefile(epsg_code, map_center_coordinates, map_width, map_height, save_directory)
    crop_from_shapefile(epsg_code, geotiff_path, shapefile_path, save_directory)


    

