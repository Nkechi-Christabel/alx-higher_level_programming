#!/usr/bin/python3

"""
This is "2-matrix_divided" module.

The 2-matrix_divided supplies one function, matrix_divided(), that divides
all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide all elements by.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to
        2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) and all(isinstance(x, (int, float))
                                             for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([[round(x / div, 2) for x in row] for row in matrix])
