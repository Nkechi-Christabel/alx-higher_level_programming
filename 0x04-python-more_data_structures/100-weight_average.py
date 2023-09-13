#!/usr/bin/python3

"""A function that returns the weighted average of all
integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if not my_list:
        return (0)

    total = 0
    weight_sum = 0

    for score, weight in my_list:
        total += score * weight
        weight_sum += weight

    return (total / weight_sum)
