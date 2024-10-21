#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x coordinate of the square (default is 0).
            y (int): The y coordinate of the square (default is 0).
            id (int, optional): The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance.

        Returns:
            str: A formatted string in the form [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it is a positive integer.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes.

        Args:
            *args: Non-keyword arguments for updating attributes.
                1st argument: id
                2nd argument: size
                3rd argument: x
                4th argument: y
            **kwargs: Keyword arguments for updating attributes.
                Can include 'id', 'size', 'x', 'y'.
        """
        if args and len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        
        # Only use kwargs if args is empty
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square.

        Returns:
            dict: A dictionary containing the id, size, x, and y of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
