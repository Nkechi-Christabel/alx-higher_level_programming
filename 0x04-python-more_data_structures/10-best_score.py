#!/usr/bin/python3

"""A function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    return (max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
            if a_dictionary else None)
