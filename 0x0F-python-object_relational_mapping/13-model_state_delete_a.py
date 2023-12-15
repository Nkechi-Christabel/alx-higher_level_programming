#!/usr/bin/python3
"""
The script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306\
                           /{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        states_to_delete = session.query(State).filter(State.name.
                                                       contains('a')).all()

        for state in states_to_delete:
            session.delete(state)

        session.commit()
