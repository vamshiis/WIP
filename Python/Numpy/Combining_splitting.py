import numpy as np
''' concatenate : 
    Global Function
    Syntax : np.concatenate((exsisting_array,new_array),axis = value)
    - The concatenate is a master function for combining arrays.
    - Glues an arbitrary number of arrays together along a specific, pre-determined axis.
    - Always retruns a copy. It allocates a fresh,larger contiguous block of memory to fit all the data points together.
    - The sizes of all dimensions except the concatenation axis must match exactly.
    - No virtual Stretching allowed like how broadcasting did.
    In combination always check the exsisting array shape and new array shape.
        Based on axis you gave leave that axis dimension and always keep sure the other dimension are equal.
    Ex : 
        1D array : we have only 1 axis which is 0 by default.
                   we can concatenate a 1D + 1D array without even specifying an axis.
                   Array_A.shape: (3,)
                   Array_B.shape: (2,)
                   Result: They join seamlessly into a 1D vector of length 5.

        
        2D Array : we have 2 axis which are 0 for row and 1 for column
                   we can concatenate a 2D + 2D array based on row and column
                   - if we want to add new row to exsisting array specify axis = 0 
                          Array_A.shape: (3,4)
                          Array_B.shape: (2,4)
                        Here for this to work we have to check the column_dimensions of both arrays to match
                        Think if you want to add a row and you have 3 values which are column values [1,2,3]
                        but the existing array has 4 values for each row which are column values [1,2,3,4]
                        so if you try to combine it looks like [1,2,3,4
                                                                1,2,3, ]
                        This is not a shape numpy even hold it throws an Value Error.
                        So whatever axis you gave the leftover dimensions of arrays should match.
                        To add the row to exsisting array the new-array should have (n-rows, same_columns(of exsisting array))
                        Think like graph structure if we wanna add new row we require all the column value to hold the shape of matrix.
                   - if we wnat to add new column to exsisting array specify axis = 1
                          Array_A.shape: (3,4)
                          Array_B.shape: (3,6)
                        here the axis is 1 so we have leave the exsisting arrays column dimension and check the row dimensions values.
                        If they are equal we can combine, so exsisting array row_dim = 3
                                                             new array row_dim = 3 
                                    axis = 1 compare row_dim of both array's => 3 == 3  
                        so we can combine new array to exsisting array successfully.
        
        3D Array : we have 3 axis which are 0 for layer, 1 for row and 2 for column.
                   we can concatenate a 3D + 3D array based on layer,row,column

                   - If we want to add new layer to the 3D structure specify axis as 0
                         Array_A.shape: (2,3,4) --> 2 layers, 3 rows and 4 columns in each layer
                         Array_B.shape: (2,3,4) --> n layers are added which have 3 rows and 4 columns for each layer it give

                         so check the row and column dimension of both array they should be equal.
                         so to add a layer with axis = 0 we can say (n_layers,row_dim(match Array_A),col_dim(match Array_A))
                    - If we want to add new row to 3D structure specify axis as 1 
                        Array_A.shape: (2,3,4) --> 2 layers, 3 rows and 4 columns in each layer
                        Array_B.shape: (2,6,4) --> 2 layers which have 6 rows (added) and 4 columns for each layer it give.

                        Here we need the equal layer as there is no stretching available
                        so we leave row_dim check if they match the layer_dim and col_dim of Array_A
                        If they match they can be combinable so for axis = 1 we shld have (same_layers,n_rows,same_columns)
                    - If we wanna add a columns to 3D structure specify axis as 2 
                           Array_A.shape: (2,3,4) --> 2 layers, 3 rows and 4 columns in each layer
                           Array_B.shape: (2,3,6) --> 2 layers are added which have 3 rows and 4 columns(added) for each layer it give.

                        now check for layer_dim and row_dim to be equal leave the column_dim of new array
                        If they match they can be combinable so for axis = 2 we shld have (same_layers,same_rows,n_columns)
''' 

