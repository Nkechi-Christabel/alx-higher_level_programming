#!/usr/bin/python3

"""A function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    return ({k: v * 2 for k, v in a_dictionary.items()})
