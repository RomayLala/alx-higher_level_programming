#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.
"""

from 9_rectangle import Rectangle  # Corrected import statement

class Square(Rectangle):
    """
    Square class that represents a square shape.
    """

    def __init__(self, size):
        """
        Initializes the square with a size.

        Parameters:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
