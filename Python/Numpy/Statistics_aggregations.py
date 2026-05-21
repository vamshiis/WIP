import numpy as np
''' axis : 
    An Axis represents a specific directional path or dimension inside a NumPy array. 
    Axes are numbered starting from 0 based on their index position in the array's shape tuple.
    Core Usage :
      - When applied to statistical aggregation functions (like sum, mean, max, or std), the axis parameter specifies which dimension to target, collapse, and eliminate.
      - Without keepdims=True: The targeted axis is completely deleted from the final shape tuple.
      - With    keepdims=True: The targeted axis is preserved but its size is forced down to 1.

    About Aggregate function : 
    - All Aggregate function like mean, are universal as well as methods on the array_objects.
    - so we can use any one of them to do the same work.
    
    1D array : Has only axis = 0 as all elements are in form of single row(don't think its a row) sits on x-axis.
    Syntax : np.aggregate_function(array,axis=0,keepdims=False) (or) array_object.sum(axis=0,keepdims = False)
             - By default we have keepdims = False no need to write again we need to pass keyword Argument only to make it True --> (keepdims = True)

    Return : Without keepdims=True: Returns a Scalar (a single, raw numeric value like 15).
             With    keepdims=True: Returns a 1D array with a single element, shape (1,).

    Internal Execution and understanding : 
     - A 1D array only has one dimension (Axis 0). 
     - It is a simple line of elements. 
     - Because there are no other directions, axis=0 targets the entire line, squishing every element together into one single point.
'''
arr_1d = np.array([10, 20, 30, 40, 50]) #shape : (5,) -> 1D array containing 5 elements

# --- WITHOUT keepdims=True ---
res_normal = arr_1d.sum(axis = 0)
print("Normal Result:", res_normal)        # Output: 150
print("Normal Shape :", np.shape(res_normal))  # () --> means a pure scalar value 

res_keep = np.sum(arr_1d,axis=0,keepdims=True)
print("Keepdims Result:", res_keep)        # Output: [150]
print("Keepdims Shape :", res_keep.shape) # (1,) -> 1D array containing 1 Element

''' 2D array : Has axis=0 and 1 
               Where axis = 0 comtains the row elements residing on x-axis
                     axis = 1 contains the column elements residing on y-axis
    Syntax : array.aggregate_function(axis=0 or 1, keepdims = True(optional))

    Return :
    Without keepdims=True: Drops the targeted dimension completely. 
                           Returns a flat 1D array.
    With    keepdims=True: Replaces the targeted dimension with 1. 
                           Returns a 2D matrix of shape (1, Columns) or (Rows, 1).
    Understanding and execution : 
    axis=0 (Row Smasher): 
       - Moves vertically down through the rows. 
       - It collapses all rows into a single baseline row. 
       - The original number of columns remains.
    axis=1 (Column Smasher): 
       - Moves horizontally across the columns. 
       - It collapses all columns into a single vertical column. 
       - The original number of rows remains.
'''

matrix_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # Shape: (2, 3) -> 2 Rows, 3 Columns

# === AXIS 0 (SMASH ROWS DOWN) ===
# Normal: Drops row dim -> (3,)
print("Axis 0 Normal:", matrix_2d.sum(axis=0))        # output : [5 7 9]
print("Shape Normal :", matrix_2d.sum(axis=0).shape)  # output : (3,)

# Keepdims: Replaces row dim with 1 -> (1, 3)
print("Axis 0 Keep  :", matrix_2d.sum(axis=0,keepdims=True))  # Output: [[5 7 9]]
print("Shape Keep   :", matrix_2d.sum(axis=0,keepdims=True).shape)  # Output: (1, 3)


# === AXIS 1 (SMASH COLUMNS LEFT) ===
# Normal: Drops col dim -> (2,)
print("Axis 1 Normal:", matrix_2d.sum(axis=1))         # Output: [6 15]
print("Shape Normal :", matrix_2d.sum(axis=1).shape)   # Output: (2,)

# Keepdims: Replaces col dim with 1 -> (2, 1)
print("Axis 1 Keep  :\n", matrix_2d.sum(axis=1, keepdims=True))
# Output:
# [[ 6]
#  [15]]
print("Shape Keep   :", matrix_2d.sum(axis=1, keepdims=True).shape)  # Output: (2, 1)

print(matrix_2d.strides)
''' 3D array : Has axis 0,1,2
                array.sum(axis=0)  # Targets Layers
                array.sum(axis=1)  # Targets Rows
                array.sum(axis=2)  # Targets Columns
    Syntax : array_object.aggregate_function(axis = value, keepdims = True(optional)) 

    Return:
    Without keepdims = True: 
     - Drops the targeted dimension completely.
     - Returns a standard 2D array.
    With keepdims = True: 
     - Replaces the targeted dimension with 1.
     - Returns a 3D array with shapes (1, Rows, Columns), (Layers, 1, Columns), or (Layers, Rows, 1).      

    Internal Execution and understanding : 3D Array --> (layer,row,column)
    - Assume in graph structure as (easier draw a three dimension on graph to understand better)
                layer   => depth(No.of 2d arrays)
                        => sits on z-axis
                        => each 2D array is stacked behind each other on the z-axis
                        => when axis = 0 given all layers position values are just aggregated 
                        => returns the columns,rows i.e all layers are combined into one 
                row     => no.of rows in 2d array(shld be same in N-layers)    
                        => sits on x-axis
                        => each row of the 2d array are already placed on x-axis when you place the layers on z-axis
                        => when axis = 1 given each layers column's row's are shrinked from top to down resulting one value per column
                        => results layer,column in shape i.e, all layers rows are combined
                columns => no.of columns in 2d array(shld be same in N-layers)
                        => sits on y-axis
                        => each column of 2nd array are already placed on y-axis when you place layers on z-axis
                        => when axis = 1 is given each layer row's column's are shrinked from right to left resulting one value per row 
                        => results layers,rows in shape i.e, all layers columns are combined
    Imagine a multi-story building. 
    axis=0 (Layer Smasher): 
     - Axis 0 drops the top floors straight down into the ground floor. 
     - The elements align perfectly by floor position and combine. Layers disappear; a 2D floor layout remains.
     - Returns 
    axis=1 (Row Smasher):
     - Stands on each floor separately. 
     - Within each floor, it pushes all the rows forward into a single row.
     - Retuns the layer,column of the array (if keepdims = False)
     - Returns the layer,1,column of the array (if keepdims = True)

    axis=2 (Column Smasher):
      Stands on each floor separately.
      Within each individual row, it pushes all the columns from right-to-left into a single column.         
'''

