FROM nginx:latest

# Копируем конфигурацию серверного блока (default.conf)
COPY ./default.conf /etc/nginx/conf.d/default.conf

# Копируем статические файлы и шаблоны
COPY ./templates/ /usr/share/nginx/html/
COPY ./static/ /usr/share/nginx/html/static/

# Открываем порт 80
EXPOSE 80
