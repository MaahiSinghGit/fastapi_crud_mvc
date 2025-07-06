from sqlalchemy.orm import Session
from models.user import User


class UserService:
    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def create_user(name: str, email: str, db: Session):
        new_user = User(name=name, email=email)
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def delete_user(user_id: int, db: Session):
        user = db.query(User).get(user_id)
        if user:
            db.delete(user)
            db.commit()
        return user

    @staticmethod
    def update_user(user_id: int, name: str, email: str, db: Session):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.email = email
            db.commit()
        return user
