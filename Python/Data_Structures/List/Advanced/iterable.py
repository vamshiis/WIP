''' Iterable :
    - Iterable is a thing that we can loop over
    - we call a list Iterable, because we have items where we can loop through them.
    - Also the String Values we call them Iterable because it is something which we can loop over.
    -  On the other hand we have numbers and Booleans which we are not Iterable they don't have the independent items that we can loop through.
    
    • why we need Iteration ??
    - we use iteration to transformation the data.
'''
# Iterate and Transform each letter to uppercase
letters = ['a','b','c']
for letter in letters:
    print(letter.upper())

# Store the transformed result in a new list
letters = ['a', 'b', 'c']
new_list = []
for letter in letters:
    new_list.append(letter.upper())
print(new_list)
