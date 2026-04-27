''' union() :
    Syntax : set_a.union(set_b) //or// (set_a | set_b)
    output : set
    - Combines ALL unique items from both sets.
    - gives the every unquie value from both the sets 
    - if any duplicates it removes and includes them only once 
    Note :
    Math Operators return a new set and leave the originals untouched
'''
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.union(b))
print(a | b)  # we can use | to for the same union operation

''' intersection() :
    Syntax : set_a.intersection(set_b) //or// (set_a & set_b)
    output : set
    - returns only the shared items
    - It gives us only the items that appears in both the sets
'''
print(a.intersection(b))
print(a & b)

''' difference() :
    Syntax : set_x(whose set values you need).difference(set_y(from whose set values))
    output : set
    - a.difference(b) - Returns Items in A , but not in B
    - want the item in one set where its items aren't overlapped with another.
    - only in A not in B / Only in B not in A
    - the position of what you needed are important in syntax whose difference we gonna
      need comes first then we use another set inside the method.
'''
print(a.difference(b))
print(a - b)
print(b - a)  # returns items in B, but not in A

''' Symmetric_difference() :
    Syntax :
    output :
    - Returns values which are not shared from both the sets
    - gives only none-shared items
    - To get the items which are not overlapping and unique in each sets we use this method
    - It is opposite operation of Intersection where we get only overlapped items, in here we get the unoverlapped items from both the sets.
'''
print(a.symmetric_difference(b))
print(a ^ b)
