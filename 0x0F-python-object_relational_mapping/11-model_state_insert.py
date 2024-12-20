#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Connect to MySQL and insert 'Louisiana' into the database."""
    # Get arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}')
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if 'Louisiana' already exists in the table
    state = session.query(State).filter(State.name == 'Louisiana').first()

    if not state:
        # If 'Louisiana' does not exist, create a new State object
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()  # Commit the transaction to save the state
        
        # Print the id of the new state
        print(new_state.id)
    else:
        # If 'Louisiana' already exists, print the existing state's id
        print(state.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
