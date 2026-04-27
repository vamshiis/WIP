a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

''' issubset() :
    Syntax : set_a.issubset(set_b)
    output : Boolean
    - Returns True if all items in this set exist in the other set.
    - Returns False if all items dont exist in the other set.
    - need to completely present in the asked set otherwise it returns false.
'''
print(a.issubset(b))

''' issuperset() :
    - Returns true when it includes ALL items of the other set
    - sometimes we want to check if the set contains all the items of another set to showcase its superiority.
    - for that we need to use superset() method
'''
print(b.issuperset(a))

''' isdisjoint() :
    - Returns true if both sets share no items (No Overlapping)
    - we use this method to check if both items has no shared items among them in that case it returns true.
'''
print(a.isdisjoint(b))