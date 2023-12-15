#!/usr/bin/python3
"""
The script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa and prints its ID using the with statement.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:\
                           3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state = State(name="Louisiana")
        session.add(new_state)

        session.commit()

        print(new_state.id)
