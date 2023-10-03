#!/usr/bin/python3

"""
This module defines a class LockedClass that prevents the
user from creating new instance attributes, except if the new
instance attribute is called first_name.
"""


class LockedClass:
    """
    This class restricts the creation of new instance attributes,
    except for the 'first_name' attribute.

     __slots__ : Allows us to explicitly declare data
    members, causes Python to reserve space for them in memory,
    and prevents the creation of other attributes
    """
    __slots__ = ('first_name', )
