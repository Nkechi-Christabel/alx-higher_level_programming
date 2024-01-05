#!/usr/bin/python3
"""
It finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers (list): A list of unsorted integers.

    Returns:
    - int or None: The peak element in the list. If the list
                   is empty, returns None.

    Algorithm Complexity:
    - O(log(n)): The algorithm uses a binary search approach
                 to efficiently find a peak.

    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
