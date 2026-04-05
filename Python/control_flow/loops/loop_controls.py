# ''' Break : 
#    - It stops the loop immediately
#    - It jumps out and ends the loop right away
# '''
# names = ['john', 'vamshi', 'sophie', '', 'Edward']
# for name in names:
#     if name == "":
#         print("Empty value detected!")
#         break
#     print(f'Name = {name}')

# ''' Continue :
#     - It skips one loop cycle without stopping the loop.
#     - It's like Skip this one and go next.
# '''
# names = ['john', 'vamshi', 'sophie', '', 'Edward']
# for name in names:
#     if name == "":
#         print("Empty value detected!")
#         continue
#     print(f'Name = {name}')

# ''' Pass : 
#     - It is a placeholder where nothing happens.
#     - For now just keep going do nothing.
#     - it is just placeholder to be changed later.
# '''
# names = ['john', 'vamshi', 'sophie', '', 'Edward']
# for name in names:
#     if name == "":
#         pass  # todo : Handle Empyty value
#     print(f'Name = {name}')

# # later to replace the empty value i gonna write something like this
# # its just like a condition sitting there need to be replaced later
# names = ['john', 'vamshi', 'sophie', '', 'Edward']
# for name in names:
#     if name == "":
#         name = name.replace("", "unknown")
#     print(f'Name = {name}')

# # Break vs Continue:

# # Real world Applications:

# '''Task - 1: 
# Loop through a list of days and print only the working days, skipping the weekends.
# - Avoid Hardcoding values inside for or if. Instead , define them as variables
# '''
# days = ['Mon', 'Sun', 'Wed', 'Tue']
# weekends = ['Sat', 'Sun']
# for day in days:
#     if day in weekends:
#         continue
#     print(f'Workday : {day}')

# ''' Task -2 :
# Scan emails to block unsafe data from entering the system
# '''
# emails = [
#     'xyz@gamil.com',
#     'abc@outlook.com',
#     'Select * from users;', #SQL Injection
#     'vomshiii@gmail.com'
# ]
# for email in emails:
#     if ';' in email:
#         print('SQL Injection')
#         break
#     print(f'Processing Email : {email}')

# for - else :
# It executes after the completion of for loop.
items = [1,3,4,6]
for i in items:
    print(i)
else:
    print('Loop ends')        
''' 
  - What's the point of using else when anyhow after the for loop it executes.
  - having else is useless we can simply go with print statement after for loop then also it will work similiar.
  - but real usage comes when we use the break statement in the for loop then the else block after the for loop makes sense. 
'''
items = [1, 3, 5, 7]
for i in items:
    if i % 2 == 0:
        print(f'Even no. found {i}')
        break
else:  # else will run only if the loop is not interrupted.
    print('All numbers are odd')
'''
    similar to if-else functioning
   - if the for loop if condition is satisfted and has break then else part wont be executed which is placed after for loop.
   - if the for loop if is not satisfied then the else part gonna be executed.
 ''' 
#  Why we need Else in Loop ??
# use case of for - else loop : we use it for search and validate operations.

# Task - 1 : check for missing Names in a List 
names = ['Vamshi','John', None, 'Smith']

for name in names:
    # Bad quality data checkpoint
    if name is None:
        print('found a missing name')
        break
# Ensures the data is of good quality if the else is executed.
else:
    print('All Names are available')
# We are using break & else in order to search for something and validate the data.

# Task - 2 : Check if all the files are CSV 

files=['data1.csv','data2.csv','data3.pdf','data4.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        break
else:
    print('All files are CSV')


# Challenge 
''' Check whether any filename appears more than once
    - file_list = ['report.csv','data.xlsx','summary.docx','report.csv','data.csv']
    - print "Duplicate found" if a duplicate exists, otherwise print "All files are unique"
'''

# Using for - else loop code :
# Even more efficient way is using sets.
files_list = ['report.csv', 'data.xlsx','summary.docx','report.csv','data.csv']
checked_list =[]

for file in files_list:
    if file in checked_list:
        print('duplicate found')
        break
    checked_list.append(file)
else:
    print('All files are unique')

# Not a Efficient Code 
'''why ?
   - Imagine if files_list had 1,000,000 files in it, and the very first two were duplicates.
       our code would still process all 1,000,000 files before checking if a duplicate existed!
    - but in for-else loop the exact second we see a item we've already checked, we sound the alarm, print "Duplicate found",
        and smash the break button to kill the loop entirely.
     '''
files_list = ['data.xlsx', 'report.csv',
              'summary.docx', 'report.csv', 'data.csv']
checked_list = []
for file in files_list:
    if file not in checked_list:
        checked_list.append(file)
print(checked_list)   

if checked_list != files_list:
        print('duplicate found')
else:
    print('All files are unique')


