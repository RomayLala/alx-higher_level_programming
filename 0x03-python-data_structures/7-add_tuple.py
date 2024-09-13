#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend both tuples to have at least two elements (default to 0)
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    
    # Add the first two elements of both tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result
