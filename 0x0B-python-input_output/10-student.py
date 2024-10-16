#!/usr/bin/python3
"""
This module defines a Student class with methods to return
JSON representation of the student's attributes.
"""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes
        must be retrieved.

        Args:
            attrs (list, optional): The list of attributes to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}
