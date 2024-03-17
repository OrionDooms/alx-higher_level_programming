#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

import sys
if __name__ == "__main__":
    UN = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    DB = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(UN, PW, BASE))
    engine = create_engine(DB)
    session = sessionmaker(bind=engine)
    session = session()

    name = sys.argv[4]
    states = session.query(State).filter(name == State.name)
    try:
        result = states[0].id
    except IndexError:
        result = "Not found"
    print(result)

    session.close()
