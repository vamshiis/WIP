import numpy as np
''' 1. Boolean Masking(Filtering) : 
    - It is an syntactic sugar using comparison coperators (e.g., >,<,==) directly on the array object
      Inside the square brackets arr[condition]
    - Filters an array down to only the elements that match the specified condition.
    Return : A brand new 1D ndArray containing only the matching values.
    - Boolean masking always returns a copy. It cannot return the view because the matching elements 
      are scattered across different non-consecutive places in the memory.
    - Means wee have the array on contigious space in memory but these matching arent staying side by side based on condition we gave
     so its hard to return the view of object itself so it needs to copy all matching values to new array object.
    - we cannot use "or","and" keywords like how we used them in standard python for multiple conditions.
    - we have to use bitwise operaters(|,&) for multiple condition in numpy arrays. 
    - if we apply a boolean mask to 2D matrix, it loses it shape and returns us the flat 1D array why?
    - Because different rows might have a different number of matching elements, making a uniform matrix gris is impossible.
    Most Recommended use case : 
    - use only when you need to extract matching values into 1D array.
'''
data_1 = np.array([15,20,1,2,11,12,90])
data_2 = np.array([[10,20,20],[20,30,50],[30,40,78],[90,56,56]])
data_3 = np.array([[[10,20,20],[20,30,50]],[[30,40,78],[90,56,56]]])
most_days_1 = data_1[data_1 > 15]
most_days_2 = data_2[data_2 > 30]
most_days_3 = data_3[data_3 > 50]
print(f'Dimension : {data_1.ndim},shape : {data_1.shape}')
print(f'matching elements : {most_days_1}')
print(f'Dimension : {data_2.ndim},shape : {data_2.shape}')
print(f'matching elements : {most_days_2}')
print(f'Dimension : {data_3.ndim},shape : {data_3.shape}')
print(f'matching elements : {most_days_3}')


''' where() : 
    Global Numpy Function
    Syntax_1 : np.where(condition)
    Syntax_2 : np.where(condition,x,y)
    Return_1 : 1 Parameter : A Tuple containing ndarray's size of indicies for eaching matching elements for a given condition.
    Return_2 : 3Parameters : A New ndarray of exact same shape as the input with x and y values yielded based on condition.
                             if true places given x value else places y in new array
    3-Parameter : Always returns a copy because it creates a brand new array built from components of your choice.
                  Acts as an Mapper in most cases simply.
                  Mostly use when you want to replace values or map them on condition.
    1-Parameter : Returns fresh index arrays, but if we use this indices to modify dat, we will be mutating original data.
                  - Returns indices but most recommended to use for 1D arrays alone.
                  - For 2D and above use argwhere() function.
    - When using it as an IF-ELSE tool, x and y can be scalar values (like 0 or "High") OR they can be entirely different arrays of the exact same shape. 
      This is widely used to cap outliers (e.g., "if value > 100, set it to 100, otherwise keep the original value").
'''
salaries = np.array([45000, 120000, 30000, 85000])
labels = np.where(salaries > 80000, "High", "Standard")
print(labels)
higher_earners_indices = np.where(salaries > 80000)
print(higher_earners_indices)

# Best practice for usage of where() on high dimensional arrays.
days = np.array([[10, 20, 20], [20, 30, 50], [30, 40, 78], [90, 56, 56]])
filtered_days_1= np.where(days >= 20)
print(filtered_days_1) # return the ndarray (rows_values) ndarray (column_values) we have map ourself from both tuple each value as pair (row,column) to know actual value position
# for 2 and above dimension its a nightmare to see and map ourself.
# we have 2 ways to see the matching values in 2 and above dimension.

# Method 1 : Always use 3 parameter where() function
filtered_days_2 = np.where(days >= 50,days,0) #if matched condition return that value and if not matched return 0 
print(filtered_days_2)

# method 2 : use of argwhere
''' argwhere()
    Syntax : np.argwhere(condition)
    If we absolutely must have the coordinates of a high-dimensional array in a way that a human can actually read, don't use np.where(). 
    Use np.argwhere().np.argwhere() automatically pairs the rows, columns, and layers together into clean coordinate rows.
    Most Recommended use case : 
    - If you want to see the cordinates/indices in 2D/3D array use np.argwhere()
'''
filtered_days_3 = np.argwhere(days >= 50)
print(filtered_days_3)

# Challenge 
# mark the even number as True and odd numbers False in the given array
# Note True and False are Booleans not Strings.
arr = np.array([9, 14, 22, 17, 5])
even_mask = np.where(arr % 2 == 0, True, False)
print(even_mask)

''' Fancy Indexing :
    - Passing the list of indices you want into object[indices]
    - returns the values at those indices just.
 '''
# For 1D array 
features = np.array(["Age", "Income", "Credit_Score", "Churn_Risk", "Region"])
selected_indices = [1,2,4]
# sub_report = features[selected_indices]
sub_report = features[[1,2,4]]
print(sub_report)