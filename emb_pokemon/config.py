'''Parametrización de conección a db'''

import os
import urllib.parse
import pymongo

external_root_url = os.getenv("EXTERNAL_URL", "https://pokeapi.co/api/v2/pokemon")
str_limit = os.getenv("EXTERNAL_LIMIT_STR", "?limit=")
str_offset = os.getenv("EXTERNAL_OFFSET_STR", "&offset=")
limit = os.getenv("EXTERNAL_LIMIT", "20")
offset = os.getenv("EXTERNAL_OFFSET", "0")

external_api_url = external_root_url + str_limit + limit + str_offset + offset

# user DB an conecction
# string
pok_server_name = os.getenv("POKEMON_SERVER_NAME", "localhost:27017/")
pokemon_db_name = os.getenv("POKEMON_DB_NAME", "pokemonWorld")
pokemon_collection_name = os.getenv("POKEMON_COLLECTION_NAME", "pokemondata")
pokemon_db_user = os.getenv("IAM_DB_USER", "root")
pok_db_pass = os.getenv("IAM_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")

escaped_pok_db_user = urllib.parse.quote_plus(pokemon_db_user)
escaped_pok_db_pass = urllib.parse.quote_plus(pok_db_pass)

string = f"mongodb://{escaped_pok_db_user}:{escaped_pok_db_pass}@{pok_server_name}?authSource=admin"

# db connection
client_pokemon_bd = pymongo.MongoClient(string)
pokemon_db = client_pokemon_bd[pokemon_db_name]
pokemon_collection = pokemon_db[pokemon_collection_name]
