#!/usr/bin/python3
"""
The script that lists all City objects from the database hbtn_0e_101_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:\
                           3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        data = session.query(City).order_by(City.id).all()

        for city in data:
            print(f"{city.id}: {city.name} -> {city.state.name}")
