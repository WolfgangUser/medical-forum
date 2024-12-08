from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse, ForumPostCreate, ForumPostResponse, ForumCommentCreate, ForumCommentResponse
from app.crud import create_user, create_post, create_comment
from backend.app.database import get_db

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.post("/posts/", response_model=ForumPostResponse)
def create_new_post(post: ForumPostCreate, db: Session = Depends(get_db), user_id: int = 1):
    return create_post(db=db, post=post, user_id=user_id)

@router.post("/posts/{post_id}/comments/", response_model=ForumCommentResponse)
def create_new_comment(post_id: int, comment: ForumCommentCreate, db: Session = Depends(get_db), user_id: int = 1):
    return create_comment(db=db, comment=comment, user_id=user_id, post_id=post_id)
