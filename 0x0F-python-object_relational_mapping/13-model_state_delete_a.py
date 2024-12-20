#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    """Deletes all State objects with a name containing the letter 'a'"""
    # Check for correct argument count
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database>")
        return

    # Get the MySQL username, password, and database name from the command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}",
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states table to get all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state that matches the criteria
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
