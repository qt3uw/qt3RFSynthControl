# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_namespace_packages
from src.qt3rfsynthcontrol.__version__ import __version__

requirements = [
    'windfreak',
]

with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name='qt3rfsynthcontrol',
    version=__version__,
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},  # same
    package_data={'': ['README.md'],
                  },
    description='A package for controlling the Windfreak SynthHD RF generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gadamc/qt3rfsynthcontrol',

    license='GPLv3',  # License tag
    install_requires=requirements,  # package dependencies
    python_requires='~=3.8',  # Specify compatible Python versions
)
