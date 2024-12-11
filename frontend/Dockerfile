FROM nginx:latest

# Копируем конфигурацию серверного блока (default.conf)
#COPY ./default.conf /etc/nginx/conf.d/default.conf

# Копируем статические файлы и шаблоны
COPY ./templates/ /usr/share/nginx/html/
COPY ./js/ /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY . /usr/share/nginx/html
