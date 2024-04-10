"""The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a
block of code for each element in the sequence"""
# for loops
fruits = ['mango', 'apples', 'banana', 'peas', 'peaches']

# loop through the list and print each item in the list
# for fruit in fruits:
#     print(f'{fruit}')

# # loop in range
# for i in range(20):
#     print(i + 1)   # prints 1-20

my_fruit = input("Enter the fruit: ")
# for i in [1, 2, 3, 4, 5]:
#     fruits.append(my_fruit)  # adds my_fruit 5 times
#     for fruit in fruits:
#         print(fruit)
#     # print(i)
for i in [1, 2, 3, 4, 5]:
    if my_fruit in fruits:
        my_fruit = input("Enter the fruit: ")
    else:
        fruits.append(my_fruit)
        for fruit in fruits:
            print(fruit)