from ninja import Router
from api.models import User,Post,Thread
from api.models.category import Category
from api.schemas.thread import ThreadSchemaIn, ThreadSchemaOut
from django.shortcuts import get_object_or_404
from typing import List



router = Router(tags=["thread"])

@router.get("/",response= List[ThreadSchemaOut])
def get_threads(request):
    return Thread.objects.all()

@router.get("/{id}",response=ThreadSchemaOut)
def get_thread_by_id(request,id:str):
    return get_object_or_404(Thread,id=id)

@router.post("/",response=ThreadSchemaOut)
def create_thread(request,new_thread:ThreadSchemaIn):
    category = Category.objects.get(id=new_thread.category)
    thread = Thread.objects.create(author = request.user,category = category,title=new_thread.title)
    original_post = Post.objects.create(author = request.user,thread = thread,content= new_thread.content)
    thread.save()
    original_post.save()
    return thread