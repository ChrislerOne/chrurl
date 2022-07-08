from core.database.crud import *
from core.model.shortener import URL as UrlModel
from core.database.configuration import session
import random
import string


def generate_and_check_shorty():
    shorty = ''.join(random.choice(string.ascii_lowercase +
                     string.digits) for _ in range(6))
    if select_where(session, UrlModel, UrlModel.short_url == shorty):
        return generate_and_check_shorty()
    return shorty

def get_all_urls_from_db():
    return select_all(session, UrlModel)

def shorten_url(origin_url: str):
    check_origin = select_where(
        session, UrlModel, UrlModel.origin_url == origin_url)
    if check_origin:
        return check_origin[0].short_url

    random_shorty = generate_and_check_shorty()

    url_object = UrlModel(origin_url=origin_url, short_url=random_shorty)
    result = insert_one(session, UrlModel, url_object)
    return random_shorty

def get_url_from_shorty(shorty: str):
    query = select_where(session, UrlModel, UrlModel.short_url == shorty)
    return query[0].origin_url 