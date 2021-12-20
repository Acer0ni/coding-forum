from ninja import Router

router = Router()

@router.get("/")
def hello(request):
    return "Hello post"