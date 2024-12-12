from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Конфигурация базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@database:5432/medical_forum")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель пользователя для базы данных
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # Пароль хранится в открытом виде
    role = Column(String, nullable=False)

# Модель для регистрации (Pydantic)
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

# Получаем сессию базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Основное приложение FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Auth Service is up and running!"}

# Роут для регистрации нового пользователя
@app.post('/register/')
async def register_user(user_register: UserCreate, db: Session = Depends(get_db)):
    username = user_register.username
    # Проверяем, существует ли уже пользователь с username
    existing_user = db.query(User).filter((User.username == username)).first()
    
    if existing_user:
        raise HTTPException(status_code=401, detail="Username already registered")
    
    # Сохраняем нового пользователя в базе данных (пароль сохраняется в открытом виде)
    new_user = User(username, password=user_register.password, role=user_register.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully", "user_id": new_user.id}

# Роут для логина пользователя
@app.post('/login/')
async def login_user(user_login: UserLogin, db: Session = Depends(get_db)):
    username = user_login.username
    password = user_login.password

    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {"message": "Login successful", "user_id": user.id}


# try:
#     db.query(User).first()
#     print("Database connection successful")
# except Exception as e:
#     print(f"Database connection error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)