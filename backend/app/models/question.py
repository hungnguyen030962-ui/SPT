from sqlalchemy import Column, Integer, String, Text, JSON
from app.core.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(50), nullable=False, index=True)
    exam_name = Column(String(100), nullable=True, index=True) # e.g. "Đề số 1", "Đề số 2"
    topic = Column(String(100), nullable=False, index=True)
    difficulty = Column(String(20), nullable=False, index=True)
    content = Column(Text, nullable=False)
    passage = Column(Text, nullable=True)
    options = Column(JSON, nullable=False)  # List of strings e.g. ["A...", "B...", "C...", "D..."]
    correct_answer = Column(String(5), nullable=False)  # A, B, C, D
    explanation = Column(Text, nullable=True)
    step_by_step = Column(JSON, nullable=True)  # Detailed steps for math
    formulas = Column(JSON, nullable=True)  # Math formulas list
