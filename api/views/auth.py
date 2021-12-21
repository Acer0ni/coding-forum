from typing import List
from ninja import Router
from api.schemas.auth import LoginSchema
from api.schemas.user import UserSchemaOut
from django.contrib.auth import authenticate,login,logout
router = Router(tags=["auth"],auth=None)

@router.post("/login",response=UserSchemaOut,auth=None)
def user_login(request,payload:LoginSchema):
    user = authenticate(request, username = payload.username,password = payload.password)
    if user is not None:
        login(request,user)
        return user

@router.get("/logout")
def user_logout(request):
    logout(request)
    return {"msg":"you have successfully logged out"}