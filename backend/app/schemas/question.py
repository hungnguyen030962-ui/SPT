from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional, Any

class QuestionBase(BaseModel):
    subject: str
    topic: str
    difficulty: str
    content: str
    passage: Optional[str] = None
    options: List[str]
    correct_answer: str
    explanation: Optional[str] = None
    step_by_step: Optional[List[Dict[str, str]]] = None
    formulas: Optional[List[str]] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Schema for questions during test (hides answer and explanation)
class QuestionPublic(BaseModel):
    id: int
    subject: str
    topic: str
    difficulty: str
    content: str
    passage: Optional[str] = None
    options: List[str]
    model_config = ConfigDict(from_attributes=True)

class ExamSubmitRequest(BaseModel):
    answers: Dict[int, str]  # {question_id: selected_option}
    time_spent: int          # in seconds

class QuestionGraded(QuestionOut):
    selected_answer: Optional[str] = None
    is_correct: bool

class ExamSubmitResponse(BaseModel):
    score: float
    total_questions: int
    correct_answers: int
    time_spent: int
    graded_questions: List[QuestionGraded]

class BatchRequest(BaseModel):
    ids: List[int]
