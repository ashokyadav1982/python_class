# A simple file to show the database connection

import psycopg2
from psycopg2 import sql, OperationalError

# create a connection to check the database

def create_connection(db_name, db_user, db_password, db_host, db_port):
    """Create a database connection to a SQLite database"""
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# check connection to database

def main():
    connection = create_connection("insurance", "postgres", "password", "localhost", "5432")
    if connection:
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    main()