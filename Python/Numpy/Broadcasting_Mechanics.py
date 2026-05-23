import numpy as np
'''
    - Before NumPy performs any math operation (like A + B), it runs a Structural Audit on the shapes of the two arrays.
      It looks at the shapes from right-to-left (trailing dimensions first).
    
    <<<The Rules followed by the Broadcasting before doing any math operation are : >>>
    RULE 1 :
       - If Array A has fewer dimensions than Array B, NumPy looks at the shape tuple and 
         injects 1s to the left side of the smaller shape until they have the same number of dimensions.
       Example : we add a 1D array of shape(4,) to 3D array of shape (2,3,4).
                 Numpy Automatically updates the 1d array's shape internally to :
                 (1,1,4), Now they both have same dimensions.
    RULE 2 : 
        - After padding the left most of the shapes to 1 it checks for compatability, if this check is 
          passed the broadcasting happens if here it fails the broadcasting wont happen and throws Error.
        - Numpy stacks 2 shapes vertically and compares them axis-by-axis, starting
          from the rightmost side. For each column, the shapes are compatible if and only
          if :
              • The two numbers are exactly equal, OR 
              • At least one of the number is 1.
        - If even one axis column fails this check, Numpy halts execution instantly and throws a "ValueError"
        Example :
        where it becomes compitable :
              array_a shape = (2,3) and array-b shape = (1,3) (Note 1 is padded as it was 1D array with 3 elements)
              stack them vertically : 
                                     2  3
                                     1  3
                            compares from right most side so 3 == 3 => yes both are equal hence, compitable.
                            compares next to the left side so 2 == 1 => No they are not, falls to second check is any one of them is "1" => yes so its compitable.
                            Next there arent anything to compare if all are compitable its ready to apply the broadcasting and do the specified math operation.
        where it becomes Not Compatabile : 
               array_a = (2,3) and array_b = (3,2) (as both are 2D arrays there is no need of padding 1)
               stack them vertically :
                                      2  3
                                      3  2
                            compares from right most side so 2 == 3 => No they are not, 
                                      falls to second check is any of them is "1" => No they are different and no 1 is present.
                                      so its not compatabile.
                Hence no need to check further as the math operation are forced to be done on different dimension matrix so throw "ValueError"
    RULE 3 :
        - If a dimension is 1, that axis is flagged as "Stretching Axis". Numpy will virtually
          replicate the data along that dimension to match the size of larger array. 
'''
''' 
   Broadcast on 1D and 2D array
   ****Scenario 1: The 1D + 2D Row Stretch****
   - user want to do a math operation on 1D array and 2D array, how broadcast handles this behind lets see
   - we want to add a 1D array to a 2D matrix
   • Array A (2D matrix) : shape(3,4)
   • Array B (1D vector) : shape(4,)
   The Pre-Flight Check : 
   1. Align dimensions : Array B has fewer dimensions, pre-pad 1 on the left
       • Array A : 3, 4
       • Array B : 1, 4 => pre padded 1 to the left side of actual shape
   2. stack vertically and check column : 
            3, 4 
            1, 4
        Axis 1 is 4 == 4. compitable
        Axis 0 is 3 == 1. one number is 1, Compatible! (Array B will stretch vertically down all 3 rows).

Original Array A (3, 4):          Original Array B (4,):
[[ 1,  2,  3,  4],                [10, 20, 30, 40]
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12]]

Step 3: NumPy virtually stretches Array B to match 3 rows:
[[10, 20, 30, 40],
 [10, 20, 30, 40],
 [10, 20, 30, 40]]

Final Calculation (Direct Element-wise Vectorization):
[[ 1+10,  2+20,  3+30,  4+40],
 [ 5+10,  6+20,  7+30,  8+40],
 [ 9+10, 10+20, 11+30, 12+40]]
'''
#  1D + 2D row stretch
# array_a = np.array([10,20,30,40]) #shape (4,)
# matrix_a = np.array([[1,  2,  3,  4],            
#                      [5,  6,  7,  8],
#                      [9, 10, 11, 12]]) #shape (3,4)
# add_operation = array_a + matrix_a
# print(add_operation) # Does successful broadcast and returns the (3,4) resultant matrix as output. so by this we can understand the stretch was happened

