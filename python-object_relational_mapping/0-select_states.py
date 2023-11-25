#!/usr/bin/python3
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base
from sys import argv


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(50))


engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
