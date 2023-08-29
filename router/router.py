from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse 
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.schemas import UserSchema, DataUser
from config.db import engine
from model.users import users
from fastapi.templating import Jinja2Templates
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()

templates = Jinja2Templates(directory="view")

# Pantalla de LOGIN
@user.get("/")
def root(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

@user.get("/home")
def root(req: Request):
    return templates.TemplateResponse("home.html", {"request": req})

@user.get("/profile")
def root(req: Request):
    return templates.TemplateResponse("profile.html", {"request": req})

@user.post("/api/user/login", response_class=HTMLResponse)
def user_login(data_user:DataUser, req: Request):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.username == data_user.username)).first()
        if result != None:
            check_password = check_password_hash(result[4], data_user.user_passw)
            if check_password:
                return templates.TemplateResponse("home.html", {"request": req, "username": data_user.username,"user_passw":data_user.user_passw})


# @user.post("/api/user/login", response_class=HTMLResponse)
# def user_login(data_user:DataUser, req: Request):
#     with engine.connect() as conn:

#         result = conn.execute(users.select().where(users.c.username == data_user.username)).first()

#         if result != None:
#             check_passw = check_password_hash(result[3], data_user.user_passw)
        
#             if check_passw:
                        
#                 return{
#                     "status": 200,
#                     "message": "Acceso Exitoso"    
#                 } 
            
#             return template.TemplateResponse("home.html", {"request": req, "username": data_user.username,"user_passw":data_user.user_passw})

#         return{
#             "status": HTTP_401_UNAUTHORIZED,
#             "message": "Acceso Denegado"
#         }


@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == user_id)).first()
        
        return result


@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return result

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = data_user.dict()
        # print(data_user)
        # print(new_user)
        new_user["user_passw"] = generate_password_hash(data_user.user_passw, "pbkdf2:sha256:30", 30)
        
        conn.execute(users.insert().values(new_user))
                
        return Response(status_code=HTTP_201_CREATED) 

@user.put("/api/user/{userid}")
def update_user(data_update: UserSchema, user_id: str):
    with engine.connect() as conn:
        encrypt_passw= generate_password_hash(data_update.user_passw, "pbkf2:sha256:30", 30)

        conn.execute(users.update().values(name=data_update.name, username=data_update.username, user_passw=encrypt_passw).where(users.c.id == user_id))

        result = conn.execute(users.select().where(users.c.id == user_id) )

        return

@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)

    
@user.get("/logout")
def logout(req : Request):
    return templates.TemplateResponse("index.html", {"request": req})
#   response = RedirectResponse('', status_code= 302)
#   response.delete_cookie(key ='*your access token name*')
#   return response