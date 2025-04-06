# This is the main file for the organized database program.
from PersonCrud1 import PersonCRUD1
from DBConnectory import DBConnector


# Initialize connection pool
DB_CONFIG = {
    "host": "localhost",
    "database": "insurance",
    "user": "postgres",
    "password": "password",
    "port": "5432"
}

def main():
    try:
        # Initialize connection pool
        DBConnector.initialize_pool(**DB_CONFIG)
        
        # Get a connection
        conn = DBConnector.get_connection()
        
        # Initialize CRUD operations
        db = PersonCRUD1(conn)
        
        # Example CRUD operations
        # 1. Create
        driver_id = 17
        name = "deepak"
        address = "bhaktapur"
        
        user_id = db.create_record(driver_id, name, address)
        print(f"Created user with ID: {user_id}")
        
        # 2. Read
        users = db.read_records("person", limit=5)
        for user in users:
            print(user)
        
        # # 3. Update
        # updated_count = db.update_records(
        #     "users",
        #     {"age": 31},  # Updates
        #     {"username": "johndoe"}  # Conditions
        # )
        # print(f"Updated {updated_count} records")
        
        # # 4. Delete
        # deleted_count = db.delete_records(
        #     "users",
        #     {"username": "johndoe"}
        # )
        # print(f"Deleted {deleted_count} records")
        
    except Exception as e:
        print(f"Application error: {e}")
    finally:
        # Release connection and cleanup
        if 'conn' in locals():
            DBConnector.release_connection(conn)
        DBConnector.close_all_connections()

if __name__ == "__main__":
    main()