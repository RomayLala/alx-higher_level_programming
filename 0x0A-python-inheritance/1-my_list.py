#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and provides
    an additional method to print a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints the list, but in ascending order.
        """
        print(sorted(self))

