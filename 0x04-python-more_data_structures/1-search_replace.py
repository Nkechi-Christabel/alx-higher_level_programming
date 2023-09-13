#!/usr/bin/python3

"""A function that replaces all occurrences of an element by
another in a new list."""


def search_replace(my_list, search, replace):
    return (list(map(lambda str: replace if str == search else str, my_list)))
