#! /bin/sh
pip install .

cd GDAL-3.4.2
python setup.py build
python setup.py install