#!/usr/bin/python3
"""
This module defines a SQLAlchemy model for the 'states' table, and
a relationship with the Ctiy class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """
    Represents a state in the 'states' table.

    Attributes:
        id (int): An auto-generated, unique integer acting as the primary key.
        name (str): A string column with a maximum length of 128 characters,
                    representing the state name.
        cities (relationship): A one-to-many relationship with the class City.
                              If the State object is deleted, all linked City
                              objects will be automatically deleted.
                              The reference from a City object to its State is
                              named 'state'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all,\
                          delete-orphan")
