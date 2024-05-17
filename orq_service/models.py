from pydantic import BaseModel

class Item(BaseModel):
    pokemon_name: str

class TypeItem(BaseModel):
    type_name: str

class GeolocationItem(BaseModel):
    latitude: float
    longitude: float

class TraceItem(BaseModel):
    how: str
    what: str
    when: str
    action: str
    details: str