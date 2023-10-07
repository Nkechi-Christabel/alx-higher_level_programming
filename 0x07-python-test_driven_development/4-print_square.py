#!/usr/bin/python3

"""
This is "4-print_square" module.

The 4-print_square supplies one function, print_square(), that
prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size (length) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if size == 0:
        return
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print('\n'.join(['#' * size for _ in range(size)]))
