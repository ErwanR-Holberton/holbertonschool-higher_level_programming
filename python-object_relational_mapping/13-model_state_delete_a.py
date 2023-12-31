#!/usr/bin/python3
"""Removes states containing a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    s = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(s, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()

    session.close()
