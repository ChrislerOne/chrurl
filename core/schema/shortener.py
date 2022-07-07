from pydantic import BaseModel

class URL(BaseModel):
    origin_url: str
    short_url: str

    class Config:
        orm_mode = True

class ShortUrl(URL):
    short_url: str