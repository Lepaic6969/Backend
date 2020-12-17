from typing import Dict
from pydantic import BaseModel

# Objetos en Pyton, el paréntesis reemplaza al extends de Java
class UserInDB (BaseModel):
    username: str
    password: str
    balance: int

    #Ahora vamos a definir la base de datos ficticia

database_users=Dict[str,UserInDB]
database_users={
"camilo24":UserInDB(**{"username":"camilo24",
                       "password" : "root",
                        "balance":12000  }),
"andres18":UserInDB(**{"username":"andres18",
                        "password":"hola",
                        "balance":34000  }),


                              
                                             
                   }

#Vamos a definir algunas funciones sobre la base de datos ficticia
def get_user(username:str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db:UserInDB):
    database_users[user_in_db]=user_in_db
    return user_in_db