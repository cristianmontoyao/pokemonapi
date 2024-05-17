import logging
import pymongo
from pymongo import MongoClient
import datetime

from config import *

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

# Crear manejador para MongoDB
#mongo_handler = MongoDBHandler(db_name='logs_db', collection_name='logs')
mongo_handler = MongoDBHandler(db_name=logger_db_name, collection_name=logger_collection_name)
mongo_handler.setLevel(logging.DEBUG)

# Crear un formato y añadirlo a los manejadores
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s - user_id=%(user_id)s - action=%(action)s - details=%(details)s')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - user_id=%(user_id)s - action=%(action)s - details=%(details)s')
#mongo_handler.setFormatter(formatter)

# Añadir los manejadores al logger
logger.addHandler(mongo_handler)