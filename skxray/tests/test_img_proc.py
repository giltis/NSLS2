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
from numpy.testing import assert_equal, assert_raises


test_array_1 = np.zeros((30,30,30), dtype=int)
test_array_1[0:15, 0:15, 0:15] = 1
test_array_2 = np.zeros((50, 70, 50), dtype=int)
test_array_2[25:50, 25:50, 25:50] = 87
test_array_3 = np.zeros((10,10,10), dtype=float)
test_array_4 = np.zeros((100,100,100), dtype=float)
test_array_5 = np.zeros((100,100), dtype=int)
test_array_5[25:75, 25:75] = 254

test_1D_array_1 = np.zeros((100), dtype=int)
test_1D_array_2 = np.zeros((10), dtype=int)
test_1D_array_3 = np.zeros((100), dtype=float)

test_constant_1 = 5
test_constant_2 = 2.0
test_constant_3 = 1


def test_array_size_check(test_array_1, test_array_2):
    """
    Test function for netCDF read function load_netCDF()

    Parameters
    ----------
    test_data : str

    Returns
    -------

    """
    assert_equal(mathops._check_array_size(test_array_1, test_array_2),
                 (True, True, (50, 70, 50)))


def test_apply_constant(test_array_1, test_constant_1):
    """
    Test function for netCDF read function load_netCDF()

    Parameters
    ----------
    test_data : str

    Returns
    -------

    """
    #Int array vs Int constant
    assert_equal(mathops._check_array_size(test_array_1, test_constant_1),
                 (True, False, (30, 30, 30)))
    #Int vs Float
    assert_raises(TypeError, mathops._check_array_size(test_array_1,
                                                       test_constant_2))
    #Float vs Float
    assert_equal(mathops._check_array_size(test_array_3, test_constant_2),
                 (True, False, (100, 100, 100)))
