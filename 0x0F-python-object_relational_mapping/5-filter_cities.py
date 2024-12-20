#!/usr/bin/python3
import MySQLdb
import sys

def main():
    """Connects to MySQL, performs a query to search cities by state, and displays results safely."""
    
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

    # Prepare the query to search for cities in the given state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query safely by passing the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch the result
    rows = cursor.fetchall()

    # Display the cities, formatted as a comma-separated list
    if rows:
        # Join city names with commas
        print(", ".join([row[0] for row in rows]))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
