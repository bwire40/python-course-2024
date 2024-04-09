# Lists - arrays in python.
"""
They are mutable, ordered collections of items, which means you can change the contents of
 a list after it's created,
 and the order of the items is maintained.
 Lists are defined using square brackets [],
 and items within the list are separated by commas.
 """


fruits = ['mango', 'pea', 'blueberry', 'banana', 'orange']

# Methods are functions that are associated with an object.
# They are called on an object and operate on the
# data contained within that object.

# built in methods for lists

# 1. append
fruits.append('pineapple')  # add another item to the end of the list
fruits.append('grapes')  # add another item to the end of the list

# 2. indexing
print(fruits[0])  # indexing starts from 0. the item at index 0 is mango
print(fruits[2])  # blueberry

# the last item in the list
print(fruits[-1])  # grapes

# 3. slicing
print(fruits[0:4])  # gets you the items from index 0 to 3.
print(fruits[0:5:2])  # from:to:step . the step skips the identified
print(fruits[::-1])  # from:to:step . this reverses the array
# slicing can also slice strings


# 4. length
print(len(fruits))  # the length of the array is 7

print(fruits[0:len(fruits)-1])  # get the items from start to the second last


# print(fruits)
# how to always get the last item of an array
