from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
# when user add in the form like sign up the user does not know the id which must will put to him
# كل schema بنحدد شكله حسب "مين بيبعث الداتا" و"مين بيستقبلها"، مش نفس الشكل دايماً 

class UserOut(BaseModel):
    id:int
    email:str
    name:str

class PostCreate(BaseModel):
    title:str
    content:str
class PostOut(BaseModel):
    id:int
    title:str
    content:str
    user_id:int