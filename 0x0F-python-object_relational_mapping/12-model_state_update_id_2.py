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

    second_id = session.query(State).filter_by(id=2).first()
    second_id.name = ("New Mexico")
    session.commit()
    session.close()
