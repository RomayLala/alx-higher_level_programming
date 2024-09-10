#!/usr/bin/python3

def print_last_digit(number):
    """
    Print the last digit of a number and return it.
    
    Args:
        number (int): The number from which to extract the last digit.
        
    Returns:
        int: The last digit of the number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit
