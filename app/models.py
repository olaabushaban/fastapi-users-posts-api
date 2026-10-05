from database import Base
from sqlalchemy import Integer , String , Column ,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    posts = relationship("Post", back_populates="author" , cascade="all, delete-orphan")

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    author =relationship("User",back_populates="posts")