'''vstack & hstack
    - Specialized convenience functions built on top of np.concatenate.
    - one feature is we need to be good at visualization to use this and we can skip specifying axis with this vstack and hstack functions.
    - To add rows use vstack and make sure col_dim match prehandly.
    - To add columns use hstack and make sure row_dim match prehandly.
    - can be manual work to ensure the matching of other dimensions.
    - we can track upto 2D but as dimension increase form 2D we it will be a tough job to maintain and moreover it includes a manual work.
    - use concatenate and learn how to handle axes better than this hstack and vstack and dstack(depth stack used for layer concatenation for 3D array)
    vstack :
    Syntax : np.vstack((existing_array,new_array))
     - only use if new array has equal column_dimnesion as existing_array
     - It joins arrays vertically (row-by-row) .
     - It translates directly to np.concatenate(..., axis=0) for 2D arrays.
     hstack:
     Syntax : np.vstack((existing_array,new_array))
      - only use if new array has equal row_dimension as existing_array
      - It joins arrays horizontally (column-by-column) .
      - It translates directly to np.concatenate(..., axis=1) for 2D arrays .
    Return Type: A single combined ndarray.
    Memory Behavior: Always returns a Copy.
'''

'''
1D Array Blueprint (The Line Merge)
In 1D data, there is only one tracking axis (axis=0). Elements can only be glued end-to-end.
 The Pre-Flight Check:
          Array_A.shape: (3,)
          Array_B.shape: (2,)
          Result: They join seamlessly into a 1D vector of length 5.
'''
arr_a = np.array([1,2,3])
arr_b = np.array([4,5])

# Using Master Concatenate (axis=0 is default for 1D)
result_concat = np.concatenate((arr_a,arr_b),axis=0)
print("1D Concatenate:", result_concat) # [1,2,3,4,5]

# Using hstack (For 1D arrays, hstack performs a flat end-to-end join)
result_hstack = np.hstack((arr_a,arr_b))
print("1D hstack : ",result_hstack)

'''WARNING TRAP: 
np.vstack forces 1D arrays to become rows of a new 2D matrix!
This requires both 1D arrays to be of EXACTLY equal length.
Turns the arr_a, arr_b to columns from rows first and then stacks them.
arr_a = [1,2,3] and arr_b = [4,5]
arr_a = [1    arr_b = [4
         2             5]
         3]
on this the vstack performs to stack them column wise that results in 
res_vstack =[1 4
             2 5
             3  ] -> we have a null value here so it throws error so make sure they both have same length to perform vstack.
in 1D make sure length of both arrays are same to perform vstack.
'''
try:
    np.vstack((arr_a, arr_b))
except ValueError as e:
    # Fails because lengths 3 and 2 don't match for a grid matrix row!
    print("1D vstack Crash:", e)


''' 2D Array Blueprint (Spreadsheet Grid Matching)
    - In 2D tables, you must choose your target track: stacking rows (axis=0) or stacking columns (axis=1).
    
    Vertical Pre-Flight Check (axis=0 / vstack):
    Array_A.shape: (2, 3) (2 rows, 3 columns)
    Array_B.shape: (1, 3) (1 row, 3 columns)
    Check Rule: 
    Leftover dimension (Columns) must match exactly: 
    Array_A.shape[1] == Array_B.shape[1] (3 == 3). Passes.
    
     Horizontal Pre-Flight Check (axis=1 / hstack):
     Array_A.shape: (2, 3) (2 rows, 3 columns)
     Array_C.shape: (2, 1) (2 rows, 1 column)
     Check Rule: 
     Leftover dimension (Rows) must match exactly: 
     Array_A.shape[0] == Array_C.shape[0] (2 == 2). Passes.
'''

matrix_a = np.array([[10, 20, 30],
                     [40, 50, 60]])

matrix_b = np.array([[70, 80, 90]])
# Row combining
concate_row_result = np.concatenate((matrix_a,matrix_b),axis=0)
# using vstack columns shls match to use this function.
v_result = np.vstack((matrix_a,matrix_b))

