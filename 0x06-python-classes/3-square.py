#!/usr/bin/python3
"""
This module defines a Square class that models a square with a size attribute.
"""


class Square:
    """
    A class used to represent a square.

    Attributes
    ----------
    size : int
        The size of one side of the square.

    Methods
    -------
    __init__(self, size=0)
        Initializes a square with a given size (optional, default is 0).

    area(self)
        Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        Parameters
        ----------
        size : int
            The size of one side of the square. Must be a non-negative integer.

        Raises
        ------
        TypeError
            If the size is not an integer.
        ValueError
            If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns
        -------
        int
            The area of the square (size squared).
        """
        return self.__size ** 2
