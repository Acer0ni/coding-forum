from typing import List,Optional 
from ninja import ModelSchema
from api.models.category import Category
from api.schemas.thread import ThreadSchemaOut


class CategorySchemaOut(ModelSchema):
    threads:Optional[List[ThreadSchemaOut]]
    class Config:
        model = Category
        model_fields = [
            'id',"title",'description'
        ]
class CategorySchemaIn(ModelSchema):
    class Config:
        model  = Category
        model_fields = [
            "title","description",
        ]
