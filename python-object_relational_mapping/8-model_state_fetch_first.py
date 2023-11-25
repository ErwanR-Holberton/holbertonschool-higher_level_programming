#!/usr/bin/python3
"""Print first state"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    s = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(s, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    State_obj = Session().query(State).order_by(State.id).first()
    if State_obj is None:
        print("Nothing")
    else:
        print("{}: {}".format(State_obj.id, State_obj.name))
    Session().close()
