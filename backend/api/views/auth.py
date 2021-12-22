from typing import List
from django.contrib import auth
from ninja import Router
from api.schemas.auth import LoginSchema
from api.schemas.user import UserSchemaOut,UserSchemaIn
from api.models.user import User
from django.contrib.auth import authenticate,login,logout
from ninja.errors import HttpError
router = Router(tags=["auth"],auth=None)

@router.post("/login",response=UserSchemaOut,auth=None)
def user_login(request,payload:LoginSchema):
    user = authenticate(request, username = payload.username,password = payload.password)
    if user is not None:
        login(request,user)
        return user
    raise HttpError(403,"invalid credentials")

@router.post("/logout")
def user_logout(request):
    logout(request)
    return {"msg":"you have successfully logged out"}

@router.post("/signup",response=UserSchemaOut,auth=None)
def user_signup(request,new_user:UserSchemaIn):
    user = User.objects.create(**new_user.dict())
    user.set_password(new_user.password)
    user.save()
    login(request,user)
    return user