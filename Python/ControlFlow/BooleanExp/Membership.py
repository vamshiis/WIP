# Membership (in) operator :
# Check if a value inisde another value.
# like in strings, list , tuples
print("o" in 'python')
print('f' not in "python")
print(3 not in [1,2,3])
print(3  in [1,2,3])

# Task :
# Validate that the domain is not on the banned list
# Security check : ensure the domain is not banned
domain = "gmail.com"
domain1="spam.com"
banned_domains = ['spam.com','bot.net','spin.org','fake.net']
print(domain not in banned_domains )
print(domain1 not in banned_domains)