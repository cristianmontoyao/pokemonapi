import os
from dotenv import load_dotenv

import pymongo

global secret_key 
secret_key = os.getenv("SECRET_KEY", "")

# user DB an conecction
# string
iam_server_name = os.getenv("IAM_SERVER_NAME", "mongodb://localhost:27017/")
iam_db_name = os.getenv("IAM_DB_NAME", "iam")
iam_collection_name = os.getenv("IAM_COLLECTION_NAME", "userdata")
# db connection
client_iam_bd = pymongo.MongoClient(iam_server_name)
iam_db = client_iam_bd[iam_db_name]
iam_collection = iam_db[iam_collection_name]

# logger DB an conecction
# string
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017/")
logger_db_name = os.getenv("LOGGER_DB_NAME", "iam")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "iam_logs")
# db connection
client_logger_bd = pymongo.MongoClient(logger_server_name)
logger_db = client_logger_bd[logger_db_name]
logger_collection = logger_db[logger_collection_name]
