'''funciones de entrada endpoints'''
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from functions import *
from queryes import *
from models import *
from logger import *

app = FastAPI(
    title="Pokemon API",
    description="Conoce del mundo pokemon",
    version="1.0.0",
)

@app.post("/pokemons/v1/pokemon/gettypebyname",
          tags=["by name"],
          description="Obtener el tipo de pokemon dado su nombre")
def get_type_by_name(item: Item):
    '''Obtener tipo dado el nombre del pokemon'''
    item_dict = item.dict()
    authorization = item_dict["authorization"]
    authentication_status = authenticate_sesion(authorization)
    log = {
        "user_id": item_dict["authorization"],
        "action":"get type by name"
    }
    if authentication_status["status"]:
        try:
            result = query_get_type_by_name(item_dict["pokemon_name"])
            if result["code"] == 200:
                log["details"] = item_dict["pokemon_name"] + " / pokemon type returned"
                logger.info("pokemon type returned", extra=dict(log))
                return JSONResponse(content=result, status_code=200)
            if result["code"] == 404:
                log["details"] = item_dict["pokemon_name"] + " / pokemon not found"
                logger.info("pokemon not found", extra=dict(log))
                return JSONResponse(content=result, status_code=404)
            if result["code"] == 400:
                log["details"] = item_dict["pokemon_name"] + " / bad request"
                logger.info("bad request", extra=dict(log))
                return JSONResponse(content=result, status_code=400)
        except Exception as e:
            log["details"]: item_dict["pokemon_name"] + "server internal error"
            logger.error("server internal error", extra=dict(log))
            return JSONResponse(content=result, status_code=500)
    log["details"] = "unauthorized"
    logger.info("unauthorized", extra=dict(log))
    return JSONResponse(content="unauthorized", status_code=401)


@app.post("/pokemons/v1/pokemon/getnamebytype", tags=["by type"])
def get_longest_name_by_type(item: TypeItem):
    '''Obtener el nombre de pokemonmás largo basado en el tipo'''
    item_dict = item.dict()
    authorization = item_dict["authorization"]
    authentication_status = authenticate_sesion(authorization)
    print("token capturado del header:")
    print(authorization)
    log = {
            "user_id": item_dict["authorization"],
            "action":"get longest name by type"
        }
    if authentication_status["status"]:
        try:
            result = query_get_longest_name_by_type(item_dict["type_name"])
            if result["code"] == 200:
                log["details"] = item_dict["type_name"] + " / pokemon returned"
                logger.info("pokemon name returned", extra=dict(log))
                return JSONResponse(content=result, status_code=200)
            if result["code"] == 404:
                log["details"] = item_dict["type_name"] + " / pokemon type not found"
                logger.info("type not found", extra=dict(log))
                return JSONResponse(content=result, status_code=404)
            if result["code"] == 400:
                log["details"] = item_dict["type_name"] + " / bad request"
                logger.info("bad request", extra=dict(log))
                return JSONResponse(content=result, status_code=400)
        except Exception as e:
            log["details"]: item_dict["type_name"] + "server internal error"
            logger.error("server internal error", extra=dict(log))
            return JSONResponse(content=result, status_code=500)
    log["details"] = "unauthorized"
    logger.info("unauthorized", extra=dict(log))
    return JSONResponse(content="unauthorized", status_code=401)


@app.post("/pokemons/v1/pokemon/getrandombytype", tags=["by type"])
def get_random_by_type(item: TypeItem):
    '''Obtener un pokemon aleatorio dado su tipo'''
    item_dict = item.dict()
    authorization = item_dict["authorization"]
    authentication_status = authenticate_sesion(authorization)
    log = {
            "user_id": item_dict["authorization"],
            "action":"get random by type"
        }
    if authentication_status["status"]:
        try:
            result = query_get_random_by_type(item_dict["type_name"])  
            if result["code"] == 200:
                log["details"] = item_dict["type_name"] + " / pokemon name returned"
                logger.info("pokemon name returned", extra=dict(log))
                return JSONResponse(content=result, status_code=200)
            if result["code"] == 404:
                log["details"] = item_dict["type_name"] + " / type not found"
                logger.info("type not found", extra=dict(log))
                return JSONResponse(content=result, status_code=404)
            if result["code"] == 400:
                log["details"] = item_dict["type_name"] + " / bad request"
                logger.info("bad request", extra=dict(log))
                return JSONResponse(content=result, status_code=400)
        except Exception as e:
            log["details"]: item_dict["type_name"] + "server internal error"
            logger.error("server internal error", extra=dict(log))
            return JSONResponse(content=result, status_code=500)
    log["details"] = "unauthorized"
    logger.info("unauthorized", extra=dict(log))
    return JSONResponse(content="unauthorized", status_code=401)

@app.post("/pokemons/v1/pokemon/getrandombycityweather", tags=["by type"])
def get_random_by_city_weather(item: GeolocationItem):
    '''Obtener pokemon aleatorio basado en el clima de una ciudad'''
    item_dict = item.dict()
    authorization = item_dict["authorization"]
    authentication_status = authenticate_sesion(authorization)
    log = {
            "user_id": item_dict["authorization"],
            "action":"get random by city weather"
        }
    if authentication_status["status"]:
        try:
            result = get_pokemon_by_city_temp(item_dict["longitude"], item_dict["latitude"])
            print(f"resultado de ocnsulta temperatura: {result}")
            if result["code"] == 200:
                log["details"] = "lon: " + str(item_dict["longitude"]) + "- lat: " + str(item_dict["latitude"]) + " / pokemon name returned"
                logger.info("pokemon name returned", extra=dict(log))
                return JSONResponse(content=result, status_code=200)
            if result["code"] == 404:
                log["details"] = "lon: " + str(item_dict["longitude"]) + "- lat: " + str(item_dict["latitude"]) + " / not found"
                logger.info("type not found", extra=dict(log))
                return JSONResponse(content=result, status_code=404)
            if result["code"] == 400:
                log["details"] = "lon: " + str(item_dict["longitude"]) + "- lat: " + str(item_dict["latitude"]) + " / bad request"
                logger.info("bad request", extra=dict(log))
                return JSONResponse(content=result, status_code=400)
        except Exception as e:
            print(e)
            log["details"]: "lon: " + str(item_dict["longitude"]) + "- lat: " + str(item_dict["latitude"]) + "server internal error"
            logger.error("server internal error", extra=dict(log))
            return JSONResponse(content={"details":"server internal error"}, status_code=500)
    log["details"] = "unauthorized"
    logger.info("unauthorized", extra=dict(log))
    return JSONResponse(content="unauthorized", status_code=401)

@app.post("/pokemons/v1/pokemon/getpokemonlist",tags=["by name"])
def get_pokemon_list(item:EmptyItem):
    '''Obtener la lisra de pokemons'''
    item_dict = item.dict()
    authorization = item_dict["authorization"]
    authentication_status = authenticate_sesion(authorization)
    log = {
            "user_id": item_dict["authorization"],
            "action":"get random by city weather"
        }
    if authentication_status["status"]:
        return query_get_all_pokemon_names()
    log["details"] = "unauthorized"
    logger.info("unauthorized", extra=dict(log))
    return JSONResponse(content="unauthorized", status_code=401)
