#!/usr/bin/python3
"""
This module defines the Square class that represents a square.
"""


class Square:
    """
    A class to represent a square.
    
    Attributes:
        size (int): The size of the square.
    
    Methods:
        __init__(size=0): Initializes a square with the given size.
        size(): Retrieves the size of the square.
        size(value): Sets the size of the square.
        area(): Returns the current area of the square.
        my_print(): Prints the square using the '#' character.
    """
    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'.
        
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