# Shape: (2, 2, 3) -> 2 Layers, 2 Rows, 3 Columns
matrix_3d = np.array([
    [[1, 1, 1], [2, 2, 2]],  # Layer 0
    [[3, 3, 3], [4, 4, 4]]   # Layer 1
])

# === AXIS 0 (SMASH LAYERS TOGETHER) ===
# Layer 0 adds to Layer 1 element-by-element. (2, 2, 3) -> (2, 3)
print("Axis 0 Normal:\n", matrix_3d.sum(axis=0))
# Output: [[4 4 4]
#          [6 6 6]]

# Keepdims: (2, 2, 3) -> (1, 2, 3)
print("Axis 0 Keep : \n", matrix_3d.sum(axis=0, keepdims=True))
print("Axis 0 Keep Shape:", matrix_3d.sum(axis=0, keepdims=True).shape)


# === AXIS 1 (SMASH ROWS WITHIN EACH LAYER) ===
# Rows compress vertically on each floor. (2, 2, 3) -> (2, 3)
print("Axis 1 Normal:\n", matrix_3d.sum(axis=1))
# Output: [[3 3 3]    <- Layer 0 rows combined (1+2)
#          [7 7 7]]   <- Layer 1 rows combined (3+4)

# Keepdims: (2, 2, 3) -> (2, 1, 3)
print("Axis 1 Keep :\n", matrix_3d.sum(axis=1, keepdims=True))
print("Axis 1 Keep Shape:", matrix_3d.sum(axis=1, keepdims=True).shape)


# === AXIS 2 (SMASH COLUMNS WITHIN EACH ROW) ===
# Columns compress horizontally inside each row. (2, 2, 3) -> (2, 2)
print("Axis 2 Normal:\n", matrix_3d.sum(axis=2))
# Output: [[3 6]      <- Layer 0: row 1 sum (3), row 2 sum (6)
#          [9 12]]    <- Layer 1: row 1 sum (9), row 2 sum (12)

# Keepdims: (2, 2, 3) -> (2, 2, 1)
print("Axis 2 Keep :\n", matrix_3d.sum(axis=2, keepdims=True))
print("Axis 2 Keep Shape:", matrix_3d.sum(axis=2, keepdims=True).shape)


''' mean(),median(),std(),var() : 
    These are all Global Functions and can also be used as methods on array_object 
    Syntax : np.mean() or arr.mean()
    Return :
       A scalar value (if applied to the whole array)
         <OR> 
       an ndarray (if an axis parameter is provided).
    - Compute basic descriptive statistics across the entire array, or along a specific axis.
    - These standard functions are not safe against missing data (NaN). 
    - If your dataset has even a single missing value (NaN), running np.mean() or np.std() will immediately return NaN as the result, ruining your calculation.
    - NumPy provides twin functions specifically designed to ignore missing values: np.nanmean(), np.nanmedian(), np.nanstd(), and np.nanvar(). 
    - They drop the missing values on the fly during vectorization.
'''
sales_1 = np.array([10, 20, 300, 4000])
print(np.mean(sales_1))

sales_2 = np.array([200, 450, np.nan, 300])
print(sales_2.mean())  # nan -> Total Breakdown

# The optimized fix :
# specifying the float precision to print way
''' 
 np.set_printoptions() (Visual Display Only)
 - If you want to keep the absolute maximum precision intact for your backend calculations 
   but want clean screen output limited to 2 decimals, change NumPy's global rendering engine using precision=2.
   import numpy as np

# Set the global display format configuration
np.set_printoptions(precision=2, suppress=True)

data = np.array([3.14159265, 0.00001234])
print(data)
# Output: [3.14 0.  ]

'''
# np.set_printoptions(precision=2,suppress=True)
# data = np.array([3.14159, 2.71828])
# print(data)
# print(np.nanmean(sales_2,keepdims=True))


# standard way to precise the decimal count in float values
print(f'{np.nanmean(sales_2):.2f}')
#  nanmean() is a function of module numpy its not a method for array_object
# So don't try to write arr_object.nanmean() it will throw error as ndarray object dont recognize this method on the object.
# we can use np.nanmean(array_object) the module contains the function nanmean().
matrix_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# shrinks column to single value by adding them up
print(np.median(matrix_2d, axis=1))
# next calculates median by doing calculatedvalue / no.of values in that row
# row 1 : 1+2+3 = 6 => median = 6/3 = 2.0 (return float values)
# row 2 : 4+5+6 = 15 => median = 15/3 =5.0

matrix_3d = np.array([
    [[1, 1, 1], [2, 2, 2]],  # Layer 0
    [[3, 3, 3], [4, 4, 4]]   # Layer 1
])

print(matrix_3d.mean(axis=0, keepdims=True))

