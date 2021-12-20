from ninja import Router
from api.models.post import Post
from api.models.thread import Thread
from api.models.user import User
from api.schemas.post import PostSchemaIn,PostSchemaOut

router = Router(tags=["posts"])

@router.get("/")
def get_posts(request):
    return Post.objects.all()

@router.get('/{thread_id}',response=PostSchemaOut)
def get_post_by_thread_id(request,id:str):
    return Post.objects.get(thread = id)

@router.post("/",response=PostSchemaOut)
def create_post(request,new_post:PostSchemaIn):
    
    user = User.objects.get(id=new_post.author)
    print(user)
    current_thread = Thread.objects.get(id = new_post.thread)
    post = Post.objects.create(thread = current_thread,author= user,content= new_post.content )
    print(current_thread)
    return post