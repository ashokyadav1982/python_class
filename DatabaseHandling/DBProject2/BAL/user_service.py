from DAL.user_repo import UserRepository
from BAL.user_model import User

class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def register_user(self, name, email):
        user = User(name=name, email=email)
        return self.repo.create(user)

    def get_user(self, user_id):
        return self.repo.get(user_id)

    def update_user(self, user_id, name, email):
        user = User(id=user_id, name=name, email=email)
        self.repo.update(user)
        return user

    def delete_user(self, user_id):
        self.repo.delete(user_id)
