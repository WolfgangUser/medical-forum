from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base  # Импорт базы для SQLAlchemy

class ForumPost(Base):
    __tablename__ = "forum_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # Заголовок темы
    content = Column(Text, nullable=False)  # Содержание темы
    author_id = Column(Integer, ForeignKey("users.id"))  # Связь с пользователем
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    # Связь с комментариями
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("forum_posts.id"))  # Связь с темой форума
    author_id = Column(Integer, ForeignKey("users.id"))  # Связь с автором комментария
    content = Column(Text, nullable=False)  # Содержание комментария
    created_at = Column(DateTime, nullable=False)

    # Связь с постом
    post = relationship("ForumPost", back_populates="comments")
