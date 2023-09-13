#!/usr/bin/python3

"""function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
