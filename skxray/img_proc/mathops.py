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


def _check_array_size(input_1, input_2):
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
    input_1 : {ndarray, int, float}
    Array containing 2D or 3D image data that will be comparatively analyzed
    or applied to a separate ndarray. This input could also, potentially, 
    be an integer or float constant to be applied to input_2.

    input_2 : {ndarray, int, float}
    The second array to which input_1 will be applied, compared or combined.
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
    if type(input_1) or type(input_2) != numpy.ndarray:
        # Determine whether one of the inputs is an ndarray, and if so,
        # then which one.
        for input_obj in [input_1, input_2]:
            if type(input_obj) == numpy.ndarray:
                array_obj = input_obj
            if type(input_obj) != numpy.ndarray:
                constant_obj = input_obj
        # Confirm that dtypes match. If they don't then raise an error
        if type(constant_obj) != array_obj.dtype:
            raise TypeError("The data types do not match. Please check your "
                            "input data and convert the erroneous input to "
                            "the desired data type.")
        valid_operation = True
        resize_arrays = False
        corrected_dims = array_obj.shape
    # Verify that the input arrays have equivalent demensionality
    elif len(input_1.shape) != len(input_2.shape) and \
            (len(input_2.shape) and input_2.shape[0] != 1):
        valid_operation = False
        resize_arrays = True
        logging.warning("Array dimensions do not match. Reevaluate input "
                         "arrays and modify as necessary before applying "
                         "image arithmetic operations. Example: Input array "
                         "#1 is 2D (len(array1.shape) = 2), and Input array "
                         "#2 is 3D (len(array2.shape) = 3)")
    # If input data is 1-dimensional then raise warning, as 1-dimensional
    # image data sets are atypical.
    elif len(input_1.shape) and len(input_2.shape) == 1:
        valid_operation = True
        resize_arrays = False
        corrected_dims = input_1.shape
        logging.warning("Input arrays are 1-dimensional. While the input "
                        "arrays may contain valid image data, this format "
                        "is atypical (as most image data being processed "
                        "is to be evaluated using 2D or 3D image arrays.")
    # Determine whether dimensions for the two input arrays are equal. If
    # they're not then evaluate the array size which will contain both
    # arrays, thereby allowing for image arithmetic operations.
    elif input_1.shape != input_2.shape:
        if len(input_1.shape) and len(input_2.shape) == 1:
            corrected_dims = (np.amax((input_1.shape[0],
                                       input_2.shape[0])))
        elif len(input_1.shape) and len(input_2.shape) == 2:
            corrected_dims = (np.amax((input_1.shape[0],
                                       input_2.shape[0])),
                              np.amax((input_1.shape[1],
                                       input_2.shape[1])))
        elif len(input_1.shape) and len(input_2.shape) == 3:
            corrected_dims = (np.amax((input_1.shape[0],
                                       input_2.shape[0])),
                              np.amax((input_1.shape[1],
                                       input_2.shape[1])),
                              np.amax((input_1.shape[2],
                                       input_2.shape[2])))
        valid_operation = True
        resize_arrays = True
    elif input_1.shape == input_2.shape:
        valid_operation = True
        resize_arrays = False
        corrected_dims = input_1.shape
    return valid_operation, resize_arrays, corrected_dims
