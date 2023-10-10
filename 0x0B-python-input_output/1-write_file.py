#!/usr/bin/python3

"""
This module(1-write_file.py) contains a function write_file(), that
writes a string to a text file (UTF8) and returns the number of
characters written
"""


def write_file(filename="", text=""):
    """
    Writes the given text to a file and returns the number of characters
    written.

    Args:
        filename (str): The name of the text file to write to. If not provided,
                        an empty string is assumed.

        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
