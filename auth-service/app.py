from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os

# Настройки подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@database:5432/medical_forum")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модели для SQLAlchemy
class User(Base):
    tablename = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

# Создание сессии с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI приложение
app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login/")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Авторизация пользователя"""
    user = db.query(User).filter(User.username == request.username).first()
    if user and user.password == request.password:
        return {"status": "success", "message": "Login successful", "user_id": user.id}
    raise HTTPException(status_code=401, detail="Invalid credentials")
    
if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)