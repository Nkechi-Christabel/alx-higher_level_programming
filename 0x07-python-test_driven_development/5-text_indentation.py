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
            string += "\n\n"
        else:
            string += ch

    rmv_ldn_space = [paragraphs.strip() for paragraphs in string.split('\n\n')]
    