''' Scenario 2: The 1D + 2D Total Dimension Mismatch (Immediate Crash) : 
    
    We want to add a 1D vector of 3 elements to a 2D matrix of shape (3, 4).
       • Array A (2D Matrix): Shape (3, 4)
       • Array B (1D Vector): Shape (3,)
    The Pre-Flight Check:
    1. Align Dimensions: Pre-pad a 1 on the left of Array B.
        • Array A: 3 , 4
        • Array B: 1 , 3 
    2. Stack and check for compatability : 
                 3  4
                 1  3
            Axis 1 : Compare 4 and 3. Are they equal? No.Is one of them 1? No.
    NumPy throws ValueError: operands could not be broadcast together. 
    It cannot continue because it does not know how to map 3 elements across a width of 4 columns.

    
    **** Scenario 3: The 1D + 2D Column Stretch (The Manual Fix) ****
    - To make Scenario 2 work, we must change Array B into a 2D column vector using
      np.newaxis so a 1 is explicitly present in the right to left check.
    - the rule was to pad 1 to left each time there is smaller shape.
    - but after padding 1 and checking from right most side we hit with no match to compatability test.
    - so it instantly returned ValueError, now we need to pad 1 to right not left and the prev right value of smaller shape shld match the left value of bigger shape.
    - we need to explicitly say to pad 1 to the right not to the left can solve our problem.

    How to override the broadcast rule of padding??
    - To pad 1 to right means columns we need to use np.newaxis which will give 1 to specified location.
        - We need to pad on column so we need to do is :
            [:, np.newaxis] = (3,1)-> leave row as it is but add new axis 1 to column
    
    The Pre-Flight Check:
    1. Align Dimensions: Both are already 2D. No padding needed.
      • Array A (2D Matrix): Shape (3, 4)
      • Array B (2D Column Vector): Shape (3,1)
    2. stack and check for compatability : 
                   3  4
                   3  1
            Axis 1 : 4 vs 1. one number is 1, so Compatible!!(Array B will stretch horizontally across all 4 columns).
            Axis 0 : 3 == 3. compatible!

The Visual Memory Map :    
Original Array A (3, 4):          Original Array B (3, 1):
[[ 1,  2,  3,  4],                [[10],
 [ 5,  6,  7,  8],                 [20],
 [ 9, 10, 11, 12]]                 [30]]

Step 3: NumPy virtually stretches Array B to match 4 columns:
[[10, 10, 10, 10],
 [20, 20, 20, 20],
 [30, 30, 30, 30]]

Final Calculation:
[[ 1+10,  2+10,  3+10,  4+10],
 [ 5+20,  6+20,  7+20,  8+20],
 [ 9+30, 10+30, 11+30, 12+30]]

-> we have forced the 1d array rather to be (1,3) -> 1 row three columns to be (3,1) three rows and 1 colums.
-> so that can support the stretch rule of matrix whose dimensions are (3,4) we can simply now stretch the columns to 4 easily.
'''
# matrix_2d = np.arange(1,13).reshape(3,4)
# col_1d = np.array([10,20,30])[:, np.newaxis] #shape (3,1)
# print(matrix_2d + col_1d)


''' Scenario 4: The 3D Advanced Stretch (Data Analytics Scenario)
    - In analytics, a 3D array represents [Layers/Panels, Rows, Columns]. 
    - Imagine data tracking 2 different stores, each tracking sales over 3 departments, across 4 weeks.
        • Array A (3D Data Cube): Shape (2, 3, 4)
        • Array B (2D Matrix)   : Shape (1, 3)
    The Pre flight check : 
    1.Align Dimensions : Array B has fewer dimensions. pre - pad a 1 on the left,
       • Array A : 2,3,4
       • A  rray B 1,1,3
    2. stack vertically and check : 
                 2  3  4
                 1  1  3
        Axis 2 : 4 vs 3  Are they equal? No.Is one of them 1? No.
      Throws valueError can't broadcast 2,3,4 with 1,3
      
    Explicit Axis specifying : 
      - Always check shape and calulate what will it throw via pre pad method if it's compatible then you wont have to explicitly add np.newaxis.
      - If it doesnt satisfy then look out and try to force the pad of 1 on specific axis via np.newaxis just.
      - here we need at column so we do [:,:,np.newaxis] at the column axis in squarebrackets on the array itself.
    Explicitly say to have 1 at column so we write [:, :, np.newaxis] --> add a new axis at column not to the left 
    
    That makes shape(1,3,1)
                 2  3  4
                 1  3  1
         Axis 2 : 4 vs 1 Are they Equal ? No. Is one of them 1? yes.Compatible
         Axis 1 : 3 == 3 compatible
         Axis 0 : 2 vs 1 Are they Equal? No. Is one of them 1? Yes.Compatible
The Visual Memory Map:
  - Array B (1, 3, 1) acts like a transparent sheet of rubber containing a single (1,3) matrix grid. 
  - Because the leading dimension is 1, and column are 1 in explicit shape (1,3,1).
  - NumPy stretches the entire matrix grid backward into a deep stack to create 2 layers, making it a (2, 3, 1) cube.
  - And it also stretches horizontaly to create 4 columns to match the 3D matrix columns for broadcasting.
  - The new internal shape of Array B is (2,3,4) -> with 4 stretched columns and a stretched backward layer of 2.

Array B virtually duplicates its entire 2D grid across Layer 0 and Layer 1:

          [ Layer 0]                            [ Layer 1  ]
       [[10, 10, 10, 10],                    [[10, 10, 10, 10],
        [20, 20, 20, 20],                     [20, 20, 20, 20],
        [30, 30, 30, 30]]                     [30, 30, 30, 30]]
This new 3D array of Array B is used in broadcast with Array A data cube.
'''
matrix_3d = np.arange(1,25).reshape(2,3,4)
print(matrix_3d)
matrix_2_2d = np.arange(10, 31, 10).reshape(1, 3)[:,:, np.newaxis]
print(matrix_2_2d)
res = matrix_3d + matrix_2_2d
print(res)