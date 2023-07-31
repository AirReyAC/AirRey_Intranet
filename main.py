from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/")
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signup")
def signup(req: Request):
    return template.TemplateResponse("components/signup.html", {"request": req})

@app.get("/user")
def user(req: Request):
    return template.TemplateResponse("components/user.html", {"request": req})