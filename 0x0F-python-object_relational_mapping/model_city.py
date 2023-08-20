#!/usr/bin/python3
"""
this module houses the model_state class
"""

from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """state class, same as in table"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
