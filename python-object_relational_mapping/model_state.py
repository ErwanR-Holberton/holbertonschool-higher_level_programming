#!/usr/bin/python3
"""class representing states from a database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class representing states from a database"""
    __tablename__ = 'States'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
