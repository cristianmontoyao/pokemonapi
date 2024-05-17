import logging
import pymongo
from pymongo import MongoClient
import datetime

from config import *


class MongoHandler(logging.Handler):
    def __init__(self, db_uri, db_name, collection_name, username, password):
        logging.Handler.__init__(self)
        self.client = MongoClient(db_uri, username=username, password=password)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def emit(self, record):
        log_entry = self.format(record)
        log_doc = {
            "created": datetime.datetime.fromtimestamp(record.created),
            "level": record.levelname,
            "user_id": getattr(record, 'user_id', None),
            "action": getattr(record, 'action', None),
            "details": getattr(record, 'details', None)
            #"message": log_entry
        }
        self.collection.insert_one(log_doc)

def get_mongo_logger(db_uri, db_name, collection_name, username, password):
    logger = logging.getLogger("iam_Logger")
    logger.setLevel(logging.DEBUG)  # O ajusta al nivel que necesites

    mongo_handler = MongoHandler(db_uri, db_name, collection_name, username, password)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    mongo_handler.setFormatter(formatter)

    logger.addHandler(mongo_handler)
    return logger

'''
logger_server_name = os.getenv("LOGGER_SERVER_NAME", "localhost:27017/")
logger_db_name = os.getenv("LOGGER_DB_NAME", "iam")
logger_collection_name = os.getenv("LOGGER_COLLECTION_NAME", "iam_logs")
logger_db_user = os.getenv("LOGGER_DB_USER", "")
logger_db_password = os.getenv("LOGGER_DB_PASSWORD", "")

logger_server_name = "mongodb://localhost:27017"

# Configuración de conexión a MongoDB
db_uri = logger_server_name
db_name = logger_db_name
collection_name = logger_collection_name
username = logger_db_user
password = logger_db_password
'''
# Obtener el logger
logger = get_mongo_logger(logger_server_name, logger_db_name, logger_collection_name, logger_db_user, logger_db_password)


#



'''
# Crear un manejador de logging para MongoDB
class MongoDBHandler(logging.Handler):
    def __init__(self, db_name, collection_name, uri=logger_server_name):
        super().__init__()
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def emit(self, record):
        log_entry = self.format(record)
        log_doc = {
            "created": datetime.datetime.fromtimestamp(record.created),
            "level": record.levelname,
            "user_id": getattr(record, 'user_id', None),
            "action": getattr(record, 'action', None),
            "details": getattr(record, 'details', None)
            #"message": log_entry
        }
        self.collection.insert_one(log_doc)

# Configuración del logger
logger = logging.getLogger('iam_pokemon_logger')
logger.setLevel(logging.INFO)  # Configurar el nivel mínimo de log

mongo_uri = f"mongodb://{logger_db_user}:{logger_db_password}@{logger_server_name}/{logger_db_name}?authSource=admin"

# Crear manejador para MongoDB
#mongo_handler = MongoDBHandler(db_name='logs_db', collection_name='logs')
mongo_handler = MongoDBHandler(mongo_uri, logger_db_name, logger_collection_name, logger_db_user2, logger_db_password2)
#mongo_handler = MongoDBHandler(db_name=logger_db_name, collection_name=logger_collection_name, uri=mongo_uri)
mongo_handler.setLevel(logging.DEBUG)

# Crear un formato y añadirlo a los manejadores
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s - user_id=%(user_id)s - action=%(action)s - details=%(details)s')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - user_id=%(user_id)s - action=%(action)s - details=%(details)s')
#mongo_handler.setFormatter(formatter)

# Añadir los manejadores al logger
logger.addHandler(mongo_handler)

'''