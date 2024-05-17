from fastapi import FastAPI
from fastapi.responses import JSONResponse

import uuid

from models import *
from functions import *
from queryes import *
from logger import *

app = FastAPI()

@app.post("/auth/v1/registeruser")
def register_new_user(item: RegisterItem):
    item_dict = item.dict()
    log = {
        "user_id": item_dict["username"],
        "action":"register user"
    }
    try:
        result = set_new_register_user(item_dict)
        if result["code"] == 200:
            log["details"] = result["details"]
            logger.info("user has been created", extra=dict(log))
            response = {"code": 201, "details": result["details"]}
            return JSONResponse(content=response, status_code=201)
        if result["code"] == 400:
            log["details"]= result["details"]
            logger.info(result["details"], extra=dict(log))
            response = {"code": 401, "details": result["details"]}
            return JSONResponse(content=response, status_code=401)
    except Exception as e:
        log["details"]= "server internal error"
        logger.info("server internal error", extra=dict(log))  
        response = {"code": 500, "details": "internal server error"}
        return JSONResponse(content=response, status_code=500)


@app.post("/auth/v1/authenticate")
def authenticate_user(item: AuthItem):
    item_dict = item.dict()
    username = item_dict["username"]
    password = item_dict["password"]  
    log = {
        "user_id": item_dict["username"],
        "action":"authenticate user"
    }
    result = authenticating_user(username, password)
    if result["code"] == 200:
        log["details"] = result["details"]
        logger.info("password is correct", extra=dict(log))
        response = {"code": 200, "details": result["details"], "authorization": result["authorization"]}
        return JSONResponse(content=response, status_code=200)
    if result["code"] == 401:
        log["details"] = result["details"]
        logger.info("password wrong", extra=dict(log))
        response = {"code": 400, "details": "user or password as wrong"}
        return JSONResponse(content=response, status_code=400)
    if result["code"] == 400:
        log["details"] = "user does not exist"
        logger.info("user does not exist", extra=dict(log))
        response = {"code": 400, "details": "user or password as wrong"}
        return JSONResponse(content=response, status_code=400)
    log["details"]= "server internal error"
    logger.info("user does not exist", extra=dict(log))
    response = {"code": 500, "details": "servir internal error"}
    return JSONResponse(content=response, status_code=500)

@app.post("/auth/v1/validatetoken")
def validate_token(item: TokenItem):
    item_dict = item.dict()
    token = item_dict["authorization"] 
    result = verify_token_jwt(token)
    print("*"*10)
    print(result)
    print("*"*10)
    log = {
        "action":"validate token"
    }
    if result["code"] == 200:
        log["user_id"] = result["uid"]
        log["details"] = result["details"]
        logger.info("valid token", extra=dict(log))
        response = {"code": 200, "status":True, "details": result["details"]}
        return JSONResponse(content=response, status_code=200)
    if result["code"] == 400:
        log["details"] = result["details"] + " - " + token
        logger.info("password wrong", extra=dict(log))
        response = {"code": 400, "status":False,  "details": result["details"]}
        return JSONResponse(content=response, status_code=400)
    if result["code"] == 401:
        log["details"] = result["details"] + " - " + token
        print(log)
        logger.info("user does not exist", extra=dict(log))
        response = {"code": 401, "status":False,  "details": result["details"]}
        return JSONResponse(content=response, status_code=401)
    log["details"]= "server internal error" + " - " + token
    logger.info("server internal error", extra=dict(log))
    response = {"code": 500,  "status":False, "details": "servir internal error"}
    return JSONResponse(content=response, status_code=500)

