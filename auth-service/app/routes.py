from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.security import hash_password, verify_password, create_access_token
from backend.app.database import get_db  # Импортируем get_db из внешнего файла

auth_router = APIRouter()

@auth_router.post("/register/")
def register_user(username: str, email: str, password: str, is_doctor: bool, db: Session = Depends(get_db)):
    """Регистрация нового пользователя"""
    user_exists = db.query(User).filter((User.username == username) | (User.email == email)).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = hash_password(password)
    new_user = User(username=username, email=email, password_hash=hashed_password, is_doctor=is_doctor)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

@auth_router.post("/login/")
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    """Авторизация пользователя и выдача JWT токена"""
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
