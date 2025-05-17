from db import engine, SessionLocal, Base
from models import User

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def get_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        return user

def update_user(user_id: int, name: str, email: str):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.email = email
            session.commit()
            session.refresh(user)
        return user

def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        return user
    
if __name__ == "__main__":
    # Example usage
    user = create_user("Niraj", "niraj.karn1@gmail.com")
    print('Created:', user)
    
    fetched = get_user(user.id)
    print('Fetched:', fetched)
    
    updated = update_user(user.id, "Niraj Prasad Karn", "niraj.karn1@gmail.com")
    print('Updated:', updated)
    
    # deleted = delete_user(user.id)
    # print('Deleted:', deleted)