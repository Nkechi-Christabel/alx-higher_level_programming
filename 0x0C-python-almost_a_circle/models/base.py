#!/usr/bin/python3

"""This module(base.py) defines a class Base."""


class Base:
    """
    The Base class represents the base of a geometric shape.

    Attributes:
        __nb_objects (int): A private class attribute that keeps
        track of the number of instances created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int, optional): An identifier for the instance. If not
            provided, a unique ID is assigned.

        Attributes:
            id (int): The identifier for the instance.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
