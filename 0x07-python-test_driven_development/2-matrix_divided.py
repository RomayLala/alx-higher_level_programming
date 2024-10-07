#!/usr/bin/python3
"""
This module contains a function matrix_divided that divides
all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list): A list of lists of integers/floats.
        div (int/float): The number by which to divide each element.

    Returns:
        list: A new matrix with each element divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if each row of the matrix is not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each element in matrix is an integer or float
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows in the matrix have the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element by div and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
