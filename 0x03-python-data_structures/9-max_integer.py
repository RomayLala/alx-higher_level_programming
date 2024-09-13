#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None  # Return None if the list is empty
    max_value = my_list[0]  # Assume the first element is the largest initially
    for num in my_list:
        if num > max_value:
            max_value = num  # Update max_value when a larger number is found
    return max_value
