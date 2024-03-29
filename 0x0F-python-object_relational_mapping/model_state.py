#!/usr/bin/python3
'''This module has class definition of a State and
an instance Base = declarative_base()'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import sys


Base = declarative_base()

# db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
#                     password=sys.argv[2], db=sys.argv[3])


class State(Base):
    '''This defines a class state that links to a table
    in the database'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
