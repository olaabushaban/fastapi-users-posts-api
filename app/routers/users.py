from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserOut
from database import get_db
from models import User

router = APIRouter()


@router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    email_user = db.query(User).filter(User.email == user.email).first()
    if email_user:
        raise HTTPException(status_code=409, detail=" الايميل مكرر يا حلو ")
    new_user = User(name=user.name, email=user.email)  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="اليوزر مش موجود يابابا")
    return db_user


@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="اليوزر مش موجود يابابا")

    email_user = db.query(User).filter(User.email == user.email, User.id != user_id).first()
    if email_user:
        raise HTTPException(status_code=409, detail="الايميل مكرر يا حلو")

    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
       raise HTTPException(status_code=404, detail="اليوزر مش موجود يابابا")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}