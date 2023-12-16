from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token

from schemas.UserSchema import UserSchema

auth_router = APIRouter()

@auth_router.post("/login",tags=['auth'],response_model=dict,status_code=200)
def login(user:UserSchema):
    if user.email == "admin@gmail.com" and user.password =="password":
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token":token},status_code=200)
    else:
        result = JSONResponse(content={"message":"invalid credentials"},status_code=401)
    return result