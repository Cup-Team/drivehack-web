from pydantic import BaseModel
from datetime import date, timedelta
from typing import List


class ParserData(BaseModel):
    title: str | None
    text: str
    date: date
    country: str | None

class QueryParameters(BaseModel):
    start_date: date
    end_date: date


class LinkObj(BaseModel):
    link: str
    date: date | None


class MentionBase(BaseModel):
    startup_id: int
    links: List[LinkObj]


class StartupBase(BaseModel):
    id: int
    title: str
    descripiton: str | None
    country : str | None
    link: str | None
    img_link: str | None
    