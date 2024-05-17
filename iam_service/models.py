from pydantic import BaseModel
from typing import Dict, List, Optional

class RegisterItem(BaseModel):
    username: str
    password: str
    mail: str
#agregar cómo validar el correo elctrónico

class AuthItem(BaseModel):
    username: str
    password: str

class TokenItem(BaseModel):
    authorization: str

class TraceItem(BaseModel):
    how: str
    what: str
    when: str
    action: str
    details: str


class ResponseItem(BaseModel):
    id_transacction: str
    details: str
    status: str



class LogItem(BaseModel):
    user_id: Optional[str] = None
    action: Optional[str] = None
    details: Dict[str, str] = None


    #register
    #authtntication
    