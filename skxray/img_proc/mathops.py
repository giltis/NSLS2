# Module for the BNL image processing project
# Developed at the NSLS-II, Brookhaven National Laboratory
# Developed by Gabriel Iltis, Oct. 2013
"""
# This module contains the tools and functions required for basic image
arithmetic and logical operations. While the tools included are able to be
executed at the python interpreter prompt, or as part of a image processing
python script, the module has been designed to facilitate image arithmetic
and logical operations on image data sets in the VisTrails workflow manager.
"""

import numpy as np
import logging


def _check_array_size(array_1, array_2):
    """
    This helper function is designed to ensure that input arrays have
    equivalent dimensions. Since arithmetic operations generate an error if
    there is a size mismatch, this function notifies the user of mismatch
    and returns a set of axial dimensions that will enable additional
    analysis of the source data sets. A separate helper function is
    available to actually resize the source arrays as this is beyond the
    scope of this tool.

    Parameters
    ----------
    array_1 : ndarray
    Array containing 2D or 3D image data that will be comparatively analyzed
    or applied to a separate ndarray.

    array_2 : {ndarray, int, float}
    The second array to which array_1 will be compared or combined.
    Alternatively, this input can also be a constant to which the first
    input array will be applied.

    Returns
    -------
    valid_operation : bool
    A True/False key switch used to specify whether the input arrays or
    constants can be used for image arithmetic. If this value evaluates to
    False then the dtypes for the input values do not match, or array
    dimensionality does not match (e.g. a 2D array is being used to modify a
    3D array).

    resize_arrays : bool
    A True/False key switch used to specify whether arrays must be resized
    using the returned corrected_dims data. If resize_arrays equals False,
    then the second input array is either a constant, or has the same axial
    dimensions as the first input array.

    corrected_dims : tuple
    Returns a tuple containing the minimum axial dimensions required in
    order to evaluate or modify the input data (arrays or constants). The
    tuple takes the form of (y_dim, x_dim) for evaluation of 2D data sets,
    or (z_dim, y_dim, x_dim) for 3D data sets.
    """
    # Check to make sure that arithmetic operation does not involve
    # application of a constant value
    if len(array_2.shape) and array_2.shape[0] == 1:
        valid_operation = True
        resize_arrays = False
        corrected_dims = array_1.shape
    # Verify that the input arrays have equivalent demensionality
    elif len(array_1.shape) != len(array_2.shape) and \
            (len(array_2.shape) and array_2.shape[0] != 1):
        valid_operation = False
        resize_arrays = True
        logging.warning("Array dimensions do not match. Reevaluate input "
                         "arrays and modify as necessary before applying "
                         "image arithmetic operations. Example: Input array "
                         "#1 is 2D (len(array1.shape) = 2), and Input array "
                         "#2 is 3D (len(array2.shape) = 3)")
    # Determine whether dimensions for the two input arrays are equal. If
    # they're not then evaluate the array size which will contain both
    # arrays, thereby allowing for image arithmetic operations.
    elif array_1.shape != array_2.shape:
        if len(array_1.shape) and len(array_2.shape) == 1:
            valid_operation = True
            resize_arrays = True
            corrected_dims = (np.amax((array_1.shape[0],
                                       array_2.shape[0])))
        elif len(array_1.shape) and len(array_2.shape) == 2:
            valid_operation = True
            resize_arrays = True
            corrected_dims = (np.amax((array_1.shape[0],
                                       array_2.shape[0])),
                              np.amax((array_1.shape[1],
                                       array_2.shape[1])))
        elif len(array_1.shape) and len(array_2.shape) == 3:
            valid_operation = True
            resize_arrays = True
            corrected_dims = (np.amax((array_1.shape[0],
                                       array_2.shape[0])),
                              np.amax((array_1.shape[1],
                                       array_2.shape[1])),
                              np.amax((array_1.shape[2],
                                       array_2.shape[2])))
    elif array_1.shape == array_2.shape:
        valid_operation = True
        resize_arrays = False
        corrected_dims = array_1.shape
    return valid_operation, resize_arrays, corrected_dims
