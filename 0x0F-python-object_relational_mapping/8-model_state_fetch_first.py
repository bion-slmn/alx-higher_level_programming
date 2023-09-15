#!/usr/bin/python3
'''This module lists all State objects from the database hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()
    print(f'{row.id}: {row.name}') if row else print('Nothing')
    session.close()
