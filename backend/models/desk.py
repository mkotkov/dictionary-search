from pydantic import BaseModel
from typing import List

class Word(BaseModel):
    id: int
    title: str
    cards: List[int]
    description: str