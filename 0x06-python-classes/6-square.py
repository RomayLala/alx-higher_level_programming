#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square.
"""


class Square:
    """
    Represents a square with size and position.

    Attributes:
        size (int): The size of the square (private).
        position (tuple): The position of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print the vertical position
        for _ in range(self.__position[1]):
            print("")

        # Print the square with spaces at horizontal position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
