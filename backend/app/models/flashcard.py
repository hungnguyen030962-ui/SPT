from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class EnglishFlashcard(Base):
    __tablename__ = "english_flashcards"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(100), nullable=False, index=True)
    ipa = Column(String(100), nullable=True)
    meaning = Column(String(200), nullable=False)
    part_of_speech = Column(String(50), nullable=True)
    example = Column(Text, nullable=True)
    topic = Column(String(100), nullable=True, index=True)
