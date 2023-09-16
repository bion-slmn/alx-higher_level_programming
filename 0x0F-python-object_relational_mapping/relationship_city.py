#!/usr/bin/python3
'''This module has class definition of a State and
an instance Base = declarative_base()'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import sys


Base = declarative_base()


class City(Base):
    '''This defines a class state that links to a table
    in the database'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
