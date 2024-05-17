import random
from config import *

def query_get_type_by_name(pokemon_name):
    pokemon_data ={}
    pipeline = [
    {
        '$match': {
            'name': pokemon_name
        }
    }, {
        '$project': {
            '_id':0,
            'name': 1, 
            'types': 1
        }
    }
    ]
    try:
        result = list(collectionpk.aggregate(pipeline))
        #la consulta devuelve una lista por cada registro encontrado
        data = result[0]
        pokemon_data["code"] = 200
        pokemon_data["name"] = data['name']
        pokemon_data["types"] = [type_data['type']['name'] for type_data in data['types']]
        return pokemon_data
    except Exception as e:
        pokemon_data["code"] = 404
        pokemon_data["details"] = "not found"
        return pokemon_data


def query_get_longest_name_by_type(type_name):
    pokemon_data ={}
    pipeline = [
    {
        '$match': {
            'types.type.name': type_name
        }
    }, {
        '$addFields': {
            'length': {
                '$strLenCP': '$name'
            }
        }
    }, {
        '$sort': {
            'length': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'types.type.name': 1
        }
    }
    ]
    
    try:
        result = list(collectionpk.aggregate(pipeline))
        data = result[0]
        pokemon_data["code"] = 200
        pokemon_data["name"] = data['name']
        pokemon_data["types"] = [type_data['type']['name'] for type_data in data['types']]
        return pokemon_data
    except Exception as e:
        pokemon_data["code"] = 404
        pokemon_data["details"] = "not found"
        return pokemon_data    

def query_get_random_by_type(type_name):
    pokemon_data ={}
    pipeline = [
    {
        '$match': {
            'types.type.name': type_name
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'types.type.name': 1
        }
    }
    ]
    try:
        result = list(collectionpk.aggregate(pipeline))
        random_number = random.randint(0, len(result)-1)
        data = result[random_number]
        pokemon_data["code"] = 200
        pokemon_data["name"] = data['name']
        pokemon_data["types"] = [type_data['type']['name'] for type_data in data['types']]
        return pokemon_data
    except Exception as e:
        pokemon_data["code"] = 404
        pokemon_data["details"] = "not found"
        return pokemon_data 



def query_get_random_by_city_weather(type_name):
    pokemon_data ={}
    pipeline = [
    {
        '$match': {
            'types.type.name': type_name
        }
    }, {
        '$match': {
            'name': {
                '$regex': '[iam/i]'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'types.type.name': 1
        }
    }
    ]
    try:
        print("aqui")
        result = list(collectionpk.aggregate(pipeline))
        random_number = random.randint(0, len(result)-1)
        #devuelve una lista de diccionarios por cada pokemon de ese tipo
        data = result[random_number]
        pokemon_data["code"] = 200
        pokemon_data["name"] = data['name']
        pokemon_data["types"] = [type_data['type']['name'] for type_data in data['types']]
        return pokemon_data
    except Exception as e:
        print("aquij")
        pokemon_data["code"] = 404
        pokemon_data["details"] = "not found"
        return pokemon_data 



def query_get_all_pokemon_names():
    pipeline = [
    {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'types': 1
        }
    }, {
        '$addFields': {
            'name': '$name', 
            'type': '$types.type.name'
        }
    }, {
        '$project': {
            'name': 1, 
            'type': 1
        }
    }
    ]
    pokemon_list = list(collectionpk.aggregate(pipeline))
    result = {}
    for pokemon in pokemon_list:
        result[pokemon["name"]] = pokemon["type"]
    
    all_types = [value for value_list in result.values() for value in value_list]

    # Obtener los valores únicos utilizando un conjunto
    unique_values = set(all_types)
    result["differents_types"] = unique_values
    # Imprimir los valores únicos
    return result
