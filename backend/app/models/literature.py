from sqlalchemy import Column, Integer, String, Text, JSON
from app.core.database import Base

class LiteratureMaterial(Base):
    __tablename__ = "literature_materials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    author = Column(String(100), nullable=True)
    epoch = Column(String(100), nullable=True)
    genre = Column(String(50), nullable=True)
    summary = Column(Text, nullable=True)
    content_value = Column(Text, nullable=True)
    art_value = Column(Text, nullable=True)
    outline = Column(JSON, nullable=True)  # List of objects: {"section": "...", "content": "..."}
    keywords = Column(JSON, nullable=True)  # List of strings
