#!/usr/bin/python3
"""
This module defines a Rectangle class that models a rectangle
"""


class Rectangle:
    """
    A class to define a rectangle with width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height
        Args:
            width (int): The width of the rectangle (default 0)
            height (int): The height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        Args:
            value (int): The width to set
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        Args:
            value (int): The height to set
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle
        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        Returns:
            int: The perimeter of the rectangle
            If width or height is 0, return 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Print the rectangle using the character '#'
        If width or height is 0, return an empty string
        Returns:
            str: String representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation using eval()
        Returns:
            str: String representation for eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")