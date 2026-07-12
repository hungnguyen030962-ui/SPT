from pydantic import BaseModel, ConfigDict
from typing import Optional

class EnglishFlashcardBase(BaseModel):
    word: str
    ipa: Optional[str] = None
    meaning: str
    part_of_speech: Optional[str] = None
    example: Optional[str] = None
    topic: Optional[str] = None

class EnglishFlashcardCreate(EnglishFlashcardBase):
    pass

class EnglishFlashcardOut(EnglishFlashcardBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
