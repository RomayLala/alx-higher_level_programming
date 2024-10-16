#!/usr/bin/python3
"""
Module for class_to_json function
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    
    Args:
        obj (object): An instance of a class.
        
    Returns:
        dict: A dictionary containing all serializable attributes.
    """
    return obj.__dict__
