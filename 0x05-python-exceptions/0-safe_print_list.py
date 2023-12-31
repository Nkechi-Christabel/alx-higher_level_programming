#!/usr/bin/python3

"""Prints x elements of a list.

Args:
   my_list: The list to print.
   x: The number of elements to print.

Returns:
   The real number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for el in my_list[:x]:
            print(el, end="")
            count += 1
    except IndexError:
        pass

    print()
    return (count)
