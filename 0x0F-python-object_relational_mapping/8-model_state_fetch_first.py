#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

Base = declarative_base()
import sys
if __name__ == "__main__":
    engine = database_url = "mysql+pymysql://{}:{}@localhost:3306/{}".format(sys.argv[1], sys,argv[2], sys.argv[3]
    Base.matadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    all_user = session.query(States).all()
    print(all_user)
