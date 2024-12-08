from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.database import Base
from datetime import datetime

class User(Base):
    tablename = "users"
    table_args = {'schema': 'medical_forum'}
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_doctor = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    topics = relationship("Topic", back_populates="user")
    comments = relationship("Comment", back_populates="user")

class Topic(Base):
    tablename = "topics"
    table_args = {'schema': 'medical_forum'}
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("medical_forum.users.id"))
    title = Column(String, index=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_anonymous = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="topics")
    comments = relationship("Comment", back_populates="topic")

class Comment(Base):
    tablename = "comments"
    table_args = {'schema': 'medical_forum'}
    
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("medical_forum.topics.id"))
    user_id = Column(Integer, ForeignKey("medical_forum.users.id"))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    topic = relationship("Topic", back_populates="comments")
    user = relationship("User", back_populates="comments")