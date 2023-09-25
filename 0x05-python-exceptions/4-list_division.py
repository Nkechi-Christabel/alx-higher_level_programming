#!/usr/bin/python3

"""Divides element by element 2 lists.

Args:
    my_list_1: First list.
    my_list_2: Second list.
    list_length (int): The number of elements to divide.

Returns:
    A new list (length = list_length) with all divisions.
"""


def list_division(my_list_1, my_list_2, list_length):
    lists = []

    try:
        for i in range(list_length):
            try:
                lists.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                lists.append(0)
            except TypeError:
                print("wrong type")
                lists.append(0)
            except IndexError:
                print("out of range")
                lists.append(0)
    finally:
        return (lists)
