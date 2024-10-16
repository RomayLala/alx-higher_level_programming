#!/usr/bin/python3
"""
This module contains the function `save_to_json_file` which writes
a Python object to a text file using its JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    
    Args:
        my_obj (object): The object to be serialized into JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
