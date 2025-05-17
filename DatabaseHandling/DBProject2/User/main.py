# from DAL.database import Database
from BAL.user_service import UserService
# from DBProject2.BAL.user_service import UserService
from DAL.database import Database
def main():
    db = Database()
    service = UserService(db)

    # Create
    user = service.register_user("Deepak", "karna.deepak@gmail.com")
    print("Created:", user)

    # Read
    fetched = service.get_user(user.id)
    print("Fetched:", fetched)

    # Update
    updated = service.update_user(user.id, "Deepak Kumar Karna", "karna.deepak@gmail.com")
    print("Updated:", updated)

    # Delete
    # service.delete_user(user.id)
    # print("Deleted user with ID:", user.id)

    db.close()

if __name__ == "__main__":
    main()
