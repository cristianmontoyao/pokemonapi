'''Parametrización de conección a db'''
import os
import urllib.parse
import pymongo

# user DB an conecction
# string
pok_server_name = os.getenv("POKEMON_SERVER_NAME", "localhost:27017/")
pokemon_db_name = os.getenv("POKEMON_DB_NAME", "pokemonWorld")
pokemon_collection_name = os.getenv("POKEMON_COLLECTION_NAME", "pokemondata")
pokemon_db_user = os.getenv("POKEMON_DB_USER", "root")
pokemon_db_password = os.getenv("POKEMON_DB_PASSWORD", "")

escaped_pok_db_user = urllib.parse.quote_plus(pokemon_db_user)
escaped_pok_db_pass = urllib.parse.quote_plus(pokemon_db_password)

string = f"mongodb://{escaped_pok_db_user}:{escaped_pok_db_pass}@{pok_server_name}?authSource=admin"

# db connection
client_pokemon_bd = pymongo.MongoClient(string)
pokemon_db = client_pokemon_bd[pokemon_db_name]
collectionpk = pokemon_db[pokemon_collection_name]

# logger DB an conecction
# string
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017/")
logger_db_name = os.getenv("LOGGER_DB_NAME", "pokemonWorld")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "pokemon_logs")
logger_db_user = os.getenv("LOGGER_DB_USER", "root")
logger_db_password = os.getenv("LOGGER_DB_PASSWORD", "")
