a = [1, 2, 3, 4, 5]

print(f'List initial values: \n {a}')

# append to the list
a.append(16)

print(f'After appending a value:\n {a}')

# insert at a specific index
a.insert(2, 8)

print(f'After inserting a value at a specific index:\n {a}')

# remove the last element
a.pop()

print(f'After removing a value:\n {a}')

# remove the element at a specific index
a.pop(2)

print(f'Removing value of index 2:\n {a}')

# remove the first occurence of a value
a.remove(4)

print(f'Removing first occurance of 4:\n {a}')

# reverse the list
a.reverse()

print(f'After reversing:\n {a}')

# sort the list
a.sort()

print(f'After sorting:\n {a}')

# sort the list in reverse
a.sort(reverse=True)

print(f'After sorting in reverse order:\n {a}')

# get the index of a value
print(f'Value at index 3:\n {a.index(3)}')

# count the number of occurences of a value
print(f'Item count in list: {a.count(3)}')

# copy the list
b = a.copy()

print(f'Copy of list {a} is:\n {b}')

# extend the list
a.extend(b)

print(f'Extending the list :\n {a}')

# get the length of the list
print(f'Length of list:\n {len(a)}')

# get the maximum value in the list
print(f'Maximum value of list: {max(a)}')

# get the minimum value in the list
print(f'Minimum value in the list: {min(a)}')

# get the sum of the list
print(f'Sum of items in the list: {sum(a)}')

# get the average of the list
print(f'Average of items in the list: {sum(a)/len(a)}')

# clear the list
a.clear()

print(f'After clearing the list:\n {a}')
