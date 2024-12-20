#!/usr/bin/python3
"""Base module.

This module contains a class Base that will be the base
of all other classes in this project.
"""

import json
import os

class Base:
    """Represents the base model.

    Attributes:
        __nb_objects (int): The number of instantiated Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of a class with attributes set from a dictionary.

        Args:
            dictionary (dict): A dictionary containing attributes to set.

        Returns:
            Base: An instance of the class with attributes set.
        """
        # Create a dummy instance with minimum required attributes
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)  # Dummy width and height for Rectangle
        elif cls.__name__ == 'Square':
            dummy = cls(1)  # Dummy size for Square
        else:
            raise ValueError("Unsupported class")

        # Use the update method to set actual values from the dictionary
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries,
                 or "[]" if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string,
                  or an empty list if json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits from Base.
                               If list_objs is None, an empty list will be saved.
        """
        if list_objs is None:
            list_objs = []

        # Convert each object to a dictionary using the to_dictionary method
        dict_list = [obj.to_dictionary() for obj in list_objs]

        # Get the class name to form the filename
        filename = f"{cls.__name__}.json"

        # Write the JSON string representation to the file
        with open(filename, "w") as file:
            file.write(cls.to_json_string(dict_list))

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: A list of instances of the class, or an empty list if the file does not exist.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()
        
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
