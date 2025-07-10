# from DAL.database import Database
from user_repo import UserRepository
# from DBProject2.BAL.user_service import UserService
from database import Database
def main():
    db = Database()
    user_repo = UserRepository(db)

    # Create
    user = user_repo.create("Neeraj", "neerajkarna12@gmail.com")
    print("Created:", user)

    # Read
    fetched = user_repo.get(user.id)
    print("Fetched:", fetched)

    # Update
    updated = user_repo.user_update(user_id=user.id,name="Neeraj Kumar Karna", email="karna1.neeraj@gmail.com")
    print("Updated user:", updated.id)

    # Delete
    # service.delete_user(user.id)
    # print("Deleted user with ID:", user.id)

    db.close()

if __name__ == "__main__":
    main()
