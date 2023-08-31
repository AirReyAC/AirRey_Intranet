from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

files = APIRouter()

templates = Jinja2Templates(directory="view")


@files.get("/files/common")
def common_files(req: Request):
    return templates.TemplateResponse('common.html', {"request": req})