print('2D Vertical Stacking:\n',concate_row_result)
# Returns shape (3, 3):
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Column Combining
matrix_c = ([[40],
            [70]])
concate_col_result = np.concatenate((matrix_a,matrix_c),axis=1)
# using Hstack rows should match to use this 
h_result = np.hstack((matrix_a,matrix_c))
print("\n2D Horizontal Stacking:\n",concate_col_result)
# Returns shape (2, 4):
# [[ 10  20  30  40]
#  [ 40  50  60  70]]

''' 3D Array Blueprint (The Data Cube Filing Cabinet)
    - In 3D enterprise cubes (Layers, Rows, Columns), the leftover verification rules must be strictly cross-checked.
    
    Layer Check (axis=0):
     - Leftover axes [1] (Rows) and [2] (Columns) must match exactly.
     - Target Layout: Adding an entirely new warehouse/store layer.
    
    Row Check (axis=1 / vstack):
     - Leftover axes [0] (Layers) and [2] (Columns) must match exactly.
     - Target Layout: Adding new departments across all warehouse layers simultaneously.
    
    Column Check (axis=2 / hstack):
      - Leftover axes [0] (Layers) and [1] (Rows) must match exactly.
      - Target Layout: Appending a new week of data across all stores and departments simultaneously.
'''

# Project :
'''
Existing Base Cube: 2 Stores, 3 Departments, 4 Weeks
- we have 2 stores in layers form
- 3 Departemnts on the row axis
- 4 weeks on the column axis
'''
# we cant simply say layer 1 to have fill value 1 and layer 2 to have fill value 2
# we cant use fill value directly on to 2D arrays
# Instead create an empty 3D array and treat inner 2D arrays as indexes.
# If there are 2 2D arrays then index will be 0,1
# Target them individually and apply fill method pass the fill value you want to load
cube_base = np.empty((2, 3, 4), dtype=int)

cube_base[0].fill(1)
cube_base[1].fill(2)

print(cube_base)


'''--- CASE A: Layer Concatenation (axis=0) ---
        Goal: Add a 3rd Store. 
        - Stores sits on Layers axis so specify the axis = 0 to concatenate.
        - To add new store it should contain all the departments and all weeks data which exsiting data_cube contains.
        - check Leftovers (Rows, Columns) must be (3, 4)
'''
new_store_layer = np.empty((1, 3, 4))

new_store_layer[0].fill(3)

cube_3_stores = np.concatenate((cube_base, new_store_layer), axis=0)
print("Addition of New store Data :\n", cube_3_stores)


'''--- CASE B: Row Concatenation (axis=1) ---
     - Goal: Add a 4th Department to all the stores. 
         - Department sits on row axis so specify axis = 1 to concatenate
         - To add 4th department we should have all details of 4th department over both store + all weeks performance
         - check Leftovers (Layers, Columns) must be (2, 4)
         - if we have 4th department data for both the stores with all 4 weeks available its ready to be combined. 
'''
new_dept_rows = np.zeros((3, 1, 4))

cube_4_depts = np.concatenate((cube_3_stores, new_dept_rows), axis=1)
print('\nAdd new department for all 3 stores :\n', cube_4_depts)

'''--- CASE C: Column Concatenation (axis=2) ---
    - Goal: Add a 5th and 6th Week of data. 
       - Each week performance sits on column axis specify the axis = 2 to concatenate
       - Now we should have every store's all departments week 4 and week 5 data then only we can combine.
       - To add week 4 and 5 we should have metrics for each store and each department's week 4 and 5 data.
       - so the store value and department value shld match 
       - Check Leftovers (Layers, Rows) must be (2, 3)
'''
# print(cube_4_depts.shape)
new_weeks_cols = np.zeros((3, 4, 2))

cube_6_weeks = np.concatenate((cube_4_depts, new_weeks_cols), axis=2)

print('\n Added week 4 and 5 performance metrics for all store\'s departments :\n', cube_6_weeks)

