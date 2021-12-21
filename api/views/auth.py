from typing import List
from ninja import Router
router = Router(tags=["auth"])

@router.get("/login")
def login(request,):
    pass



@router.get("/logout")
def logout(request,):
    pass