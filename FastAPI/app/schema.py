from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

# REQUEST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
class UserBase(BaseModel):
    email: EmailStr
    password: str
 
class UserCreate(UserBase):
    pass    

class userlogin(BaseModel):
    email: EmailStr
    password: str
    
# RESPONSE
class Post(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
        
class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserInfo(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None  