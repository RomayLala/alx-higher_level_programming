#!/usr/bin/python3
"""
Module for Square class that inherits from Rectangle.
"""

from rectangle import Rectangle  # Assumes Rectangle is in 9-rectangle.py


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.
    
    Attributes:
        size (int): The size of the square (width and height).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call the Rectangle initializer

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
