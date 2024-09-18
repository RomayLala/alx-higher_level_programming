#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' with 'replace' in a new list.
    
    Args:
        my_list: List of elements to search through.
        search: The element to be replaced.
        replace: The new element to replace 'search'.
    
    Returns:
        A new list with 'search' replaced by 'replace'.
    """
    return [replace if element == search else element for element in my_list]
