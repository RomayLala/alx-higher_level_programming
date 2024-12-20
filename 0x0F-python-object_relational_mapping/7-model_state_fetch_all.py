#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Lists all State objects from the database hbtn_0e_6_usa"""

    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}", pool_pre_ping=True)

    # Create all tables in the database (if they do not exist already)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display all states in the desired format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
