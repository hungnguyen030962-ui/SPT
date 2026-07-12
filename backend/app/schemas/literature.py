from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional, Any

class LiteratureMaterialBase(BaseModel):
    title: str
    author: Optional[str] = None
    epoch: Optional[str] = None
    genre: Optional[str] = None
    summary: Optional[str] = None
    content_value: Optional[str] = None
    art_value: Optional[str] = None
    outline: Optional[List[Dict[str, str]]] = None
    keywords: Optional[List[str]] = None

class LiteratureMaterialCreate(LiteratureMaterialBase):
    pass

class LiteratureMaterialOut(LiteratureMaterialBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
