from typing import Optional
from ninja import ModelSchema
from api.models.post import Post

class PostSchemaOut(ModelSchema):
    class Config:
        model = Post
        model_fields = [
            'id','author','thread','created_at','content'
        ]
class PostSchemaIn(ModelSchema):
    class Config:
        model = Post
        model_fields = [
            'thread','content'
        ]