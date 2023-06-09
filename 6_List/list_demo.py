"""
A list is a collection of ordered and mutable elements that
can be of different data types.
"""

fruits = ['apple', 'orange', 'banana', 'mango']
my_info = ['Mr.smith', 'NY', 20, 20.5, "apple.com"]

# length
print((len(fruits)))

# accessing elements by index number
name = my_info[0]
print(name)
address = my_info[1]
print(address)

# accessing last elements
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

# Add element on last position
fruits.append("lime")
print(fruits)

# Add element on specific position
fruits.insert(2, "lemon")
print(fruits)

# Remove specific element
fruits.remove("lime")
print(fruits)

# Remove last element
fruits.pop()
print(fruits)

# Remove element by index number
fruits.pop(0)
print(fruits)

# Slice
special_fruit = fruits[0:2]
print(special_fruit)

# Element Search
fruit_search = 'apple' in fruits
print(fruit_search)

# index
index = fruits.index('lemon')
print(index)

# sort
age = [12, 23, 44, 5, 67]
age_sort = age.sort()
print(age_sort)

# clear
age.clear()
print(age)
