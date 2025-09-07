# Bi-directional Bubble Sort in Python
# Daniel R. South
# 2025-09-06

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


print("Test 1 - complete reversal")
a = [5, 4, 3, 2, 1]
print(a)
bub_sort(a)
print(a)

print("Test 2 - no sort needed")
a = [1, 2, 3, 4, 5]
print(a)
bub_sort(a)
print(a)

print("Test 3 - one element out of place")
a = [1, 2, 4, 3, 5]
print(a)
bub_sort(a)
print(a)

print("Test 4 - sort descending")
b = [1, 2, 3, 4, 5]
print(b)
bub_sort(b, direction="desc")
print(b)

print("Test 5 - sort descending with duplicate values")
b = [7, 1, 7, 3, 7, 5, 11, 9, 13, 15]
print(b)
bub_sort(b, direction="desc")
print(b)
