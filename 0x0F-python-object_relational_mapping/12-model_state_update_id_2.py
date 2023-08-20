#!/usr/bin/python3
"""
this module houses the model_state class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    root password hbtn_0e_0_usa
    Change the name of the State where id = 2 to New Mexico
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    conn = engine.connect()
    stmt = State.update(). \
        values(name="new_mexico"). \
        where(State.id == 2)
    conn.execute(stmt)
    conn.close()
