# functions - block of codes that can be reused when called

# function definition def
def say_my_name():
    print('Bwire')
    print('Karol')


# arguments
def say_my_name2(name):
    print(name)


# say_my_name()  # function call
# say_my_name2("Bwire")

def greeting(greet, name):
    print(f'{greet}! {name}')


# greeting('Aloha', 'bwire')
'''
multiple line comments for documentation using the triple quotation'''


# default arguments
# positional arguments
def greeting2(name, greet='Aloha'):
    print(f'{greet}, {name}')


# positional arguments
# greeting2("Bwire","Alohaa")

# named arguments
# greeting2(name='Bwire',greet='Hello')

# sum function, 2 numbers

def sum_calc(a, b):
    """
    Take 2 integers, return their sum
    :param a:
    :param b:
    :return a+b:

    This function can be imported to external files

    """
    return a + b


# result = sum_calc(1, 2)  # returns 3 and stores in results
# print(result)
