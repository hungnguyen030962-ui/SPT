from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud import question as crud_question
from app.schemas.question import (
    QuestionOut, QuestionPublic, ExamSubmitRequest, 
    ExamSubmitResponse, QuestionGraded, BatchRequest
)
from typing import List, Dict, Optional, Union, Any

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/", response_model=Union[List[QuestionOut], List[QuestionPublic]])
def read_questions(
    subject: Optional[str] = None,
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
    hide_answers: bool = False,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    questions = crud_question.get_questions(
        db, subject=subject, topic=topic, difficulty=difficulty, search=search, skip=skip, limit=limit
    )
    if hide_answers:
        # Convert to public schemas (hides correct answer and explanation)
        return [QuestionPublic.model_validate(q) for q in questions]
    return [QuestionOut.model_validate(q) for q in questions]

@router.get("/topics")
def read_topics(db: Session = Depends(get_db)):
    return crud_question.get_topics_by_subject(db)

@router.get("/{question_id}", response_model=QuestionOut)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud_question.get_question(db, question_id=question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@router.post("/batch", response_model=List[QuestionOut])
def read_questions_batch(payload: BatchRequest, db: Session = Depends(get_db)):
    return crud_question.get_questions_by_ids(db, ids=payload.ids)

@router.post("/submit", response_model=ExamSubmitResponse)
def submit_exam(payload: ExamSubmitRequest, db: Session = Depends(get_db)):
    answers = payload.answers
    if not answers:
        return ExamSubmitResponse(
            score=0.0,
            total_questions=0,
            correct_answers=0,
            time_spent=payload.time_spent,
            graded_questions=[]
        )

    # Fetch corresponding questions
    question_ids = list(answers.keys())
    db_questions = crud_question.get_questions_by_ids(db, ids=question_ids)
    db_questions_map = {q.id: q for q in db_questions}

    graded_list = []
    correct_count = 0

    for q_id, selected in answers.items():
        q = db_questions_map.get(q_id)
        if not q:
            continue
        
        is_correct = (selected.strip().upper() == q.correct_answer.strip().upper())
        if is_correct:
            correct_count += 1
            
        graded_q = QuestionGraded(
            id=q.id,
            subject=q.subject,
            topic=q.topic,
            difficulty=q.difficulty,
            content=q.content,
            passage=q.passage,
            options=q.options,
            correct_answer=q.correct_answer,
            explanation=q.explanation,
            step_by_step=q.step_by_step,
            formulas=q.formulas,
            selected_answer=selected,
            is_correct=is_correct
        )
        graded_list.append(graded_q)

    total_q = len(graded_list)
    score = round((correct_count / total_q) * 10.0, 2) if total_q > 0 else 0.0

    return ExamSubmitResponse(
        score=score,
        total_questions=total_q,
        correct_answers=correct_count,
        time_spent=payload.time_spent,
        graded_questions=graded_list
    )
