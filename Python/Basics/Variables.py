'''
Variables:
  - makes program Dynamic
  - Name to store a value
  - stored in memory
  - Reusable Anytime
  - updatable Anytime
'''
x=1
print(x)
x=2
print(x)

print('vamshi wants to learn python')

name='John'
print(name,'is a python expert')
print(name,'is expert since 2009')
print('Everyone needs',name,"Help!!\n")

'''
Python updates variable super easy one change updates everything!
But python runs code line-by-line so, the above print statements(4-6 lines) doesn't know the updated value of variable name.
 '''
# name='Barra'
# print(name,'is new guy in the team ')

'''
 print has in built separator as sep=" "
we can use sep=''(empty to negate that issue) or formatted string.
'''
example='Datapractice.com'
print('info@',example,sep='')
print('support@',example,sep='')
print('www.',example,sep='')
print(f'example@{example}')

name='    spaces     '
# strip() helps to remove leading and trailing spaces.
print(name.strip())