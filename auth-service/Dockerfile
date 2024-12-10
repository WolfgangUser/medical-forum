FROM python:3.9-slim

WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы внутрь контейнера
COPY . .

# Открываем порт для сервиса
#EXPOSE 8001

# Запуск через run_app.py
CMD python app.py