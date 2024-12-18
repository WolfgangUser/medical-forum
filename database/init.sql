-- Удаляем существующие таблицы, чтобы избежать ошибок при повторной инициализации
DROP TABLE IF EXISTS replies CASCADE;
DROP TABLE IF EXISTS topics CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- ===================================
-- 🔐 Таблица для сервиса авторизации (auth-service)
-- ===================================
CREATE TABLE users (
    id SERIAL PRIMARY KEY,               -- Уникальный идентификатор пользователя
    username VARCHAR(100) UNIQUE NOT NULL, -- Уникальное имя пользователя
    password VARCHAR(255) NOT NULL,      -- Пароль (возможно, без хэширования)
    role VARCHAR(50) DEFAULT 'user',     -- Роль пользователя (например, 'user' или 'doctor')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата создания записи
);

-- Добавим несколько пользователей для теста
INSERT INTO users (username, password, role) 
VALUES 
    ('admin', 'admin', 'doctor'), 
    ('user', 'user', 'user');

-- ===================================
-- 📜 Таблица для тем форума (backend)
-- ===================================
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,               -- Уникальный идентификатор темы
    title VARCHAR(255) NOT NULL,         -- Название темы
    content TEXT NOT NULL,               -- Содержимое темы
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата создания темы
);

-- Добавим несколько тестовых тем
INSERT INTO topics (title, content) 
VALUES 
    ('Как лечить кашель?', 'Какие методы лучше использовать для лечения сухого кашля?'), 
    ('Что делать при температуре 38?', 'Какие лекарства лучше принимать при высокой температуре?');

-- ===================================
-- 💬 Таблица для ответов на темы (backend)
-- ===================================
CREATE TABLE replies (
    id SERIAL PRIMARY KEY,               -- Уникальный идентификатор ответа
    content TEXT NOT NULL,               -- Содержимое ответа
    author_id INTEGER NOT NULL,          -- ID автора ответа (ссылка на таблицу users)
    topic_id INTEGER NOT NULL,           -- ID темы, к которой относится ответ (ссылка на таблицу topics)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Дата создания ответа
    FOREIGN KEY (author_id) REFERENCES users (id) ON DELETE CASCADE, -- Внешний ключ для связи с users
    FOREIGN KEY (topic_id) REFERENCES topics (id) ON DELETE CASCADE -- Внешний ключ для связи с topics
);

-- Добавим несколько тестовых ответов
INSERT INTO replies (content, author_id, topic_id) 
VALUES 
    ('Попробуйте пить больше воды и использовать сироп от кашля.', 2, 1), 
    ('Рекомендуется принимать парацетамол и наблюдать за температурой.', 1, 2);

-- ===================================
-- ✅ Завершение и вывод статуса
-- ===================================
-- Выводим сообщение для подтверждения успешного выполнения скрипта
DO $$ 
BEGIN 
    RAISE NOTICE 'База данных инициализирована успешно'; 
END $$;
