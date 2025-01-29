"""
    Tuple program

"""

tup1 = ()
print(f"tup1: {tup1}")

tup2 = (1, 2, 3)
print(f"tup2: {tup2}")

tup3 = ("Niraj", "Ashok", "Deepak")
print(f"tup3: {tup3}")

tup4 = (1, "Niraj", 3.5)
print(f"tup4: {tup4}")

# Operations on tuples

# Concatenation
tup5 = tup2 + tup3
print(f"tup5: {tup5}")

# Repetition
tup6 = tup2 * 3
print(f"tup6: {tup6}")

# Slicing
print(f"tup6[1]: {tup6[1]}")

# Length
print(f"Length of tup6: {len(tup6)}")

# Membership
print(f"Is 2 present in tup6: {2 in tup6}")

# Iteration
for i in tup6:
    print(i)

# Indexing
print(f"Index of 2 in tup6: {tup6.index(2)}")

# Count
print(f"Count of 2 in tup6: {tup6.count(2)}")

# Unpacking
a, b, c = tup2
print(f"a: {a}, b: {b}, c: {c}")

# Tuple to list
list1 = list(tup2)
print(f"list1: {list1}")

# List to tuple
tup7 = tuple(list1)
print(f"tup7: {tup7}")

# Tuple deletion
del tup7

# Tuple functions
print(f"Max of tup2: {max(tup2)}")

print(f"Min of tup2: {min(tup2)}")

print(f"Sum of tup2: {sum(tup2)}")

print(f"Sorted tup2: {sorted(tup2)}")

print(f"Reversed tup2: {tuple(reversed(tup2))}")

print(f"Length of tup2: {len(tup2)}")

