#!/Users/gjtiquia/.local/share/virtualenvs/Python_Testing-imFNgP0c/bin/python

import sys
# import osgeo_utils.gdalcompare as a convenience to use as a script
from osgeo_utils.gdalcompare import *  # noqa
from osgeo_utils.gdalcompare import main
from osgeo.gdal import deprecation_warn


deprecation_warn('gdalcompare')
sys.exit(main(sys.argv))