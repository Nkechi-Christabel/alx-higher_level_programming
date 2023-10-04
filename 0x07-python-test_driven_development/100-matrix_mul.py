#!/usr/bin/python3

"""
This is "100-matrix_mul" module.

The 100-matrix_mul supplies one function, matrix_mul(), that
multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a
        list of lists, or if one element of those list of lists is not an
        integer or a float, or if m_a or m_b is not a rectangle.

        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be
        multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
            for row_a in m_a]
