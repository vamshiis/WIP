def total(*args):
    print(type(args)) #*args collects the arguments in the form of "Tuple"
    print(sum(args))

total(1,2)
# total(a=1,b=2,c=3) # Throws error *args must be used only when positional arguments are passed 

def create_user(**kwargs):
    print(type(kwargs)) # **kwargs collects the arguments in the form of "Dictionary"
    print(kwargs)

create_user(name = 'ronaldo',age=35,country = 'SA')
# create_user('ronaldo',35,'SA') #Throws Error **Kwargs must be used only when keyword arguments are passed