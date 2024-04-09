"""

Dictionaries in Python are another fundamental data structure.
Unlike lists, which are indexed by a range of numbers,
dictionaries are indexed by keys, which can be of any immutable type (such as strings, numbers, or tuples).
Dictionaries are defined using curly braces {} and consist of key-value pairs separated by colons :.
Dictionaries are mutable - they can be modified. changeable
Starting from Python 3.7, dictionaries maintain the order of insertion of key-value pairs.

"""

person = {
    "name": "Bwire",
    "shirt": "Black",
    "age": 23
}

print(person.values())  # gets all the values in the dictionary
print(person.keys())  # gets all the keys in the dictionary

# 1. Accessing items int the dictionary
# print(person["name"])  # we call the dictionary and give it the key we want
# print(person["shirt"])
# print(person["age"])


# exercise
# def introducer():
#     person2 = {
#         "name": "Bwire",
#         "shirt": "Black",
#         "age": 23,
#         "friends": ['kevin', 'john', 'maggie']
#     }
#
#     print(f'Hi!, my name is {person2["name"]}. My friends include {person2["friends"][2]}')


# introducer()

# 2. Update and assign values


person["shirt"] = "blue"  # changing the value of the key shirt
print(person["shirt"])

# removing
