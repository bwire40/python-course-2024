# Lists - arrays in python
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(type(numbers))  # list

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
