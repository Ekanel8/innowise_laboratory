from typing import Optional
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookResponse(BaseModel):
    id:      int
    title:   str
    author:  str
    year: Optional[int] = None

class Config:
    orm_mode = True