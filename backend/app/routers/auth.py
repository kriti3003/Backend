from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.auth import bcrypt_context, create_access_token, Token

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str = "user"

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    # For profile management, we'll create a simple admin user
    from app.models import Profile
    create_user_model = Profile(
        name=f"{create_user_request.first_name} {create_user_request.last_name}",
        email=create_user_request.email,
        description="User created via registration"
    )
    db.add(create_user_model)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    # Simple hardcoded admin login for demo
    if form_data.username == "admin" and form_data.password == "password123":
        token = create_access_token("admin", 1, "admin", timedelta(minutes=60))
        return {'access_token': token, 'token_type': 'bearer'}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid credentials'
    )