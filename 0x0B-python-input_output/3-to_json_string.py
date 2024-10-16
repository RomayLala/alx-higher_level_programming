#!/usr/bin/python3
"""
Module that defines a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
