'''Parametrización de looger asociado a BD Mongo'''

import logging
import datetime
from pymongo import MongoClient

from config import *

class MongoHandler(logging.Handler):
    '''Manejador de la conexión del logger hacia mongo'''
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
    '''Definición del logger'''
    logger = logging.getLogger("iam_Logger")
    logger.setLevel(logging.DEBUG)  # O ajusta al nivel que necesites

    mongo_handler = MongoHandler(db_uri, db_name, collection_name, username, password)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    mongo_handler.setFormatter(formatter)

    logger.addHandler(mongo_handler)
    return logger

# Obtener el logger
logger = get_mongo_logger(logger_server_name, logger_db_name, logger_collection_name, logger_db_user, logger_db_password)