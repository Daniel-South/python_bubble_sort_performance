# Test with a non-numeric list

l3 = ['orange', 'grape', 'pineapple', 'pear', 'grapefruit', 'lemon', 'apple']
print(l3)
bub_sort(l3)
print(l3)

print("\nSort descending")
bub_sort(l3, direction='desc')
print(l3)


OUTPUT:

['orange', 'grape', 'pineapple', 'pear', 'grapefruit', 'lemon', 'apple']
['apple', 'grape', 'grapefruit', 'lemon', 'orange', 'pear', 'pineapple']

Sort descending
['pineapple', 'pear', 'orange', 'lemon', 'grapefruit', 'grape', 'apple']
