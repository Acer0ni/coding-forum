from ninja import Router
from models.category import Category
from schemas.category import CategorySchemaOut


router = Router(tags=["category"])

@router.get("/")
def get_categories(request):
    return Category.objects.all()

@router.get('/{category_id}',response=CategorySchemaOut)
def get_category_id(request,id:str):
    return Category.objects.get(thread = id)