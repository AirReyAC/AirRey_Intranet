from fastapi import FastAPI, Request, Response
from fastapi.resposes import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

@app.get("/")
def root():
    return "Hola, Soy el servidor de AirRey"