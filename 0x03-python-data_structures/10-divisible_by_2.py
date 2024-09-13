#!/usr/bin/python3
"""
Module that contains a function to determine if elements in a list are divisible by 2.
"""

def divisible_by_2(my_list=[]):
    """
    Function that returns a list of boolean values indicating whether
    each element in the input list is divisible by 2.

    Args:
        my_list (list): The list of integers to check.

    Returns:
        list: A list of boolean values.
    """
    return [x % 2 == 0 for x in my_list]
