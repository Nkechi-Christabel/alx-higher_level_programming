#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save them to a file
"""

from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(argv[1:])
    save_to_json_file(data, "add_item.json")
