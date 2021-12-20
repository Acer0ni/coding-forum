from ninja import Router
from api.models import User
from api.schemas.user import UserSchemaIn, UserSchemaOut
from django.shortcuts import get_object_or_404
from typing import List
router = Router(tags=["user"])

@router.get("/",response=List[UserSchemaOut])
def get_users(request):
    return User.objects.all()

@router.get("/{id}",response=UserSchemaOut)
def get_user_by_id(request,id:str):
    return get_object_or_404(User,id=id)

@router.post("/",response=UserSchemaOut)
def create_user(request,new_user:UserSchemaIn):
    user = User.objects.create(**new_user.dict())
    user.set_password(new_user.password)
    user.save()
    return user

@router.put("/{id}",response=UserSchemaOut)
def update_user(request,id:str,user:UserSchemaIn):
    updated_user = get_object_or_404(User,id=id)
    for attr, value in user.dict().items():
        setattr(updated_user,attr,value)
    updated_user.save()
    return updated_user

