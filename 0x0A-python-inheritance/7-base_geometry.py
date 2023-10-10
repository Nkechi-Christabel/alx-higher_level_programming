#!/usr/bin/python3

"""
This module defines a class BaseGeometry.

It is based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(self): Calculate the area of the geometry (to be implemented by
        subclasses).
        integer_validator(self, name, value): Validate that a value is a
        positive integer.

    Raises:
        Exception: When the 'area' method is called directly (not implemented
        in the base class).
        TypeError: When 'value' is not an integer in 'integer_validator'.
        ValueError: When 'value' is less than or equal to 0 in
        'integer_validator'.
    """
    def area(self):
        """
        Defined method, area. Not Implemented

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Parameters:
            name (str): The name of the value being validated
            (for error messages).
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
