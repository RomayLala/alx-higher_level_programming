#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Args:
        my_list (list): List of integers.
    Returns:
        int: The sum of all unique integers in the list.
    """
    return sum(set(my_list))
