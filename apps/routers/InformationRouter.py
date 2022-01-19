from fastapi import APIRouter
from main import PARAMS


APPS_INFORMATION = PARAMS.APPS_INFORMATION
router = APIRouter()


@router.get("/")
async def home():
    return APPS_INFORMATION["title"]


@router.get("/ping")
async def ping():
    return APPS_INFORMATION["version"]

@router.get("/rifki1")
async def rifki1():
    result = loan.rifki(input_data=input_data)
    response.status_code = result.status
    return result