# map
# filter

# def double_numbers(numbers: list) -> list:
#     """
#     This function takes a list as an argument
#     Then doubles the values of the list and appends them to a new list
#
#     :param numbers:
#     :return:
#     """
#     result = []
#
#     for number in numbers:
#         print(number * 2)
#
#     return result


# double_numbers([1, 2, 3])


# map function always returns a new array.The copy of the existing list
# def double(number):
#     return number * 2


# print(list(map(lambda num: num * 2, [1, 2, 3])))
# print(list(map(lambda num: num ** 2, [1, 2, 3])))  # squarea
# print(list(map(double, [1, 2, 3])))  # doubles the list


# filter method. test elements to see whether it is true ot false
numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 6]
print(list(filter(lambda number: number % 2 == 0, numbers)))
# def even_number(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     print(result)


# even_number(numbers)

# using filters
