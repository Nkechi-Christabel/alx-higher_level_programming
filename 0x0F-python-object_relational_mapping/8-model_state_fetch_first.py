#!/usr/bin/python3
"""
The script that prints the first State object from the database hbtn_0e_6_usa.
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
        instance = session.query(State).order_by(State.id).first()
        if instance:
            print("{}: {}".format(instance.id, instance.name))
        else:
            print("Nothing")
