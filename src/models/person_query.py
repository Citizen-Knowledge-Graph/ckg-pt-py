from pydantic import BaseModel, TypeAdapter
from typing import List, Union

from src.models.constraint import IntConstraint
from src.models.house import HouseConstraint

AvailablePropertyConstraints = Union[HouseConstraint]


class PersonalDataConstraint(BaseModel):
    age: IntConstraint


class PersonQuery(BaseModel):
    target_type: str = "Person"
    personal_data: PersonalDataConstraint
    properties: List[AvailablePropertyConstraints] = []


PersonQueryParser = TypeAdapter(PersonQuery)
