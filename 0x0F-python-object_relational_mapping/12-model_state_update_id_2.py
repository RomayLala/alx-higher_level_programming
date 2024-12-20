#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Update the name of the state with id 2 to 'New Mexico'."""
    
    # Get the command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        # Update the state name to "New Mexico"
        state.name = "New Mexico"
        session.commit()  # Commit the changes

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
