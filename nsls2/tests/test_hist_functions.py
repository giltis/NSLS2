
#TODO: Need to sort out tests for each function and operation as a whole.
import numpy as np
import nsls2.img_proc.histops as histops
from histops import rescale_intensity_values as rscale
from nsls2.core import bin_1D
from nsls2.core import bin_edges_to_centers
from nose.tools import assert_raises
from numpy.testing import assert_array_almost_equal

%load_ext autoreload
%autoreload 2

#Test case number 1: float values ranging from 0 to 1
test_1 = np.zeros(7)
test_1[0:5] = np.random.rand(5)
test_1[6] = 1.0
test_2 = np.array([0.10549548,
                         0.18549702,
                         0.64457573,
                         0.89678006,
                         0.37372467,
                         0.,
                         1.,
                         0.92712985,
                         0.06273057,
                         0.98712985])
test_3 = test_2 * 10000
test_4 = (test_2 - 0.3) * 12000
test_5 = np.floor(test_2*10)
#Large test arrays
test_5 = np.random.rand(5,5,5)


def get_base_test_array():
    test_array = np.random.rand(5,5,5)
    return test_array


def test_rescale_intensity_values_flt2int():
    base_test_array = get_base_test_array()
    small_flt_test = base_test_array
    lrg_flt_test = base_test_array*10000
    end_ranges = [(-5.0,5.0), (-32000.0,32000.0), (0,1)]
    initial_values_list = [small_flt_test, lrg_flt_test]
    for i in initial_values_list:
        for f in end_ranges:
            rescale_1 = histops.rescale_intensity_values(i,
                                                         new_max=np.amax(f),
                                                         new_min=np.amin(f),
                                                         out_dType=f.dtype)
            rescale_2 = histops.rescale_intensity_values(rescale_1,
                                                         new_max=np.amax(i),
                                                         new_min=np.amin(i),
                                                         out_dType=i.dtype)
            assert_equals(rescale_2 == i)


def test_rescale_intensity_values_int2int():
    base_test_array = get_base_test_array()
    small_int_test = np.floor(base_test_array*5)
    med_int_test = np.floor(base_test_array*255)
    lrg_int_test = np.floor(base_test_array*10000)
    end_ranges = [(0,3), (1,10), (-5000, 12000), (0,255)]
    histops.rescale_intensity_values


def test_rescale_intensity_values_int2flt():
    base_test_array = get_base_test_array()
    small_int_test = np.floor(base_test_array*5)
    med_int_test = np.floor(base_test_array*255)
    lrg_int_test = np.floor(base_test_array*10000)
    end_ranges = [(-5.0,5.0), (-32000.0,32000.0), (0,1)]
    histops.rescale_intensity_values

