from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_ola_mundo():
    return {"message": "olá mundo"}