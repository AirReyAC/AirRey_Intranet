from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import photos, router, files



app= FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/common", StaticFiles(directory="common"), name="common")


app.include_router(router.user)
app.include_router(files.files)
# app.include_router(photos.router)