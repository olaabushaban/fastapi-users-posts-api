from pydantic import BaseModel ,EmailStr , Field ,ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

# ده إعداد بيشيل المسافات من أول وآخر أي نص قبل التحقق. من غيره، الاسم " " (3 مسافات) كان هيعدّي من min_length=2 لأنه بيحسب المسافات كحروف. بالإعداد ده بيتحول لنص فاضي وبيترفض.

    name:str = Field(min_length=2, max_length=50)
    email:EmailStr
# when user add in the form like sign up the user does not know the id which must will put to him
# كل schema بنحدد شكله حسب "مين بيبعث الداتا" و"مين بيستقبلها"، مش نفس الشكل دايماً 

class UserOut(BaseModel):
    id:int
    email:EmailStr
    name:str

class PostCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title:str = Field(min_length=3,max_length=100)
    content:str = Field(min_length=1,max_length=5000)
class PostOut(BaseModel):
    id:int
    title:str
    content:str
    user_id:int