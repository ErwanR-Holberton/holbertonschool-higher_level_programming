#!/usr/bin/python3
"""Show all cities"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    s = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(s, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    states = Session().query(State).all()

    for city in Session().query(City).order_by(City.id).all():
        for state in states:
            if state.id == city.state_id:
                print("{}: ({}) {}".format(state.name, city.id, city.name))

    Session().close()
