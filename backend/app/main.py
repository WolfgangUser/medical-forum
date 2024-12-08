from fastapi import FastAPI
from app.routes import router
from backend.app.database import engine
from app.models import Base  # Импорты базы

app = FastAPI(title="Medical Forum Backend")

# Создаем таблицы при запуске приложения
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Forum Backend"}
