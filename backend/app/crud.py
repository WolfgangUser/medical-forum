from sqlalchemy.orm import Session
from app.models import User, ForumPost, ForumComment
from app.schemas import UserCreate, ForumPostCreate, ForumCommentCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        role="patient"  # по умолчанию создается пациент
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_post(db: Session, post: ForumPostCreate, user_id: int):
    db_post = ForumPost(**post.dict(), author_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def create_comment(db: Session, comment: ForumCommentCreate, user_id: int, post_id: int):
    db_comment = ForumComment(**comment.dict(), author_id=user_id, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
