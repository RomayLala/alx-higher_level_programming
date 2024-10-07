#!/usr/bin/python3
"""
This module provides a function 'add_integer' that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers a and b.
    Arguments:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).
    Returns:
        The integer addition of a and b after casting floats to integers.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast floats to integers
    a = int(a)
    b = int(b)
    
    return a + b
