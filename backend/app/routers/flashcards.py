from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud import flashcard as crud_flashcard
from app.schemas.flashcard import EnglishFlashcardOut
from typing import List, Optional

router = APIRouter(prefix="/flashcards", tags=["flashcards"])

@router.get("/", response_model=List[EnglishFlashcardOut])
def read_flashcards(
    topic: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_flashcard.get_flashcards(db, topic=topic, skip=skip, limit=limit)

@router.get("/random", response_model=List[EnglishFlashcardOut])
def read_random_flashcards(
    limit: int = Query(default=10, le=50),
    db: Session = Depends(get_db)
):
    return crud_flashcard.get_random_flashcards(db, limit=limit)
