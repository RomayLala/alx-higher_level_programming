#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values of the original matrix
    return [[element ** 2 for element in row] for row in matrix]
