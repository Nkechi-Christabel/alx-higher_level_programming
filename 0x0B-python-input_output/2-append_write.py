#!/usr/bin/python3

"""
This module(2-append__file.py) contains a function write_file(), that
appends a string at the end of a text file (UTF8) and returns the
number of characters written
"""


def append_write(filename="", text=""):
    """
    Writes the given text to the end file and returns the number of
    characters  written.

    Args:
        filename (str): The name of the text file to write to. If not provided,
                        an empty string is assumed.

        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
