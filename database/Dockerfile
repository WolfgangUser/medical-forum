FROM postgres:13

COPY init.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_DB=medical_forum
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt