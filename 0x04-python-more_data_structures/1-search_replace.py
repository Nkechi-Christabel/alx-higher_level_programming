#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return (list(map(lambda str: replace if str == search else str, my_list)))
