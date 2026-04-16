''' List Comprehensions :  
    - Till now we have learnt looping through data + filtering through data + Transforming the data.
    - Now we gonna put this three process into  one and execute them.
'''

'''  Working of List Comprehension : 
  - Lets say we have a list with 3 prices [80,20,100]
  - We want to Multiply only high prices > 50
  - so in order to do this we need to first find the prices which are >50 and then multiply them.

  - In order to do this in Python we have List Comprehension.
  - We don't have a keyword, method or function to do this but we need to build 3 blocks in one line to do list comprehension.
    1. Data Transformation
    2. Loop
    3. Filter

>> Behind the Scenes of how this work :
    1. Goes for the FOR loop (Here internally it creates a Iterator if list is passed and applies while True loop to get Items), It creates a Iterator out of the list.
    2. Python gonna next take an Item from Iterator and Filter the data.
        In this filter we have IF condition which checks the filter rule on each  item.
    3. Only if the filter IF condition is True then only the Data Transformation is applied on that item and then goes to the top of the loop.
    4. If the IF condition rule is not fulfilled, then it goes back to the top of the loop.
    5. If any item that is not full filled by filter rule then it wont get transformed as well as not appear in new list  as well. 
    6. filtering the data is optional.
         In that case all the items will be transformed because no filter is available

   Syntax : Data Transformation Loop Filter Rule ( includes Space between them ) 
   Use Case : Very powerful for data analysis      
'''
#  list comprehension Internals- for loop + filter + data transformation
list = [80, 20, 100]
multiplied_list = []

# Looping block  -- For loop
iterator = iter(list)   # Creates Iterator for the List      
while True:                   
    try:
        item = next(iterator) # Goes and get Item from the Iterator created 
        if item > 50:        # Filtering block
                             # If True goes for Data Transformation
                             # If false goes to bring new item 
            multiplied_list.append(item * 2)   # Data Transformation Block
    except StopIteration:
        break
print(multiplied_list)

# TASK - Normalize the domains into standard format
# Data Transformation + Filtering
domains = ['www.google.com', 'openai.com', 'loacalhost', 'WWW.ATLASSIAN.COM']
# Here we need to have a filter to pass valid domains and transform the domains into standard format

cleaned = [
    d.lower().replace('www.', '')  # Data Transformation
    for d in domains  # For Loop
    if '.' in d  # Filtering
]
print(cleaned)

