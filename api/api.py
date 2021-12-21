from ninja import Router



router = Router()

from api.views.user import router as user_router
from api.views.post import router as post_router
from api.views.thread import router as thread_router
from api.views.category import router as category_router
from api.views.auth import router as auth_router

router.add_router('user/',user_router)
router.add_router('thread/',thread_router)
router.add_router('post/',post_router)
router.add_router('category/',category_router)
router.add_router('auth/',auth_router)
