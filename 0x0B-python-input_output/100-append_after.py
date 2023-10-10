#!/usr/bin/python3

"""
This module(100-append_after.py) contains function def pascal_
triangle(n): that returns a list of lists of integers representing
the Pascal’s triangle of n.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string
    in a file.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines containing the
                          search string.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
