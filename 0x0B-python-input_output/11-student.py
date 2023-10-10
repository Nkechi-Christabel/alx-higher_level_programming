#!/usr/bin/python3

"""
This module(11-student.py) defines a class Student.

It is based on 10-student.py.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert a Student instance to a dictionary representation.

        Args:
            attrs (list of str): A list of attribute names to include in the
             dictionary. If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes of the
            Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr
                    (self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a provided
        dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their
                         values.
        """
        for key, value in json.items():
            setattr(self, key, value)
