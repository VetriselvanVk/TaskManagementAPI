from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(max_length=72)  # type: ignore

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    name: str
    email: EmailStr
