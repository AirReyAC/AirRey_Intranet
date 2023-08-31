from pydantic import BaseModel
from typing import Optional


class DataUser(BaseModel):
    Iid: Optional[str]
    username: str
    user_passw: str


class UserSchema(BaseModel):
    Iid: Optional[str]
    name: str
    username: str
    user_passw: str
    # tipo_usuario: str

# class Fotos_Usuarios(BaseModel):
#     Iid: Optional[str]
#     IdNombre = str
#     idFoto_Perfil = str
#     idFoto_Usuario = int
