#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """List all State objects from the database that contain the letter 'a'."""
    
    # Retrieve the arguments passed in the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to find states where 'a' is in the name, ordered by state.id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results, displaying only the state.id and state.name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
