from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
