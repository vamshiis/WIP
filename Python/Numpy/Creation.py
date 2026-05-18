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


