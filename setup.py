"""
mutexlock
============

A python locking implementation using mutex
"""

from setuptools import setup
from setuptools import find_packages

version = '1.0'

setup(
    name='mutexlock',
    version=version,
    description="A python locking implementation using mutex",
    long_description=__doc__,
    classifiers=[],
    # Get strings from
    #http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='https://github.dtc.avira.com/VDT/mutexlock',
    license='GPL',
    packages=['mutexlock'],
    include_package_data=True,
    zip_safe=False,
)
