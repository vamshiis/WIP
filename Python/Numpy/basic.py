import numpy as np
import time
''' List vs Numpy Array Speed : 
    - Comparing the standard Python List vs Numpy Array Speed on the squaring of numbers.
    Cache :
      - first we need to understand the Cache concept in Programming la nguages for this to klick.
      - So we have this Cache concept where we retrieve and store in L1 cache in order to have faster accessing then going to slow RAM
        each time.
      - Because the cache is so small, the computer has to guess what data the CPU will need next. It makes these guesses based on two 
        fundamental rules:
        1. Temporal Locality: If you use a variable now, you will probably use it again very soon (like a loop counter). Keep it in the cache!
        2. Spatial Locality:  If you ask for a piece of data at memory address `100`, you will almost certainly ask for the data at address `101` next.
        
      - Because of Spatial Locality, when the CPU asks the RAM for a single variable, the RAM doesn't send just that variable. 
        It scoops up the adjacent 64 bytes (the **Cache Line**) and sends all of it to the CPU Cache, assuming you will need the 
        neighboring data next.

    - List :
      When we create a standard Python list, Python asks the operating system for memory wherever it can find space.
      - The Structure: The list itself is just a contiguous block of memory addresses (pointers). 
                       The actual integer objects are scattered randomly across the heap.
      - The Cache Line Pull: When the CPU tries to process the first item, it pulls a 64-byte chunk of memory from the heap.
                               But because the Python objects are scattered, that 64-byte chunk contains the one item you wanted, 
                               plus 56 bytes of random, useless memory from other programs.
      - **The Result:** To get the second item, the CPU has to go back to the slow RAM again. 
                        This is called a **Cache Miss**. It is terribly inefficient.

    Numpy Array :
      When we create a NumPy array, it bypasses Python's memory manager and uses lower-level C code to demand a single, unbroken block of memory.
     - The Structure: All the raw integers are packed shoulder-to-shoulder. No pointers, no Python object overhead. Just raw binary data.
     - The Cache Line Pull: When the CPU asks for the first item, the RAM sends the 64-byte chunk. Because the array is tightly packed
                              that 64-byte chunk contains your first item **AND your next 7 items** perfectly lined up.
     - The Result: For the next 7 calculations, the CPU operates at maximum speed entirely inside the L1 Cache without ever talking 
                   to the slow RAM. This is a **Cache Hit**. It is extremely Efficient.
     - Vectorization /         : SIMD stands for Single Instruction, Multiple Data. Once that clean, continuous block of data is sitting 
       SIMD (The actual magic)   in the cache, the CPU's arithmetic logic unit doesn't loop through them one by one. 
                                 It fires a single hardware instruction that multiplies the entire block by 2 at the exact same time.

    - Standard Python says: "Take item 1, multiply by 2. Take item 2, multiply by 2." Hits RAM everytime
    - NumPy says: "Take this entire block of 8 items, multiply them all by 2 right now." computes on Cache itself
    - So this was the reason behind the faster Numpy Array and slower List of standard Python 

'''
demo_list = list(range(100))
start = time.time()
res = [x*2 for x in demo_list]
res_time = time.time() - start

demo_np = np.arange(100)
start = time.time()
res_np = demo_np * 2
np_time = time.time() - start

print(res_time)
print(np_time)
