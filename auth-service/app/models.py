from sqlalchemy import Column, Integer, String, Boolean
from backend.app.database import Base  # Используем Base из внешнего модуля

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_doctor = Column(Boolean, default=False)  # Разделение прав доступа на пациента и врача
