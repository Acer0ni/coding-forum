from typing import List, Optional
from ninja import ModelSchema
from api.models.thread import Thread
from api.schemas.post import PostSchemaOut

class ThreadSchemaOut(ModelSchema):
    posts:List[PostSchemaOut]
    class Config:
        model = Thread
        model_fields = [
            'id',"author","title",'category',
        ]
class ThreadSchemaIn(ModelSchema):
    content:str
    class Config:
        model  = Thread
        model_fields = [
            "title","category",
        ]
