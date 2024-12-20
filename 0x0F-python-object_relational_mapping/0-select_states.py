#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
The results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print each row in the result
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
