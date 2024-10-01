#!/usr/bin/python3
"""
This module defines the Square class with a private instance attribute `size`.
"""


class Square:
    """
    This class represents a square with a private size attribute.
    """
    
    def __init__(self, size):
        """
        Initializes the square with a private size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute
