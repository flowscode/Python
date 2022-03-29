# imports
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..schema import User, UserCreate, UserInfo
from .. import models, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

####################### CREATE A NEW USER
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    # hash the password - user.password
    hash_pwd = utils.hash(user.password)
    user.password = hash_pwd
    
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

################## Get User
@router.get("/{id}", response_model=UserInfo)
def get_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id).first()
    if not user_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id: {id} was not found")
    return user_query    