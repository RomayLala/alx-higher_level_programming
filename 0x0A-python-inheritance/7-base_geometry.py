#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class provides a template for geometric operations.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than 0.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
