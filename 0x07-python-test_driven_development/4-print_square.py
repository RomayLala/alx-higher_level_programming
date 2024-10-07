#!/usr/bin/python3
"""
This module defines the print_square function, which prints
a square using the '#' character based on the given size.
"""

def print_square(size):
    """
    Prints a square of the given size using the '#' character.
    
    Args:
        size (int): The size of the square to print.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
