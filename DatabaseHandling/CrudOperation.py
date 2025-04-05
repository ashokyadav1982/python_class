# A program to handle the CRUD operations in the database

# import the necessary libraries
import psycopg2
from psycopg2 import sql, OperationalError, pool

# create a connection pool
connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    database = "insurance",
    user = "postgres",
    password = "password",
    host = "localhost",
    port = "5432"
)

# function to return a connection from the pool
def get_connection():
    """_summary_

    Returns:
        _type_: _description_
    """

    try:
        connection = connection_pool.getconn()
        return connection
    except Exception as e:
        print(f"Error getting connection from pool: {e}")
        return None
   
# function to return a connection to the pool
def release_connection(connection):
    """_summary_
    Args:
        connection (_type_): _description_
    """
    try:
        connection_pool.putconn(connection)
    except Exception as e:
        print(f"Error returning connection to pool: {e}")

def get_records(connection, limit=10):
    """_summary_

    Args:
        connection (_type_): _description_
        limit (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    try:
        cursor = connection.cursor()
        cursor.execute(sql.SQL("SELECT * FROM public.person LIMIT {}").format(sql.Placeholder()), [limit])
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(f"Error getting records: {e}")
        return None
    
def main():
    """_summary_"""
    conn = None
    try:
        conn = get_connection()
        if conn:
            records = get_records(conn, 5)
            print(records)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            release_connection(conn)

if __name__ == "__main__":
    main()