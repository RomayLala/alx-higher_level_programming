#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Connect to MySQL, query the first State, and display it."""
    
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Create the database connection URL
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}", pool_pre_ping=True)

    # Create all tables if they don't exist (this is just a precautionary step)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object from the 'states' table
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
