#!/usr/bin/python3
import MySQLdb
import sys

def main():
    """ Connects to MySQL, performs a query to search states, and displays results """
    
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_password, db=database_name, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the query to search for states matching the given name (case-sensitive)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all results from the executed query
    rows = cursor.fetchall()

    # Display the results in the required format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
