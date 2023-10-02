#!/usr/bin/python3

"""
This is "5-text_indentation" module.

The 5-text_indentation supplies one function, text_indentation(), that prints
a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    string = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in text:
        if ch in ".?:":
            string += '\n\n'
        else:
            string += ch

    lines = [line.strip() for line in string.split('\n')]
    print('\n'.join(lines))
