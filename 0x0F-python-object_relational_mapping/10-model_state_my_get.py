#!/usr/bin/python3
# 10-model_state_my_get.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Query the database and display the id of a state by name"""

    # Check if we have the right number of arguments
    if len(sys.argv) != 5:
        return

    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the connection to the MySQL server using SQLAlchemy
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state
    state = session.query(State).filter(State.name == state_name).first()

    # If a state was found, print its id. Otherwise, print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
