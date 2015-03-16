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


def test_array_size_check():
    """
    Test function for netCDF read function load_netCDF()

    Parameters
    ----------
    test_data : str

    Returns
    -------

    """
    test_array_1 = np.zeros((30,30,30), dtype=int)
    test_array_1[0:15, 0:15, 0:15] = 1
    test_array_2 = np.zeros((50, 70, 50), dtype=int)
    test_array_2[25:50, 25:50, 25:50] = 87

    # Test correct operation: 2 int arrays of different size
    assert_equal(mathops._check_array_size(test_array_1, test_array_2),
                 (True, True, (50, 70, 50)))
    # Test for arrays with equal dimensionality
    assert_equal(mathops._check_array_size(test_array_1, test_array_1),
                 (True, False, (30, 30, 30)))


def test_apply_constant():
    """
    Test function for netCDF read function load_netCDF()

    Parameters
    ----------
    test_data : str

    Returns
    -------

    """
    test_array_int = np.zeros((30,30,30), dtype=int)
    test_array_int[0:15, 0:15, 0:15] = 1

    test_array_flt = np.zeros((10,10,10), dtype=float)

    test_constant_int = 5
    test_constant_flt = 2.0

    #Int array vs Int constant
    assert_equal(mathops._check_array_size(test_array_int, test_constant_int),
                 (True, False, (30, 30, 30)), "Test: Integer array coupled "
                                              "with an integer constant, "
                                              "has failed. Something in the "
                                              "helper function "
                                              "_check_array_size has changed "
                                              "and is generating this error.")
    #Data type mismatch
    assert_raises(TypeError,
                  mathops._check_array_size,
                  test_array_int,
                  test_constant_flt)
    #Float vs Float
    assert_equal(mathops._check_array_size(test_array_flt, test_constant_flt),
                 (True, False, (10, 10, 10)), "Test: Float array coupled "
                                              "with a float constant, "
                                              "has failed. Something in the "
                                              "helper function "
                                              "_check_array_size has changed "
                                              "and is generating this error.")
