from fastapi import APIRouter


from core.model.shortener import URL as UrlModel
from core.schema.shortener import URL as UrlSchema, ShortUrl as ShortUrlSchema
from fastapi.responses import RedirectResponse

from v1.services.shortener import get_all_urls_from_db, get_url_from_shorty, shorten_url


router = APIRouter()


@router.get("/urls", response_model=list[UrlSchema])
async def get_all_urls():
    return get_all_urls_from_db()


@router.post("/shorten")
async def short_url(origin_url: str):
    return str(shorten_url(origin_url))


@router.get("/{shorty}")
async def redirect(shorty):
    return RedirectResponse(url=get_url_from_shorty(shorty))
