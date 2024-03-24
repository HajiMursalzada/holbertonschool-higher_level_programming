#!/usr/bin/python3
""" Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa """

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    tmp = None

    for state in session.query(State).order_by(State.id):
        if (sys.argv[4] == state.name):
            tmp = state.id

    if (tmp):
        print(tmp)
    else:
        print("Not found")
