#from setuptools import setup
from distutils.core import setup

long_description = open('README.md', 'r').read()

setup(
    name='parseidf',
    py_modules=['parseidf'],  # this must be the same as the name above
    version='1.0.0',
    description='A module for parsing EnergyPlus IDF files',
    long_description=long_description,
    author='Daren Thomas',
    author_email='dthomas.ch@gmail.com',
    url='https://github.com/daren-thomas/parseidf',
    #download_url=
        #'https://github.com/daren-thomas/parseidf/archive/master.tar.gz',
    keywords=['simulation', 'parsing', 'energyplus'],  # arbitrary keywords
    requires=['ply'],
    classifiers=[],
)
