from pydantic import BaseModel, EmailStr


class LoginCredentials(BaseModel):
    username: EmailStr
    password: str

