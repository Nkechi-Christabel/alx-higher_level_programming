#!/usr/bin/python3

"""Prints the first x elements of a list and only integers.

Args:
    my_list: The list to print from.
    x: The number of elements to access in my_list.

Returns:
    The real number of integers printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return (count)
