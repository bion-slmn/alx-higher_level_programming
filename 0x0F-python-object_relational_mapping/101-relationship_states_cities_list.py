#!/usr/bin/python3
'''lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa'''
from relationship_state import Base, State
from relationship_city import City
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
    result = session.query(State).join(City) \
        .filter(State.id == City.state_id) \
        .order_by(State.id, City.id).all()

    for st in result:
        print(f'{st.id}: {st.name}')
        for citi in st.cities:
            print(f'\t {citi.id}: {citi.name}')

    session.close()
