from pydantic import BaseModel
from datetime import date, timedelta
from typing import List


class ParserData(BaseModel):
    title: str | None
    text: str
    date: date
    country: str | None
    link: str 
    img_link: str | None

class QueryParameters(BaseModel):
    start_date: date
    end_date: date


class MentionBase(BaseModel):
    title: str
    link: str 
    date: date
    startup_id: int

class StartupBase(BaseModel):
    title: str
    description: str | None
    country : str | None
    link: str | None
    img_link: str | None
    date: date
    