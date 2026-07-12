from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.models.flashcard import EnglishFlashcard
from app.schemas.flashcard import EnglishFlashcardCreate
from typing import Optional

def get_flashcard(db: Session, flashcard_id: int):
    return db.query(EnglishFlashcard).filter(EnglishFlashcard.id == flashcard_id).first()

def get_flashcards(
    db: Session,
    topic: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(EnglishFlashcard)
    if topic:
        query = query.filter(EnglishFlashcard.topic == topic)
    return query.offset(skip).limit(limit).all()

def get_random_flashcards(db: Session, limit: int = 10):
    return db.query(EnglishFlashcard).order_by(func.random()).limit(limit).all()

def create_flashcard(db: Session, flashcard: EnglishFlashcardCreate):
    db_flashcard = EnglishFlashcard(**flashcard.model_dump())
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard
