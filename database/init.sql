CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE SCHEMA IF NOT EXISTS medical_forum;

CREATE TABLE IF NOT EXISTS medical_forum.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_doctor BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS medical_forum.topics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES medical_forum.users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_anonymous BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS medical_forum.comments (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES medical_forum.topics(id),
    user_id INTEGER REFERENCES medical_forum.users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_topics_user_id ON medical_forum.topics(user_id);
CREATE INDEX IF NOT EXISTS idx_comments_topic_id ON medical_forum.comments(topic_id);
CREATE INDEX IF NOT EXISTS idx_comments_user_id ON medical_forum.comments(user_id);