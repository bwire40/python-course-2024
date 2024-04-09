# Our exercises
# 1. Bigger guy
"""
write a function bigger_guy that takes in two numbers and returns the bier one

MAKE SURE TO USE RETURN AND NOT PRINT IN YOUR FUNCTION
***import this into function calls.py***
"""


def bigger_guy(a: int, b: int) -> int:
    """
    This function checks which number is bigger
    Given 2 numbers return the bigger one

    :param a:
    :param b:
    :return bigger:
    """
    if a > b:
        return a
    else:
        return b
