from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Получаем URL для подключения к БД
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@database:5432/medical_forum"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Функция для получения сессии с базой данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
