from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(
    title="the strange place",
    description="a place for stuff",
    version="0.2.0",
    auth=django_auth,
    csrf=True
)

from api.api import router as api_router

api.add_router("/",api_router)

