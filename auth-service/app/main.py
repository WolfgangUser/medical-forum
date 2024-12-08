from fastapi import FastAPI
from app.routes import auth_router

app = FastAPI(title="Auth Service")

# Подключение маршрутов
app.include_router(auth_router)