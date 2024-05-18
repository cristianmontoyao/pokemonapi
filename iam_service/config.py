'''Parametrización de conección a db'''
import os
import urllib.parse
import pymongo

# user DB an conecction
# string
iam_server_name = os.getenv("IAM_SERVER_NAME", "localhost:27017/")
iam_db_name = os.getenv("IAM_DB_NAME", "iam")
iam_collection_name = os.getenv("IAM_COLLECTION_NAME", "userdata")
iam_db_user = os.getenv("IAM_DB_USER", "root")
iam_db_pass = os.getenv("IAM_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")

# necesario escapar el usuario y password para construir la cadena de conexión
escaped_iam_user = urllib.parse.quote_plus(iam_db_user)
escaped_iam_db_pass = urllib.parse.quote_plus(iam_db_pass)

string_iam = f"mongodb://{escaped_iam_user}:{escaped_iam_db_pass}@{iam_server_name}?authSource=admin"

# db connection
client_iam_bd = pymongo.MongoClient(string_iam)
iam_db = client_iam_bd[iam_db_name]
iam_collection = iam_db[iam_collection_name]

# logger DB conecction
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017")
logger_db_name = os.getenv("LOGGER_DB_NAME", "iam")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "iam_logs")
logger_db_user = os.getenv("LOGGER_DB_USER", "root")
logger_db_password = os.getenv("LOGGER_DB_PASSWORD", "")
