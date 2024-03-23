#!/usr/bin/python3
"""
A python file thait contains the class definition of a City
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
import sys

if __name__ == "__main__":
    UN = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(UN, PW, BASE))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    for cities in (session.query(City.name, City.id, State.name).filter
            (State.id == City.state_id)):
        print(cities[2] + ": (" + str(cities[1]) + ") " + cities[0])

    session.close()
