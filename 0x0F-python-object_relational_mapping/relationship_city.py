#!/usr/bin/python3
'''This module has class definition of a State and
an instance Base = declarative_base()'''


from model_state import Base, State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import sys

# engine = create_engine("mysql+mysqldb://sys.argv[1] \
#                      :sys.argv[2]@localhost/sys.argv[3]")


class City(Base):
    '''This defines a class state that links to a table
    in the database'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

#    state = relationship('State', back_populates='cities')
