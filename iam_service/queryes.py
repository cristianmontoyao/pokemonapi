from config import *

def query_check_if_user_exist(username):
    pipeline = [
    {
        '$match': {
            'username': username
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
    ]
    result = list(iam_collection.aggregate(pipeline))  
    return True if len(result) == 0 else False


def query_set_new_user(register):
    try:
        insert_result = iam_collection.insert_one(register)
        print("ID del documento insertado:", insert_result.inserted_id)
        response = {"details": "user has been created", "code": 200}
        return response
    except Exception as e:
        response = {"details": "internal server error", "code": 500}
        print(e)
        return response


def query_get_stored_password_hash(username):
    pipeline = [
    {
        '$match': {
            'username': username
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
    ]
    result = list(iam_collection.aggregate(pipeline))
    return result[0]
