# from django.contrib.auth.models import User
from typing import List, Optional
from ninja import ModelSchema
from api.models import User
from api.models.thread import Thread
from api.schemas.post import PostSchemaOut

class UserSchemaOut(ModelSchema):
    posts:List[PostSchemaOut]
    class Config:
        model = User
        model_fields = [
            "id","username",'first_name','last_name','last_login',"is_superuser",'is_staff',
        ]

class UserSchemaIn(ModelSchema):
    first_name: Optional[str]
    last_name: Optional[str]
    class Config:
        model  = User
        model_fields = [
            "username","password","email"

        ]