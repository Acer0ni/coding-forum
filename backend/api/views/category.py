from typing import List
from ninja import Router
from api.models.category import Category
from api.schemas.category import CategorySchemaOut


router = Router(tags=["category"])

@router.get("/",response=List[CategorySchemaOut])
def get_categories(request):
    return Category.objects.all()

@router.get('/{category_id}',response=CategorySchemaOut)
def get_category_id(request,category_id:str):
    return Category.objects.get(id = category_id)