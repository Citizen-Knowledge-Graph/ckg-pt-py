from pydantic import BaseModel, TypeAdapter
from typing import List, Union

from src.models.personal_data import PersonalData
from src.models.entity_type import EntityType
from src.models.house import House
from src.models.car import Car

AvailableProperty = Union[EntityType, PersonalData, House, Car]


class Person(BaseModel):
    properties: List[AvailableProperty]


PersonParser = TypeAdapter(Person)
