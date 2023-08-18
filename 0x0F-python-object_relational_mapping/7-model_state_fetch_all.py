#!/usr/bin/python3
"""
this module houses the model_state class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}"
                           f"@localhost:3306/{db_name}", echo=True)
    with Session(engine) as session:
        stmt = select(State)
        for state in session.scalars(stmt):
            print(state)
