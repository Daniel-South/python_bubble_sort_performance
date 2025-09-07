# Bubble Sort Performance Test
# Compare the performance of the bubble sort to numpy's built-in sort function
# Daniel R. South
# 2025-09-06

import numpy as np
import time

def bub_sort(A, direction="ascending"):
    first_letter = direction[0]

    if first_letter == 'a' or first_letter == 'A':
        # Check whether two numbers are NOT ascending
        # If the first value is less than or equal to the second,
        # they are not out of order, so return False. Else True.
        
        out_of_order = lambda x, y : True if (x > y) else False
    
    else:
        # Check whether two numbers are NOT ascending
        out_of_order = lambda x, y : True if (y > x) else False

    a_size = len(A)
    loops = a_size - 1
    comparisons = a_size - 1

    for i in range(loops):
        switch_made = False
        
        for j in range(comparisons):
            if out_of_order(A[j], A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                switch_made = True
                
        if switch_made == False:
            break
            
        comparisons = comparisons - 1




print("BEGIN PERFORMANCE TEST")
print("\nTest the NUMPY SORT with a randomly generated set of 10000 integers")
print("Note: np.sort() does not sort the array in place. It returns a sorted array.\n")

big_array = np.random.randint(1, 99999, 10000)

print("size of the array:", len(big_array))
print("min value:", min(big_array))
print("max value:", max(big_array))

print("\nfirst ten elements:")
print(big_array[:10])
print("last ten elements:")
print(big_array[-10:])

print("sort using np.sort()")

start_time = time.perf_counter()
sorted_array = np.sort(big_array)

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("\n*** NUMPY SORT completed ***")
print("Elapsed time:", elapsed_time)

print("\nfirst ten elements:")
print(sorted_array[:10])
print("last ten elements:")
print(sorted_array[-10:])




print("\nTest the BUBBLE SORT with a randomly generated set of 10000 integers")
print("Note: As coded, the bubble sort algorithm sorts the array in place.\n")

big_array = np.random.randint(1, 99999, 10000)

print("size of the array:", len(big_array))
print("min value:", min(big_array))
print("max value:", max(big_array))

print("\nfirst ten elements:")
print(big_array[:10])
print("last ten elements:")
print(big_array[-10:])

start_time = time.perf_counter()
bub_sort(big_array)

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("\n*** BUBBLE SORT completed ***")
print("Elapsed time:", elapsed_time)

print("\nfirst ten elements:")
print(big_array[:10])
print("last ten elements:")
print(big_array[-10:])


print("END OF PERFORMANCE TEST")
