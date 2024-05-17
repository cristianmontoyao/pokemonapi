import os
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weathers/v1/weather/getweatherbycoordinate")
def get_weather_by_coordinate_by_get(latitude:float,longitude:float):
    ext_url = os.getenv("EXTERNAL_URL", "https://api.open-meteo.com/v1/forecast")
    ext_url1 = os.getenv("EXTERNAL_URL1", "?latitude=")
    ext_url2 = os.getenv("EXTERNAL_URL2", "&longitude=")
    ext_url3 = os.getenv("EXTERNAL_URL3", "&current_weather=true")  
    weather_api_url = ext_url + ext_url1 + str(latitude) + ext_url2 + str(longitude) + ext_url3
    #weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude="+str(latitude)+"&longitude="+str(longitude)+"&current_weather=true"
    response = {}
    response["latitude"] = latitude
    response["longitude"] = longitude
    try:
        weather_response = requests.get(weather_api_url)
        city_data = weather_response.json()
        temperature = city_data['current_weather']['temperature']
        response["code"] = 200    
        response["temperature"] = temperature
        print(response)
        return response
    except Exception as e:
        response["code"] = 500
        response["temperature"] = "server internal error"

