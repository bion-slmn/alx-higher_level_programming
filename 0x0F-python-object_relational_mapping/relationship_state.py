#!/usr/bin/python3
'''This module has class definition of a State and
an instance Base = declarative_base()'''

from relationship_city import City, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import sys


class State(Base):
    '''This defines a class state that links to a table
    in the database'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')


# City.state = relationship('State', back_populates='cities')
