#!/usr/bin/python3
"""
0-lookup module
Defines a function that returns the list of available
attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)