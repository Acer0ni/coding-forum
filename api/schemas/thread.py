from typing import Optional
from ninja import ModelSchema
from api.models.thread import Thread

class ThreadSchemaOut(ModelSchema):
    class Config:
        model = Thread
        model_fields = [
            'id',"author","title",'category','original_post'
        ]
class ThreadSchemaIn(ModelSchema):
    class Config:
        model  = Thread
        model_fields = [
            "author","title","category",'original_post'
        ]
