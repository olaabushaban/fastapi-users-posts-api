from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PostCreate, PostOut
from database import get_db
from models import Post

router = APIRouter()

@router.post("/users/{user_id}/posts/", response_model=PostOut)
def create_post(user_id: int, post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(title=post.title, content=post.content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/posts/", response_model=list[PostOut])
def read_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.put("/posts/{post_id}", response_model=PostOut)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}