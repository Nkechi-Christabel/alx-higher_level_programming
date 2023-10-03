#!/usr/bin/python3

"""
This is "5-text_indentation" module.

The 5-text_indentation supplies one function, text_indentation(), that prints
a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Indent the text with two new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If the input 'text' is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = text

    for delim in ".:?":
        string = (delim + "\n\n").join([line.strip() for line in
                                       string.split(delim)])

    print(string, end="")
