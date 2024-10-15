#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
