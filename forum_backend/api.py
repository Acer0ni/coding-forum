from ninja import NinjaAPI
api = NinjaAPI(title="the strange place",description="a place for stuff",version="0.1.0")
from api.api import router as api_router
api.add_router("/",api_router)
