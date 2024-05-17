import os
from dotenv import load_dotenv
import requests
from config import *
from queryes import *


load_dotenv()


def get_temperature_by_city(longitude, latitude):
    url = os.getenv("WEATHER_INTERNAL_URL", "http://localhost:8003")
    url1 = os.getenv("WEATHER_INTERNAL_URL1", "/weathers/v1/weather/getweatherbycoordinate")
    url2 = os.getenv("WEATHER_INTERNAL_URL2", "?latitude=")
    url3 = os.getenv("WEATHER_INTERNAL_URL3", "&longitude=") 
    weather_internal_url = url + url1 + url2 + str(latitude) + url3 + str(longitude)
    print(weather_internal_url)
    try:
        weather_response = requests.get(weather_internal_url)
        city_data = weather_response.json()
        if city_data["code"] == 200:
            temperature = city_data["temperature"]
            return {"code": 200, "temperature": temperature}
        return {"code": 500, "temperature": temperature}
    except Exception as e:
        print("por el error")
        print(e)
        return {"code": 500, "details": "not available"}


def get_equivalent_type_by_temp(temperature):
    print("TRANSFORMANDO TEMPERATURA A TIPO")
    equivalent_temp_table = {
        'fuego': {'name': 'fire', 'lower_limit': 30, 'upper_limit': 60},
        'tierra': {'name': 'poison', 'lower_limit': 20, 'upper_limit': 30},
        'normal': {'name': 'normal', 'lower_limit': 10, 'upper_limit': 20},
        'agua': {'name': 'water', 'lower_limit': 0, 'upper_limit': 10},
        'hielo': {'name': 'ice', 'lower_limit': -80, 'upper_limit': 0}
    }

    for _key, limits in equivalent_temp_table.items():
        if limits['lower_limit'] <= temperature < limits['upper_limit']:
            type_name = limits['name']
    return type_name


def get_pokemon_by_city_temp(longitude, latitude):
    city_temperature = get_temperature_by_city(longitude, latitude)
    if city_temperature["temperature"]:
        pokemon_type = get_equivalent_type_by_temp(city_temperature["temperature"])
        print(pokemon_type)
        details = {}
        details["latitude"] = longitude
        details["longitude"] = latitude
        details["city_temperature"] = city_temperature['temperature']
        details["pokemon_type"] = pokemon_type
        try:
            print("por aquix")
            result = query_get_random_by_city_weather(pokemon_type)
            result["details"] = details
            return result
        except Exception as e:
            result["code"] = 500
            print("por aqui")
            return result
    else:
        return {"code": 500, "details": "internal server error"}

def authenticate_sesion(authorization_token):
    url = "http://127.0.0.1:8001/auth/v1/validatetoken"
    data = {"authorization": authorization_token}
    response = requests.post(url, json=data)
    result = response.json()

    if result["status"]:
        return result
        #logger
    else:
        return result
        #logger

