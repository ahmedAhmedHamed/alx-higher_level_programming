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
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    with Session(engine) as session:
        new_state = State(name="louisiana")
        session.add(new_state)
        session.commit()
        print(f"{new_state.id}")

