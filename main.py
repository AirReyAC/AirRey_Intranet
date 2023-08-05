from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router.router import user


app= FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(user)