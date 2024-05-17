from pydantic import BaseModel

class Item(BaseModel):
    authorization: str
    pokemon_name: str

class TypeItem(BaseModel):
    authorization: str
    type_name: str

class GeolocationItem(BaseModel):
    authorization: str
    latitude: float
    longitude: float

class EmptyItem(BaseModel):
    authorization: str