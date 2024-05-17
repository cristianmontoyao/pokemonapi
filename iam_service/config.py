import os
from dotenv import load_dotenv

import pymongo
import urllib.parse

global secret_key 
secret_key = os.getenv("SECRET_KEY", "")

# user DB an conecction
# string
iam_server_name = os.getenv("IAM_SERVER_NAME", "localhost:27017/")
iam_db_name = os.getenv("IAM_DB_NAME", "iam")
iam_collection_name = os.getenv("IAM_COLLECTION_NAME", "userdata")
iam_db_user = os.getenv("IAM_DB_USER", "root")
iam_db_password = os.getenv("IAM_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")

escaped_iam_db_user = urllib.parse.quote_plus(iam_db_user)
escaped_iam_db_password = urllib.parse.quote_plus(iam_db_password)

string_connection_iam = f"mongodb://{escaped_iam_db_user}:{escaped_iam_db_password}@{iam_server_name}?authSource=admin"

# db connection
client_iam_bd = pymongo.MongoClient(string_connection_iam)
iam_db = client_iam_bd[iam_db_name]
iam_collection = iam_db[iam_collection_name]

# logger DB an conecction
# string
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "mongodb://localhost:27017")
logger_db_name = os.getenv("LOGGER_DB_NAME", "iam")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "iam_logs")
logger_db_user = os.getenv("LOGGER_DB_USER", "root")
logger_db_password = os.getenv("LOGGER_DB_PASSWORD", "W9KTR@H5UvIxgklVWJH1_JuYw9XIuAIpBg-lPgs88oPaVwImz3B7G")

#logger_db_user2 = urllib.parse.quote_plus(logger_db_user)
#logger_db_password2 = urllib.parse.quote_plus(logger_db_password)


# db connection
#client_logger_bd = pymongo.MongoClient(logger_server_name)
#logger_db = client_logger_bd[logger_db_name]
#logger_collection = logger_db[logger_collection_name]
