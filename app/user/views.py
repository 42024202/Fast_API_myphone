from fastapi import APIRouter
from schemas import CreateUser

router = APIRouter(prefix="/user")

@router.post("/create/")
def create_user(user:CreateUser):
    return {
        "massage": "User created",
        "email": user.email
        }


