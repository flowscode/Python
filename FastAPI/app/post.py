from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# REQUEST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# RESPONSE
class Post(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True