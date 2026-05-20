import numpy as np

''' - Has feature to auto upcast if any single float value is given in list or matrix.
    - so if a matrix is given array [[1,2,3],[4,5,6.0]] --> this has a float64 of 6.0 value 
    - If we print the array.dtype it will give us float64 instead of int64
    - because there is an internal casting will auto cast every integer value to float 
    - think if there is 6.5 the 0.5 value will be lost if it auto cast this float to int
    - Because of data lose scope even if there is single float and all are integers it will auto cast them to float64 instead of int64
'''
''' 1. shape :
    Attribute (property of the array object)
    Syntax : object_name.shape
    Return : A tuple of integers
    - Reads the dimension of the array
    - array = [...] = 1 pair of brackets = 1D array --> output : (elements,)
    - array = [[..]] = 2 pairs of brackets = 2D array --> output: (rows, columns)
    - array = [[[...]]] = 3 pairs of brackets = 3D array  --> output : (depth, rows, columns)
                          depth : Inner 2D arrays
                          rows  : Number of rows inside the 2D array
                          columns Number of colums in a row
                          Note : There can't be inhomogenous structure so make equal rows and columns inside each 2D array.


'''
array1 = np.array([1, 2, 3, 4])
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9.]])
array3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [1,2,3]
    ]
]) # --> consist 2 2D inside it, inside it we have 2 rows and 3 columns. 

print(array1.shape)
print(array2.shape)
print(array3.shape)

''' dtype :
    Attribute
    Syntax : object_name.dtype
    Return : returns a Numpy dtype object (e.g., dtype('int64'))
    - If there is even one float value in any of the array it returns a float64.
    Homogeneity Limit: NumPy arrays can only hold one data type. If you try to mix integers and strings, 
                       NumPy will quietly upcast everything to strings (<U21), breaking math operations downstream.
'''
arr_auto_str = np.array([[1,2,'hi',4],['dg','ki','kk',6]]) # Converts everything to String and retirns to <U21 as output.
print(array1.dtype)
print(array2.dtype)
print(array3.dtype)
print(arr_auto_str.dtype)
print(arr_auto_str)


''' reshape() :
    Object Method & Function
    Method_Syntax : object.reshape(row,column)
    Function_Syntax : np.reshape(array_object,(row,column)) 
                      -> we can pass single value(N,)(N is total no.of values) to reshape and create 1D shape. 
                      -> or -1 simply to convert to 1D shape if the input was 2d structure.
    Return : A new ndarray object and the object will be view of original.
    - the number of elements you having currently should form the same n*n matrix by it.
    - Be it N dimension but the total elements you have should be equal to final shape you form.
    - we can pass -1 to either row or column (choice only any one of them) so it automatically calculates for you.
       Ex : you have 6 elements
            if you pass (3,-1) => 3 rows and 2 columns(auto calculated)
            if you pass (-1,3) => 3 columns and 2 rows (auto calculated)
        The calculation will be dynamic based on the value you gave and the total elements you have.
    - If the reshape is used on 1D array like [1,2,3,4,5,6] total = 6 elements
        so you can form 2D matrix of 2*3 or 3*2 matrix 
        if you try to do 1*2 it will be total length = 2 but you have 6 it doesnt satisfy just.
        so it throws "ValueError"
    - Since its a view of original array any changes you commit with reshaped object it will reflect in original too.
    Memory Behavior (The Big Trap): It returns a View whenever possible. This means if you change a value in the reshaped array, the original array changes too.
     It only makes a copy if the data layout in memory forces it to (non-contiguous memory).
'''
original = np.array([1, 2, 3, 4, 5, 6])

reshape_function = np.reshape(original,(-1,2)) # if original is 2D array simply pass -1 to get 1D array
reshaped_1 = original.reshape(2,3)
reshaped_2 = original.reshape(-1,2) # does calculates the row size automatically based on total length you have here it will do 3 for row.

# VIEW warning Proof
# This will reflect in reshaped_1 and original too as.
# Because reshape() gets the view of actual array not by copying it.
# Be careful when you mutate a reshaped data.
reshaped_2[1,1]  = 44 # 4 -> 44
print(reshaped_1)
print(reshaped_2)
print(original)


''' flatten() vs ravel() :
    Object Method
    Syntax flatten : array_object.flaten()
    Syntax ravel   : array_object.ravel()
    Return : Both return an 1D ndarray
    - flatten() method copies the original array and returns it.
      - Always allocates new memory and returns a Copy. 
      - Safe, but slow on massive datasets.
      - If massive amount of data needs to be mutate the data use flatten() method to copy and mutate.
    - ravel() method returns the view of the original object itself.
       - Attempts to return a View whenever possible. 
       - Extremely fast because it doesn't duplicate data.
       - Massive amount of data is there and you just need to read the values and feed into models use ravel() method.
'''
matrix = np.array([[1, 2], [3, 4]])

flat_copy = matrix.flatten()
flat_copy[0] = 90
print(flat_copy) # return 1D array with the mutation done on flat array not on original array
print(matrix)

flat_view = matrix.ravel()
flat_view[0] = 100 # Mutates the original array 
print(flat_view)
print(matrix)


