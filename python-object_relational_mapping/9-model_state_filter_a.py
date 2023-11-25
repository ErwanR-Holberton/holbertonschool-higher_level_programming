#!/usr/bin/python3
"""Select all states with an a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    s = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(s, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    for state in Session().query(State).order_by(State.id).all():
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    Session().close()
