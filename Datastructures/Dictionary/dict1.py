"""
A program for dictionary
"""

dict1 = {}

print(f"dict1: {dict1}")

dict2 = {1: "Niraj", 2: "Ashok", 3: "Deepak"}

print(f"dict2: {dict2}")

dict3 = {"name": "Niraj", "age": 25, "city": "Bangalore"}

print(f"dict3: {dict3}")

# Accessing elements

print(f"dict2[1]: {dict2[1]}")
print(f"dict3['name']: {dict3['name']}")

# Updating elements

dict2[1] = "Niraj Kumar"
print(f"dict2: {dict2}")

dict3["age"] = 26
print(f"dict3: {dict3}")

# Deleting elements

del dict2[1]
print(f"dict2: {dict2}")

dict3.pop("age")
print(f"dict3: {dict3}")

# Operations on dictionary

# Length
print(f"Length of dict2: {len(dict2)}")

# Membership
print(f"Is 2 present in dict2: {2 in dict2}")

# Iteration
for i in dict2:
    print(f"{i}: {dict2[i]}")

# Dictionary deletion
del dict3

# Dictionary methods

dict4 = {1: "Niraj", 2: "Ashok", 3: "Deepak"}
print(f"dict4: {dict4}")

# Copy

dict5 = dict4.copy()
print(f"dict5: {dict5}")

# Clear

dict5.clear()

print(f"dict5: {dict5}")

# Get

print(f"dict4.get(1): {dict4.get(1)}")

# Items

print(f"dict4.items(): {dict4.items()}")
print(f"dict4.keys(): {dict4.keys()}")
print(f"dict4.values(): {dict4.values()}")
print(f"dict4.popitem(): {dict4.popitem()}")

# Setdefault

print(f"dict4.setdefault(1, 'Niraj'): {dict4.setdefault(1, 'Niraj')}")

# Update

dict4.update({4: "Kumar"})
print(f"dict4: {dict4}")

# Pop

print(f"dict4.pop(1): {dict4.pop(1)}")
print(f"dict4: {dict4}")

# Popitem

print(f"dict4.popitem(): {dict4.popitem()}")
print(f"dict4: {dict4}")

# Dictionary comprehension

dict7 = {i: i**2 for i in range(1, 6)}

print(f"dict7: {dict7}")

# Nested dictionary

dict8 = {1: {"name": "Niraj", "age": 25}, 2: {"name": "Ashok", "age": 30}}

print(f"dict8: {dict8}")

# Accessing elements

print(f"dict8[1]['name']: {dict8[1]['name']}")
print(f"dict8[2]['age']: {dict8[2]['age']}")

# Updating elements

dict8[1]["name"] = "Niraj Kumar"
print(f"dict8: {dict8}")

dict8[2]["age"] = 31
print(f"dict8: {dict8}")

# Deleting elements

del dict8[1]
print(f"dict8: {dict8}")

dict8.pop(2)
print(f"dict8: {dict8}")

# Operations on dictionary

# Length
print(f"Length of dict8: {len(dict8)}")

# Membership
print(f"Is 2 present in dict8: {2 in dict8}")

# Iteration
for i in dict8:
    print(f"{i}: {dict8[i]}")

# Dictionary deletion

del dict8

