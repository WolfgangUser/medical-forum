from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_doctor: bool
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class TopicBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_anonymous: bool = True

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    topic_id: int

class Comment(CommentBase):
    id: int
    user_id: int
    topic_id: int
    created_at: datetime

    class Config:
        orm_mode = True