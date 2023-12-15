#!/usr/bin/python3
"""
The script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py) .
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:\
                           3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state = State(name="California")
        new_state.cities = [City(name="San Francisco")]
        session.add(new_state)

        session.commit()
