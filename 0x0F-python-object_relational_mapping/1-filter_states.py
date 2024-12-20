#!/usr/bin/python3
# This script lists all states with names starting with 'N' from the database 'hbtn_0e_0_usa'
# using MySQLdb to connect to the database and perform the query.

import MySQLdb
import sys

def filter_states():
    """ Connect to MySQL and fetch all states where the name starts with 'N' """
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server using MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch states starting with 'N', sorted by id
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows from the result
    states = cursor.fetchall()

    # Print each state in the required format
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()
