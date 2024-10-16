#!/usr/bin/python3
"""
This module contains a function that converts a JSON string
into a Python data structure.
"""

import json

def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: A Python object (e.g., list, dict) represented by the JSON string.
    """
    return json.loads(my_str)
