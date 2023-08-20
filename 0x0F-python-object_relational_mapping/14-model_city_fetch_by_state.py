#!/usr/bin/python3
"""
this module houses the model_state class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    with Session(engine) as session:
        query = session.query(City, State).join(State)
        for city, state in query.all():
            print(f"{state.name}: ({city.id}) {city.name}")
