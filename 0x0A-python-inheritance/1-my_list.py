#!/usr/bin/python3

"""
This module(1-my_list) defines a class MyList that inherits from list.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    This class provides an additional method to print the list in sorted order.

    Methods:
        print_sorted: Print the elements of the list in ascending sorted order.
    """
    def __init__(self):
        """Invoking the constructor of the parent class(list)."""
        super().__init__()

    def print_sorted(self):
        """Print the elements of the list in ascending sorted order."""
        print(sorted(self))
