# schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = Field(default="user")

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"

class UserLogin(BaseModel):
    username_or_email: str
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
