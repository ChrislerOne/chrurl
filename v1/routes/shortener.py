from fastapi import APIRouter
from core.database.crud import *
from core.database.configuration import session
from core.model.shortener import URL as UrlModel
from core.schema.shortener import URL as UrlSchema, ShortUrl as ShortUrlSchema
from fastapi.responses import RedirectResponse
import random
import string

router = APIRouter()


@router.get("/urls", response_model=list[UrlSchema])
async def test_hello():
    result = select_all(session, UrlModel)
    return result


def generate_and_check_shorty():
    shorty = ''.join(random.choice(string.ascii_lowercase +
                     string.digits) for _ in range(6))
    if select_where(session, UrlModel, UrlModel.short_url == shorty):
        return generate_and_check_shorty()
    return shorty


@router.post("/shorten")
async def shorten_url(origin_url: str):

    check_origin = select_where(
        session, UrlModel, UrlModel.origin_url == origin_url)
    if check_origin:
        return check_origin[0].short_url

    random_shorty = generate_and_check_shorty()

    url_object = UrlModel(origin_url=origin_url, short_url=random_shorty)
    result = insert_one(session, UrlModel, url_object)
    return random_shorty


@router.get("/{shorty}")
async def redirect(shorty):
    query = select_where(session, UrlModel, UrlModel.short_url == shorty)
    return RedirectResponse(url=query[0].origin_url)
