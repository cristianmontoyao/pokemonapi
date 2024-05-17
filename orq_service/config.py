import os
import pymongo
import urllib.parse

# user DB an conecction
# string
pokemon_server_name = os.getenv("POKEMON_SERVER_NAME", "localhost:27017/")
pokemon_db_name = os.getenv("POKEMON_DB_NAME", "pokemonWorld")
pokemon_collection_name = os.getenv("POKEMON_COLLECTION_NAME", "pokemondata")
pokemon_db_user = os.getenv("IAM_DB_USER", "root")
pokemon_db_password = os.getenv("IAM_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")

escaped_pokemon_db_user = urllib.parse.quote_plus(pokemon_db_user)
escaped_pokemon_db_password = urllib.parse.quote_plus(pokemon_db_password)

string_pokemon = f"mongodb://{escaped_pokemon_db_user}:{escaped_pokemon_db_password}@{pokemon_server_name}?authSource=admin"

# db connection
client_pokemon_bd = pymongo.MongoClient(string_pokemon)
pokemon_db = client_pokemon_bd[pokemon_db_name]
collectionpk = pokemon_db[pokemon_collection_name]

# logger DB an conecction
# string
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017/")
logger_db_name = os.getenv("LOGGER_DB_NAME", "pokemonWorld")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "pokemon_logs")
logger_db_user = os.getenv("LOGGER_DB_USER", "root")
logger_db_password = os.getenv("LOGGER_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")
