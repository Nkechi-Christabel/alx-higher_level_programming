#!/usr/bin/python3
"""
This is "101-lazy_matrix_mul" module.

The 101-lazy_matrix_mul supplies one function, lazy_matrix_mul(), that
multiplies two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix.
    """
    return np.matmul(m_a, m_b)
