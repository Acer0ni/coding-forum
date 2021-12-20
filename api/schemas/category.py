from typing import List 
from ninja import ModelSchema
from api.models.category import Category
from api.schemas.thread import ThreadSchemaOut


class CategorySchemaOut(ModelSchema):
    threads:List[ThreadSchemaOut]
    class Config:
        model = Category
        model_fields = [
            'id',"title",'description','threads'
        ]
class ThreadSchemaIn(ModelSchema):
    class Config:
        model  = Category
        model_fields = [
            "title","description",
        ]
