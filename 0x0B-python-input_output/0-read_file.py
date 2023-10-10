#!/usr/bin/python3

"""
This module(0-read_file.py) contains a function read_file(), that
reads a text file(UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a text file.

    Args:
        filename (str): The name of the text file to be read. If not
                        provided, an empty string is assumed.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
