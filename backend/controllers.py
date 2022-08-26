from fastapi import APIRouter
from datetime import date
from logic import Analyzer
from schemas import MentionBase, ParserData, MentionBase, StartupBase
from models import Startup, Mention
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
router = APIRouter()


@router.post("/startup")
async def get_or_create_startup(data: ParserData):
    ananlyzer = Analyzer(f"""{data.text}""")
    startup_title = ananlyzer.parse()
    if not startup_title:
        raise HTTPException(status_code=404, detail='Startup title not found!')
    startup_obj = await Startup.get_or_create(
        title=startup_title, description=data.text, country=data.country
    )
    status = 201 if startup_obj[1] else 200
    return JSONResponse({"startup_id": startup_obj[0].id, "startup_title": startup_obj[0].title}, status_code=status)


@router.post("/mentions")
async def get_or_create_mentions(data: MentionBase):
    for mention in data.links:
        await Mention.get_or_create(
            link=mention.link, date=mention.date, startup_id=data.startup_id
        )
    return {"success": True}


@router.post("/mention/force")
async def get_or_create_mention(data: MentionBase):
    await Mention.get_or_create(**data)
    return {"success": True}


@router.post("/startup/force")
async def get_or_create_startup(data: StartupBase):
    await Startup.get_or_create(**data.dict())
    return {"success": True}