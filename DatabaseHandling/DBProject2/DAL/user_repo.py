from BAL.user_model import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, user: User):
        cursor = self.db.get_cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            (user.name, user.email)
        )
        user.id = cursor.fetchone()[0]
        cursor.close()
        return user

    def get(self, user_id):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(id=row[0], name=row[1], email=row[2])
        return None

    def update(self, user: User):
        cursor = self.db.get_cursor()
        cursor.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (user.name, user.email, user.id)
        )
        cursor.close()

    def delete(self, user_id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        cursor.close()
