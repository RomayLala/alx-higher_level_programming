#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a BaseGeometry class with an area method.
"""

class BaseGeometry:
    """
    A class representing basic geometry operations.
    """

    def area(self):
        """
        Method that raises an exception indicating that
        the area calculation is not implemented.
        
        Raises:
            Exception: with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
