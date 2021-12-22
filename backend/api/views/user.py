from ninja import Router
from api.models import User
from api.schemas.user import UserSchemaIn, UserSchemaOut
from django.shortcuts import get_object_or_404
from typing import List
from django.http import Http404
router = Router(tags=["user"])

@router.get("/",response=List[UserSchemaOut])
def get_users(request):
    return User.objects.all()

@router.get("/me",response=UserSchemaOut)
def get_current_user(request):
    return request.user
    
@router.get("/{id}",response=UserSchemaOut)
def get_user_by_id(request,id:str):
    return get_object_or_404(User,id=id)
    # try:
    #     u = User.objects.prefetch_related("posts").get(id=id)
    #     u.user_posts = u.posts.all()
    # except User.DoesNotExist:
    #     raise Http404(f"no user exists for id {id}")

    # return u



@router.put("/{id}",response=UserSchemaOut)
def update_user(request,id:str,user:UserSchemaIn):
    updated_user = get_object_or_404(User,id=id)
    for attr, value in user.dict().items():
        setattr(updated_user,attr,value)
    updated_user.save()
    return updated_user

