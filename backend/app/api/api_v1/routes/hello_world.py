from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_hello_world():
    return {"message": "Hello world!"}
