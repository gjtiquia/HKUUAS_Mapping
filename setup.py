import setuptools
from setuptools import find_packages

# Load the README and requirements
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name = 'HKUUAS_Mapping',
    version = '1.0.0',
    description = '[DESCRIPTION]',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url = '#',
    install_requires=required,
    author = 'GJTiquia',
    author_email = 'gershom.tiquia@gmail.com',
    package_dir = {
            '': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    zip_safe = False
)