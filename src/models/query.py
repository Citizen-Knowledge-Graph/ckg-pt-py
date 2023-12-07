from pydantic import BaseModel, TypeAdapter
from typing import List, Union

from src.models.personal_data import PersonalDataConstraint
from src.models.car import CarConstraint
from src.models.house import HouseConstraint
from src.models.entity_type import EntityTypeConstraint


AvailableConstraints = Union[HouseConstraint, CarConstraint, PersonalDataConstraint, EntityTypeConstraint]


class Query(BaseModel):
    constraints: List[AvailableConstraints]


QueryParser = TypeAdapter(Query)
