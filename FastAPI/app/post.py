from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True

