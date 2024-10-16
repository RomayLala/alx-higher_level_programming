#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list and saves them to a JSON file.
"""

import sys
import os

# Import the functions from their respective files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the file name
filename = "add_item.json"

# Check if the file exists, if it does, load the existing list, otherwise create an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all the command line arguments to the list (excluding the script name itself)
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
