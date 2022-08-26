from fastapi import APIRouter
from datetime import date
from logic import Analyzer
from schemas import MentionBase, ParserData, MentionBase, StartupBase, StartupResposne
from models import Startup, Mention
from fastapi.responses import JSONResponse, FileResponse
from fastapi.exceptions import HTTPException
from file import write_csv
from typing import List
router = APIRouter()


@router.get("/startups")
async def get_startups(end: date, start: date):
    startups = await Startup.filter(date__lte=end, date__gte=start)
    res = []
    for startup in startups:
        mentions = await Mention.filter(startup_id=startup.id)
        res.append({**dict(startup), "mentions": len(mentions)})
    return res


@router.post("/startups", response_model=List[StartupResposne])
async def get_or_create_startup(data: ParserData):
    ananlyzer = Analyzer(f"""{data.text}""")
    startup_title = ananlyzer.parse()
    if not startup_title:
        raise HTTPException(status_code=404, detail="Startup title not found!")
    startup_obj = await Startup.get_or_create(
        title=startup_title,
        description=data.text,
        country=data.country,
        link=data.link,
        img_link=data.img_link,
        date=data.date,
    )
    status = 201 if startup_obj[1] else 200
    if not startup_obj[1]:
        await Mention.get_or_create(
            title=data.title, link=data.link, date=data.date, startup_id=startup_obj[0].id
        )
    return JSONResponse(
        {"startup_id": startup_obj[0].id, "startup_title": startup_obj[0].title},
        status_code=status,
    )


@router.get("/sartups/file")
async def get_startups_in_file(end: date, start: date):
    await write_csv(end, start)
    return FileResponse('./startups.csv')


@router.post("/mention/force")
async def get_or_create_mention(data: MentionBase):
    await Mention.get_or_create(**data.dict())
    return {"success": True}


@router.post("/startup/force")
async def get_or_create_startup(data: StartupBase):
    await Startup.get_or_create(**data.dict())
    return {"success": True}
