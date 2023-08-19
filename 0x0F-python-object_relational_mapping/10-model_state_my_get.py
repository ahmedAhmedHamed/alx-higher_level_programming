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
    root password hbtn_0e_0_usa Texas
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name_searched = argv[4]
    safe_state_name_searched = state_name_searched.split(';', 1)[0]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    with Session(engine) as session:
        results = session.query(State
                                ).where(
            State.name == safe_state_name_searched)

        for result in results:
            print(f"{result.id}: {result.name}")
