from pydantic import BaseModel
from typing import List

class Card(BaseModel):
    id: int
    front: str
    back: str
    tags: List[str]
    desk_id: int