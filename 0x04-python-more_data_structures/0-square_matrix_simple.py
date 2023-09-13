#!/usr/bin/python3

""" A function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    return ([[n * n for n in row] for row in matrix])
