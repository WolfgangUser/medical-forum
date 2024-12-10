from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session, declarative_base
import os

# Настройки базы данных
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/medical_forum')

# Инициализация базы данных
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модели базы данных
class Topic(Base):
    __tablename__ = 'topics'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)  # ID автора темы
    
    replies = relationship('Reply', back_populates='topic')

class Reply(Base):
    __tablename__ = 'replies'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)  # ID автора ответа
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    
    topic = relationship('Topic', back_populates='replies')


# Схемы для запросов и ответов (Pydantic модели)
class TopicCreate(BaseModel):
    title: str
    content: str
    author_id: int  # ID автора темы

class ReplyCreate(BaseModel):
    content: str
    author_id: int  # ID автора ответа
    topic_id: int  # ID темы, к которой добавляется ответ


# Инициализация FastAPI приложения
app = FastAPI()


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Создать тему
@app.post("/topics/", response_model=dict)
def create_topic(topic: TopicCreate, db: Session = Depends(get_db)):
    new_topic = Topic(
        title=topic.title,
        content=topic.content,
        author_id=topic.author_id
    )
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return {"message": "Тема успешно создана", "topic_id": new_topic.id}


# 🔹 Получить список всех тем
@app.get("/topics/", response_model=list)
def get_all_topics(db: Session = Depends(get_db)):
    topics = db.query(Topic).all()
    return topics


# 🔹 Получить тему по ID
@app.get("/topics/{topic_id}", response_model=dict)
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    return topic


# 🔹 Добавить ответ к теме
@app.post("/replies/", response_model=dict)
def create_reply(reply: ReplyCreate, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == reply.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    
    new_reply = Reply(
        content=reply.content,
        author_id=reply.author_id,
        topic_id=reply.topic_id
    )
    db.add(new_reply)
    db.commit()
    db.refresh(new_reply)
    return {"message": "Ответ успешно добавлен", "reply_id": new_reply.id}


# 🔹 Получить все ответы по ID темы
@app.get("/topics/{topic_id}/replies/", response_model=list)
def get_replies_by_topic(topic_id: int, db: Session = Depends(get_db)):
    replies = db.query(Reply).filter(Reply.topic_id == topic_id).all()
    return replies


# 🔹 Удалить тему по ID
@app.delete("/topics/{topic_id}", response_model=dict)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    
    db.delete(topic)
    db.commit()
    return {"message": "Тема успешно удалена"}


# 🔹 Удалить ответ по ID
@app.delete("/replies/{reply_id}", response_model=dict)
def delete_reply(reply_id: int, db: Session = Depends(get_db)):
    reply = db.query(Reply).filter(Reply.id == reply_id).first()
    if not reply:
        raise HTTPException(status_code=404, detail="Ответ не найден")
    
    db.delete(reply)
    db.commit()
    return {"message": "Ответ успешно удалён"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
