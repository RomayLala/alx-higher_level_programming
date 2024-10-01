#!/usr/bin/python3
"""
Module 2-square
Defines a Square class
"""

class Square:
    """
    Class that defines a square with a private instance attribute: size.
    
    Attributes:
        size (int): The size of the square, defaults to 0.
        
    Methods:
        __init__(self, size=0): Initializes the Square with optional size.
    """
    
    def __init__(self, size=0):
        """
        Initializes a square instance with an optional size.
        
        Args:
            size (int): The size of the square. Must be an integer and >= 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
