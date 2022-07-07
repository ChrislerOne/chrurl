from fastapi import APIRouter
from core.database.crud import *
from core.database.configuration import session
from core.model.shortener import URL as UrlModel
from core.schema.shortener import URL as UrlSchema,ShortUrl as ShortUrlSchema
router = APIRouter()


@router.get("/urls", response_model=list[UrlSchema])
async def test_hello():
    result = select_all(session, UrlModel)
    return result

@router.post("/shorten", response_model=ShortUrlSchema)
async def shorten_url():
    pass