#!/usr/bin/python3
"""Module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all element of a matrix by a given div.

    Parameters:
    matrix: Lists of integers or floats.
    div: The number to divide each element by.

    Return:
    return a new matrix list with all element divide.
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for a in row:
            if type(a) != int and type(a) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = set(len(row) for row in matrix)
    if len(size) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    result = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        result.append(new_row)
    return (result)
