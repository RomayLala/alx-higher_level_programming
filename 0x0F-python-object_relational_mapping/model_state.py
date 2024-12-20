#!/usr/bin/python3
"""Defines the State class and links it to the 'states' table in the database using SQLAlchemy"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# Create the base class
Base = declarative_base()

class State(Base):
    """State class links to the 'states' table in the database."""
    
    # Table name in the MySQL database
    __tablename__ = 'states'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Return the string representation of the State object."""
        return f"State(id={self.id}, name={self.name})"

if __name__ == "__main__":
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create the tables in the database (if not already created)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check for duplicates before adding a new state
    state_name = "California"  # Example state name to be inserted
    existing_state = session.query(State).filter_by(name=state_name).first()
    
    if not existing_state:
        # Insert the new state if it doesn't already exist
        new_state = State(name=state_name)
        session.add(new_state)
        session.commit()
        print(f"Added new state: {new_state}")
    else:
        print(f"State {state_name} already exists.")
    
    # Close the session
    session.close()
