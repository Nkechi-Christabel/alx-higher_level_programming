#!/usr/bin/python3
"""
This module defines a SQLAlchemy model for the 'Cities' table.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from model_state import Base

class City(Base):
    """
    Represents a city in the 'cities' table.

    Attributes:
        id (int): An auto-generated, unique integer acting as the primary key.
        name (str): A string column with a maximum length of 128 characters,
        representing the city name.
        state_id (int): An integer, a foreign key linking to the states table 
                        using its id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False) 
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
