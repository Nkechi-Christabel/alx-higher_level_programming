#!/usr/bin/python3
"""
The script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa.
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
    session = Session()

    lou_state = State(name="Louisiana")
    session.add(lou_state)
    session.commit()

    print(lou_state.id)
    session.close()
