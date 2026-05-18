import numpy as np
import random
''' From Python Structures : '''
''' 1. array() :
    Function 
    Syntax : np.array(object,dtype = None)
             object : Any iterable data structure like list,tuple(use for numericals especially we can still pass string it accepts.)
             dtype = None (optional) : The data type (like integer or float) is automatocally guessed when dtype = None.
    output : numpy.ndarray filled with input data
'''
arr_list = np.array([1,2,3,4])
arr_tuple = np.array((10,20,30))
print(arr_list)
print(arr_tuple)

''' Using Numerical Ranges : '''
''' 1. arange() :
    Function
    Syntax : np.arange(start, stop, step, dtype = None)
             start: Start of interval (defaults to 0).
             stop: End of interval (exclusive).
             step: Spacing between values. (default to 0)
    output : numpy.ndarray of evenly spaced values.
'''
arr_range1 = np.arange(11) # 0,1,2,3,4,5,6,7,8,9,10
arr_range2 = np.arange(1,6) # 1,2,3,4,5
arr_range3 = np.arange(0,11,2) #0,2,4,6,8,10
print(arr_range1)
print(arr_range2)
print(arr_range3)

