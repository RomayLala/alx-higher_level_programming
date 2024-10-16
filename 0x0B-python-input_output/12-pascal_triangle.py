#!/usr/bin/python3
"""
12-pascal_triangle
This module defines a function that generates Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.
    
    Args:
        n (int): The height of the triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle
