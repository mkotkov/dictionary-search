from pydantic import BaseModel
from typing import List

class Word(BaseModel):
    id: int
    text: str
    definitions: List[str]
    examples: List[str]
    synonyms: List[str]
    antonyms: List[str]
    part_of_speech: str