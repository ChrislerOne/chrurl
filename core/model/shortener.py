from sqlalchemy import Column, Integer, CHAR
from core.database.configuration import Base

class URL(Base):
    __tablename__ = "url"
    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(CHAR(255), unique=True, index=True)
    short_url = Column(CHAR(255), unique=True, index=True)
    