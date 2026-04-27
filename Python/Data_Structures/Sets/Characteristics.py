my_set = {10,20,30,40,10,20}
print(my_set) 
my_set.remove(20)
print(my_set)
print(my_set[0])
'''output : {40, 10, 20, 30} 
  • unordered     - we cant see the same order what the output has been this happened because of hash and modulo math it did.
                    They get different slots which changes based on the size of hash tables and load factor.
  • No Duplicates - Set is unique it check for the values in each slot when collision of value to insert in slots occurs, thats how it prevent duplicates.
  • Indexed       - Set is not INDEXED we cant retrieve some values based on indexes in the set data structure, they dont have any index for the items in set.
  • Mutable       - Set is mutable we can remove the specific item            
                
'''
