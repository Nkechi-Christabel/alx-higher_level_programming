#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:\
                           3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        for city, state in session.query(City, State).join(City)\
                .order_by(City.id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
