#!/usr/bin/python3
"""class representing cities from a database"""
from sqlalchemy import Column, Integer as Int, String, ForeignKey
from model_state import Base


class City(Base):
    """class representing cities from a database"""
    __tablename__ = 'cities'
    id = Column("id", Int, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Int, ForeignKey('states.id'), nullable=False)
