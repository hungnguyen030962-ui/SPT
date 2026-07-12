from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.question import Question
from app.schemas.question import QuestionCreate
from typing import List, Optional

def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def get_questions(
    db: Session,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(Question)
    if subject:
        query = query.filter(Question.subject == subject)
    if topic:
        query = query.filter(Question.topic == topic)
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)
    if search:
        query = query.filter(
            or_(
                Question.content.ilike(f"%{search}%"),
                Question.passage.ilike(f"%{search}%")
            )
        )
    return query.offset(skip).limit(limit).all()

def get_questions_by_ids(db: Session, ids: List[int]):
    return db.query(Question).filter(Question.id.in_(ids)).all()

def get_topics_by_subject(db: Session):
    # Fetch all subjects and topics
    results = db.query(Question.subject, Question.topic).distinct().all()
    mapping = {}
    for subject, topic in results:
        if subject not in mapping:
            mapping[subject] = []
        if topic not in mapping[subject]:
            mapping[subject].append(topic)
    return mapping

def create_question(db: Session, question: QuestionCreate):
    db_question = Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
