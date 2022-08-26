from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import init_db
from controllers import router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def db_load():
    await init_db()


app.include_router(router)
