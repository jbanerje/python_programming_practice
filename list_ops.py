''' Basic Array Operations in List '''

a = [i for i in range(1, 11)]

print('Actual Array - {}' . format(a))
print('Length - {}'.format(len(a)))

a.append(11) # Appends item to the back (queue)
print('Array after apppend - {}' .format(a))

a.remove(5)  # Removes the items. This is not the position
print('Array after remove - {}' .format(a))

a.insert(5, 5)  # Removes the items. This is not the position
print('Array after insert - {}' .format(a))

# Other functions
print('Minimum - {}' .format(min(a)))
print('Maximum - {}' .format(max(a)))

a.sort()
print('Sorted', a)

a.reverse()
print('Reverse', a)

del a[0]
print('After Delete -', a)

# Slicing
print('a[:-1]-', a[:-1])
print('a[::-1]-', a[::-1]) # Reverses the list

# List comprehension
print('Compr-1', [i for i in range(1, 11)])
print('Compr-2', [i*i for i in range(1, 11)])
print('Compr-3', [i for i in range(1, 11) if i%2==0])
print('Compr-4', [(i, j) for i in range(3) for j in range(3)])

# 2D to 1D conversion
m = [[1,2,3], ['a', 'b', 'c']]
print('Comp-5', [x for row in m for x in row])