#!/usr/bin/python3
'''This module lists all State objects from the database hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from sqlalchemy import bindparam


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stateName = sys.argv[4]
    row = session.query(State).filter(State.name == stateName).first()
    # print(row)
    print(f'{row.id}') if row else print(f'Not found')
    session.close()
