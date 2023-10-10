#!/usr/bin/python3

"""
Module: log_parser

This module defines a simple log file parser that reads lines
from standard input, accumulates statistics about the file size
and HTTP status codes, and prints the statistics every 10 lines
or upon receiving a KeyboardInterrupt.

Usage:
    $ cat access.log | python3 log_parser.py

"""


def print_stats(size, status_codes):
    """
    Print file size and HTTP status code statistics.

    Args:
        size (int): The total file size accumulated.
        status_codes (dict): A dictionary containing HTTP status code counts.

    Prints:
        File size: <size>
        HTTP Status Codes in sorted order, along with their counts.

    Example:
        File size: 123456
        200: 5
        301: 2
        404: 3
        ...

    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
