#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""
from sqlalchemy import create_engine, func
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

    S = State(name="Louisiana")
    session.add(S)
    session.commit()
    last_id = session.query(func.max(State.id)).scalar()
    print(last_id)
    session.close()
