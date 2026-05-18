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

''' 2. linspace() :
    Function
    Syntax : np.linspace(start, stop, num=50, endpoint=True, restep(optional)...)
             start: Starting value.
             stop: End value.
             num: Number of samples to generate.
             endpoint = True (default) : If True includes stop value too for displaying in result
                                         If false excldes the stop value from displaying as result
             restep = True : If set to true shows the (samples, spacing between them done)

    Internal help of linespace() function :
    - We can safely pass them as positional Args or keyword Args 
        - if positional Args pass it as (start,stop,num)
        - if keyword Args pass it as (start,stop,num = value)
    - Even if start and stop are given as int's NumPy immediately handles them as floating-point numbers (1.0 and 2.0) behind the scenes.
    - Because dividing an interval into equal "cuts" almost always results in decimal values (for example, 1.25, 1.5, 1.75), the np.
    - linspace function is explicitly designed to always return a numpy.
    - ndarray with a floating-point data type (float64) by default.

    Return Type: numpy.ndarray which conatin the splitting of number line from start to stop on specified num of value
                
            - The endpoint = True vs endpoint = False upon comparison adoesnt yield same outputs, the space between number changes.
                when endpoint is default
                 start = 1, stop = 2 ,num(number of cuts) : 4
                 output : array([1.  , 1.25, 1.5 , 1.75, 2.  ])

                when enpoint = False is set
                  - the start = 1 , stop = 2 and nums = 5(given)
                  - In this case when endpoint is false nums taken as nums+1 = 6
                  - does 6 equal cuts from 1 to 2 [1. ,1.2, 1.4, 1.6, 1.8, 2.0] 
                  - From this 6 cuts it excludes last one 2.0 and displays [1. , 1.2, 1.4, 1.6, 1.8]
                  - This rule is followed when endpoint is false and also the numberline from previous i.e, when endpoint = True(default)
                    that result and this result won't match it will be completely different.
'''
arr_linespace1 = np.linspace(1,2,num = 5) # can specify num = 5 or simply 5
arr_linespace2 = np.linspace(1,2,5,endpoint=False) # 2 is not considered but still it does 5 equal cuts from 1 till before 2
arr_linespace3 = np.linspace(1.0,2.0,5,retstep=True)  # displays the samples, space_size
arr_linespace4 = np.linspace(1.0, 2.0, 5,endpoint=False,retstep=True)

print(arr_linespace1)  # array([1.  , 1.25, 1.5 , 1.75, 2.  ])
print(arr_linespace2)  # array([1. , 1.2, 1.4, 1.6, 1.8]) --> takes num = num + 1 does 6 cuts but choose first 5 as display
print(arr_linespace3) # (array([1.  , 1.25, 1.5 , 1.75, 2.  ]), np.float64(0.25))
print(arr_linespace4)  # (array([1. , 1.2, 1.4, 1.6, 1.8]), np.float64(0.2))

''' Constant and Placeholder Array : '''
''' 1. zeros()
    Function
    Syntax : np.zeros(shape, dtype=float, ...)
            shape: Integer or tuple of integers defining array dimensions.
                  for 1D array :
                     np.zeros(5) --> all the 5 values are float values "0."
                  for N-D array :
                     np.zeros((3,3)) --> produces a matrix 3*3 toatl 9 values with 0. values
                                         the output form is [[],[],[]] --> N-D array wrapped in array  
    Return Type: numpy.ndarray filled with zeros.
'''
arr_zero1 = np.zeros(5)
arr_zero2 = np.zeros((3,3))
print(arr_zero1)
print(arr_zero2)

''' 2.ones() :
    Function
    Syntax : np.ones(shape, dtype=float, ...)
            shape: Integer or tuple of integers defining array dimensions.
                  for 1D array :
                     np.zeros(5) --> all the 5 values are float values "1."
                  for N-D array :
                     np.zeros((3,3)) --> produces a matrix 3*3 toatl 9 values with 1. values
                                         the output form is [[],[],[]] --> N-D array wrapped in array  
    Return Type: numpy.ndarray filled with zeros.
'''
arr_ones1 = np.ones(5)
arr_ones2 = np.ones((2,4))

print(arr_ones1)
print(arr_ones2)

''' 3.full() :
    Function
    Syntax : np.full(shape, fill_value, dtype=None, ...)
             shape: Dimensions of the array.
             fill_value: Scalar value to fill the array.
             dtype = None : Automatically identifies the fill value data types and fill in the same type for dimension specified.
    Return : numpy.ndarray filled with fill_value.
'''
arr_full1 = np.full(5,2) #1D - 5 Values with all have 2
arr_full2 = np.full((2,3),1.5) # 2D - Matrix with all the values as 1
print(arr_full1)
print(arr_full2)

