from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table("users", meta_data,
                         Column("iid", Integer, primary_key=True),
                         Column("name", String(255), nullable=True),
                         Column("username", String(255), nullable=False),
                         Column("user_passw", String(255), nullable=False))
                        #  Column("tipo_usuario", String(255),nullable=False))

# Intranet_Users = Table("Intranet_Users", meta_data,
#                          Column("Iid", Integer, primary_key=True),
#                          Column("IdCompany", String(255), nullable=True),
#                          Column("IdEmployee", String(255), nullable=False),
#                          Column("idJob_Title", String(255), nullable=False),
#                          Column("IdArea", String(255), nullable=False),
#                          Column("IdCity", String(255), nullable=False),
#                          Column("IdInmediate_Boss", String(255), nullable=False),
#                          Column("IdEmail", String(255), nullable=False),
#                          Column("IdTelephone", String(255), nullable=False),
#                          Column("idIntranet_User", String(255), nullable=False),
#                          Column("IdPaswword", String(255), nullable=False),
#                          Column("IdUsuario_Foto", String(255), nullable=False))

# Fotos_Usuarios = Table("Fotos_Usuarios", meta_data,
#                        Column("Iid", Integer, primary_key=True),
#                        Column("IdNombre", String(255), nullable=False),
#                        Column("IdFoto_Perfil", String(255), nullable=False),
#                        Column("IdFoto_Usuario", Integer, Nullable=False),
#                        )

meta_data.create_all(engine)