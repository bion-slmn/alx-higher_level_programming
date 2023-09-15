#!/usr/bin/python3
'''This module lists all State objects from the database hbtn_0e_6_usa'''
from model_state import Base, State
from model_city import City
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

    row = session.query(State).join(City). \
        filter(State.id == City.state_id).all()
    for r in row:
        for citi in r.cities:
            print(f'{r.name}: ({citi.id}) {citi.name}')
    session.commit()
    session.close()
