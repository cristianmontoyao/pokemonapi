import os
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import uuid
import jwt
import datetime

from fastapi.responses import JSONResponse

from models import *
from queryes import *
from logger import *

global secret_key 
secret_key = os.getenv("SECRET_KEY", "")

def check_password_conditions(password):
    #verificar longitud
    #verificar letras
    #verificar numeros
    #verificar símbolos
    #verificar caracter especial
    pass


def set_new_register_user(user_data):
    try:
        if query_check_if_user_exist(user_data["username"]):
            user_data["uid"] = str(uuid.uuid4())
            user_data["hash"] = generate_password_hash(user_data["password"])
            del user_data["password"]
            result = query_set_new_user(user_data)
            if result["code"] == 200:
                response = {"details": result["details"], "code": 200}
                return response
            if result["code"] == 500:
                return result
        response = {"details": "user already exists", "code": 400}
        return response
    except Exception as e:
        response = {"details": "internal server error", "code": 500}
        return response    

def generate_password_hash(password):
    ph = PasswordHasher()
    pass_hash = ph.hash(password)
    return pass_hash


def generate_token_jwt(payload):
    # Define la clave secreta para firmar el token (asegúrate de mantener esto seguro)
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def verify_token_jwt(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        print("Token válido. Payload:", payload)
        response = {"code": 200, "status":True, "uid": payload["uid"], "details": "successful authentication"}
        return response
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        response = {"code": 400, "status":False, "details": "expired token"}
        return response
    except jwt.InvalidTokenError:
        print("Token inválido")
        response = {"code": 401, "status":False, "details": "invalid token"}
        return response

def authenticating_user(username, password):
    ph = PasswordHasher()
    try:
        stored_data = query_get_stored_password_hash(username)
        stored_hash = stored_data["hash"]
        try:
            ph.verify(stored_hash, password)          
            token = generate_token_jwt({"uid":stored_data["uid"]})         
            response = {"code": 200, "details": "successful authentication", "authorization": token}
            return response
        except VerifyMismatchError:
            response = {"details": "failed authentication", "code": 401}
            return response
    except:
        response = {"details": "bad request", "code": 400}
        return response    

