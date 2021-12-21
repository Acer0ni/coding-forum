from typing import Optional
from ninja import Schema
from api.models.user import User


class LoginSchema(Schema):
    email:str
    password:str
        