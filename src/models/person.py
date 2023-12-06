from pydantic import BaseModel, conint, TypeAdapter
from typing import List, Union
from enum import Enum

from src.models.house import House
from src.models.car import Car


class Relationship(Enum):
    SINGLE = "single"
    MARRIED = "married"


class PersonalData(BaseModel):
    name: str
    age: conint(gt=0)
    relationship_status: Relationship


AvailableProperty = Union[House, Car]


class Person(BaseModel):
    type: str = "person"
    personal_data: PersonalData
    properties: List[AvailableProperty] = []


PersonParser = TypeAdapter(Person)
