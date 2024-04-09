# Sets in Python are unordered collections of unique elements. They are useful for various tasks such as removing
# duplicate elements from a list, performing mathematical set operations like union, intersection, difference,
# etc. Sets are defined using curly braces {} or the set() constructor.

# list1 = ['ruby', 'python', 'js']
# list2 = ['ruby', 'sql', 'java', 'js']

# concatenating lists
# languages = list1 + list2
# print(programming_list)

# sets have no duplicates, are also not indexed.
# convert out programming list into a set using set constructor
# programming_list = set(programming_list)
# print(programming_list)

"""
# >>>>unique() takes in a list of programming languages with duplicates
# >>>>returns unique list with unique elements
"""


def unique(languages):
    languages = list(set(languages))
    print(languages)


unique(['ruby', 'sql', 'java', 'js', 'ruby', 'sql'])
