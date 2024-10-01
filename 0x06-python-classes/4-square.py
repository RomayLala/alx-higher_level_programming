#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""


class Square:
    """
    A class used to represent a square.

    Attributes
    ----------
    size : int
        The size (length of a side) of the square (must be a non-negative integer).

    Methods
    -------
    __init__(self, size=0)
        Initializes the square with an optional size parameter.
    area(self)
        Returns the area of the square.
    size(self)
        Getter method for the private size attribute.
    size(self, value)
        Setter method for the private size attribute with validation.
    """
    
    def __init__(self, size=0):
        """
        Initialize a new square with the given size.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute. Validates the input to ensure
        it's a non-negative integer.

        Parameters
        ----------
        value : int
            The new size of the square.

        Raises
        ------
        TypeError
            If the size is not an integer.
        ValueError
            If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
