import os
from dotenv import load_dotenv

import pymongo

#global external_api_url

external_root_url = os.getenv("EXTERNAL_URL", "https://pokeapi.co/api/v2/pokemon")
str_limit = os.getenv("EXTERNAL_LIMIT_STR", "?limit=")
str_offset = os.getenv("EXTERNAL_OFFSET_STR", "&offset=")
limit = os.getenv("EXTERNAL_LIMIT", "20")
offset = os.getenv("EXTERNAL_OFFSET", "0")



external_api_url = external_root_url + str_limit + limit + str_offset + offset

# user DB an conecction
# string
pokemon_server_name = os.getenv("POKEMON_SERVER_NAME", "mongodb://localhost:27017/")
pokemon_db_name = os.getenv("POKEMON_DB_NAME", "pokemonWorld")
pokemon_collection_name = os.getenv("POKEMON_COLLECTION_NAME", "pokemondata")
# db connection
client_pokemon_bd = pymongo.MongoClient(pokemon_server_name)
pokemon_db = client_pokemon_bd[pokemon_db_name]
pokemon_collection = pokemon_db[pokemon_collection_name]
