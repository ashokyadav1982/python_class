from user_model import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, name, email):
        cursor = self.db.get_cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            (name, email)
        )
        uid = cursor.fetchone()[0]
        cursor.close()
        print(f"User created with ID: {uid}")
        return User(id=uid, name=name, email=email)

    def get(self, user_id):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(id=row[0], name=row[1], email=row[2])
        return None

    def user_update(self, user_id, name, email):
        cursor = self.db.get_cursor()
        cursor.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (name, email, user_id)
        )
        cursor.close()
        return User(id=user_id, name=name, email=email)

    def delete(self, user_id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        cursor.close()
        return User(id=user_id, name=None, email=None)
