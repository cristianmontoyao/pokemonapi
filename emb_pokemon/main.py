import requests
import pymongo
#import schedule
import time

from config import *

# Obtener el listado de pokemons disponibles
def get_pokemon_list():
    response = requests.get(external_api_url)
    data = response.json()
    pokemons = data['results']
    urls = []
    for item in pokemons:
        urls.append(item['url'])
    return urls

# get pokemon information details
def get_pokemon_details(api_url_pokemon):
    response_pokemon = requests.get(api_url_pokemon)
    data_pokemon = response_pokemon.json()
    return data_pokemon

# set information to DB by pokemon
def put_pokemon_bd(pokemon_info):
    insert_result = pokemon_collection.insert_one(pokemon_info)
    #print("document id:", insert_result.inserted_id)
    return {"code":200}

# Query a la BD para confirmar que no esté vacía
def check_bd_status():
    count = pokemon_collection.count_documents({})

    # Verificar si la colección está vacía
    if count == 0:
        urls = get_pokemon_list()
        for url in urls:
            pokemon_details = get_pokemon_details(url)
            put_pokemon_bd(pokemon_details)

def update_database():
    get_pokemon_list()

update_database()

# schedule loop task
while True:
    print("checking db status")
    db_check_time = os.getenv("DATABASE_CHECK_SECONDS_TIME", "10")
    #schedule.run_pending()
    check_bd_status()
    time.sleep(int(db_check_time))  # Esperar 1 segundo antes de revisar si hay tareas programadas