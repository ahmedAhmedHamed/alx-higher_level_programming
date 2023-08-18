#!/usr/bin/python3
"""
this module houses the model_state class
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State

    """
    root password hbtn_0e_0_usa
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    with Session(engine) as session:
        result = session.query(State).limit(1)

        print(f"{result.all()[0].id}: {result.all()[0].name}")
        if len(result.all()) == 0:
            print("Nothing")
