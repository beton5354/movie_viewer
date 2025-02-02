from fastapi import APIRouter

router = APIRouter(prefix="/system")

@router.get('/ping')
async def ping() -> str:
    return 'pong'


@router.get('/1')
async def root():
    return {"message": "Жопа"}