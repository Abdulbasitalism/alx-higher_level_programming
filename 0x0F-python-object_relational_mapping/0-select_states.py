import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database,
                             port=3306,
                             charset="utf8")
        # Create a cursor object
        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
