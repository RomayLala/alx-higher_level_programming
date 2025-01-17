#!/usr/bin/python3
"""
Function to find a peak element in a list of integers.
It uses binary search to find the peak in O(log n) time.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of integers.

    Args:
        list_of_integers (list): A list of integers.
    
    Returns:
        int: A peak element from the list.
    """
    if not list_of_integers:
        return None
    
    def binary_search(low, high):
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search(low, mid - 1)
        else:
            return binary_search(mid + 1, high)
    
    return binary_search(0, len(list_of_integers) - 1)
