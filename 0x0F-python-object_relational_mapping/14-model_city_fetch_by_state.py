#!/usr/bin/python3
"""
This script fetches and displays all City objects from the `cities` table
in the database linked to their corresponding `State` objects.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

def main():
    """
    Connect to MySQL database and fetch all cities linked to their states.
    Display results in the format: <state name>: (<city id>) <city name>
    """

    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their associated state, sorted by city id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
