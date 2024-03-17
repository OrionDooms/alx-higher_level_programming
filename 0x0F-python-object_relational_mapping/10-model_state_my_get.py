#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
"""
a program that prints the State object with the name passed as argument
from the database
"""
if __name__ == "__main__":
    UN = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    DB = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(UN, PW, BASE))
    engine = create_engine(DB)
    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).all()

    name = sys.argv[4]
    for S in states:
        if S.name == name:
            result = S.id
            break
        else:
            result = "Not found"
    print(result)

    session.close()
