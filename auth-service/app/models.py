from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base  # Импорт базы для SQLAlchemy

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="patient")  # Роль: пациент или врач

    # Связи с другими таблицами (если нужны)
    # Например, можно связать пользователя с таблицей профилей или форумных постов
