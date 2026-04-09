# --------------------- How to Unpack ?? -------------------
''' Unpacking List's
    - So far we placed multiple items into the list and packed them.
    - so now we can now unpack the items and use them wisely.

    Why we need to Unpack things??
    - lets say we have a personal info with items as name, age , role , city etc.
    - Each item has its own importance and we can apply various operations on the different items.
    - To use them differently first we need to hold them in separate variable so we can easily apply the corresponding data types operations.
'''
person = ['john', 22, 'Data Engineer', 'paris']

# Wwithout Unpacking
# using only indexes makes code long and hard to extend
name = person[0]
age = person[1]
role = person[2]
country = person[3]

# With Unpacking
# Unpacking list of variables, sepeareted by commas
# Rule : Variable order must match the list values order
# Unpacking is clean, easy, and makes code simple to extend
name, age, role, country = person
print(role)
print(age)

''' Rest Collector - Asterisk *
    - if we want to unpack things and think to only unpack specific start or end or both and move rest into separate list we need to use Asterisk (*)
    - * Asterisk Stores the Rest in New list
    - Python gonna assign specified variable with that value and take everything leftover into new list.
    - Rule : only one asterisk(*) is allowed in unpacking
'''
# first and last items matters and rest everything in middle can be stored or unpacked into another list
name, *details, country = person

print(name)
print(details)

# Start item matters and rest can be moved into details list while unpacking
# for this we need to specify the variable for first item and asterisk *
# Be careful with the order of values if in future we change the order the variable assignment changes in unpacking
name, *details = person
print(name)
print(details)

# last item is important and rest everything can be moved into details
*details, country = person
print(details)
print(country)

# Rules for unpacking

# Nr. of variables must match the values exactly - not less, not more
numbers = [1, 2, 3, 4]
first, second, third, last = numbers

# Note : *Asterisk collects leftovers, and it’s fine if there are none
bags = ['plastic']
variant_1, *rest = bags
print(variant_1)
print(rest)  # Empty list

#  Note : Can Unpack any sequence (list, tuples, strings, etc.)
message = 'hello'
first, *rest = message
print(first)
print(rest)

''' Skipping Items underscore "_"
    unpacking using "_"
    - If the value is not that important at the time of unpack we can simply use _ to skip that item and move ahead.
    - we can use multiple underscores
'''
person = ['john', 22, 'Data Engineer', 'paris']
# Unpack only name, role rest eveything skip it.
name, _, role, _ = person

''' power of Asterisk(*) and underscore(_)
    - If we want start , end items and the middle items are so long that we end up using more _ to skip items.
    - Instead we can combine the power of Asterisk(*) with the underscore(_)
    - we can use * and move to new list but we want to skip them, so * gonna take middle part instead of storing in new list we use "_" to skip complete middle part now.
'''
# Unpack first and last value , but skip all values in middle
name , *_ , country = person
print(name)
print(country)
print(*_) # Skipped Part

'''  Reference Aliasing :
- Unpacking copies the address, not the data. Whether the link stays or breaks depends on if you mutate or reassign.
- we can mutate or reasign the 2D - Data Structures like Nested List from unpacking them.
- we can only reassign for the 1D - Data Structures Like Normal lists
- unpack variables holds the reference address of items object.
- so if we change i.e reassign a value to the unpacked variable it will break the link of original list value's object.
- now the unpacked variable will be  pointing to new values object which the list doesn't have idea of.
- only mutable data can be modified which are list, dict, Sets
- integers, Strings, Tuples are immutable objects if we unpacl and
'''
''' 2D - DS Nested List
    - we can apply append and reassign for 2D nested lists.
    - while append makes the list and unpacked variable to see the change in the corresponding pointing object
    - The reassign makes the unpacked variable to point to new object, but still the list sees it old data
    - To work safely we can copy the item with .copy() and work safely, anyhow this will be helpful to not use append() directly on the data.
'''
list = [[1, 2, 3], [4, 5, 6]]
first, middle = list
print(f'list item original pointing address ---> {id(list[0])}')
print(f'Unpacked variable pointing address  ---> {id(first)}')

# Mutate using unpacked variable - using append(), update() ..
first.append(['person1', 'person2'])
# Here As the Addresses are same it can go inside the object and change the pointing objects value.
# This will makes changes reflect in both list[0] and unpacked vairable . same is being printed below
print(f'''Appended data using Unpacked variable :
               Value at list[0]                ---> {list[0]}
               Value of the unpacked variable ---> {first}
''')

# Reassign - Here we make the unpacked variable to point to different object rather than pointing to the unpacked value from list
# The address of before reassign and after reassign operation differes for the unpacked variable first in this case.
first = [8, 2]
print(f'''The re-assigned unpacked variable
                address(changed)    ---> {id(first)}
                value(changed)      ---> {first}
''')
print(f'''The list item\'s at index 0
       address(unchanged)           ---> {id(list[0])}
       and it\'s value(unchanged)    ---> {list[0]}
''')

# 1D - DS Normal List
# Can't perform mutation on Integers,Strings bascically on the  1D DS we can't apply mutation operations.
list = [1, 2, 3]
first, middle, last = list

print(f'list item original pointing address ---> {id(list[0])}')
print(f'Unpacked variable pointing address  ---> {id(first)}')

# Reassignment - Chnages the unpacked variable Pointing address to the object and its value.
first = 5
print(f'''The re-assigned unpacked variable
                address(changed)    ---> {id(first)}
                value(changed)      ---> {first}
''')
print(f'''The list item\'s at index 0
       address(unchanged)           ---> {id(list[0])}
       and it\'s value(unchanged)    ---> {list[0]}
''')
