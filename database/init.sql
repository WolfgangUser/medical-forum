-- Удаляем таблицы, если они существуют
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS users;

-- Создаем таблицу пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('patient', 'doctor')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем таблицу тем форума
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем таблицу комментариев
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Тестовые данные
INSERT INTO users (email, password_hash, role) VALUES 
('patient1@example.com', 'hashed_password_1', 'patient'),
('doctor1@example.com', 'hashed_password_2', 'doctor');

INSERT INTO topics (user_id, title, content) VALUES 
(1, 'Боль в спине', 'У меня уже несколько дней болит спина, что делать?');

INSERT INTO comments (topic_id, user_id, content) VALUES 
(1, 2, 'Сделайте МРТ и обратитесь к врачу.');
