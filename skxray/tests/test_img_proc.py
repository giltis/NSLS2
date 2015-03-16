# Module for the BNL image processing project
# Developed at the NSLS-II, Brookhaven National Laboratory
# Developed by Gabriel Iltis, Sept. 2014
"""
This module contains test functions for the file-IO functions
for reading and writing data sets using the netCDF file format.

The files read and written using this function are assumed to
conform to the format specified for x-ray computed microtomorgraphy
data collected at Argonne National Laboratory, Sector 13, GSECars.
"""

import numpy as np
import six
from nose.tools import eq_
from skxray.img_proc import mathops
from numpy.testing import assert_equal
