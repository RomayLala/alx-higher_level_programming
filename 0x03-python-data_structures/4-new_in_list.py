#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is valid (non-negative and within range)
    if idx < 0 or idx >= len(my_list):
        # Return a copy of the original list if index is invalid
        return my_list[:]
    
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Replace the element at the specified index
    new_list[idx] = element
    
    return new_list
