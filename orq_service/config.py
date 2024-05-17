import os
import pymongo

# user DB an conecction
# string
pokemon_server_name = os.getenv("POKEMON_SERVER_NAME", "mongodb://localhost:27017/")
pokemon_db_name = os.getenv("POKEMON_DB_NAME", "pokemonWorld")
pokemon_collection_name = os.getenv("POKEMON_COLLECTION_NAME", "pokemondata")
# db connection
client_bd = pymongo.MongoClient(pokemon_server_name)
db = client_bd[pokemon_db_name]
collectionpk = db[pokemon_collection_name]

# logger DB an conecction
# string
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017/")
logger_db_name = os.getenv("LOGGER_DB_NAME", "pokemonWorld")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "pokemon_logs")
