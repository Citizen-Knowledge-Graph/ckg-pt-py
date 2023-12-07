from pydantic import BaseModel, conint, Field
from enum import Enum
from typing import Optional

from src.models.constraint import IntConstraint, BoolConstraint


class Relationship(Enum):
    SINGLE = "single"
    MARRIED = "married"


class PersonalDataProperties(BaseModel):
    age: conint(gt=0)
    residence: str = None
    drivers_license: bool = None
    children: conint(ge=0) = None
    relationship_status: Optional[Relationship] = None


class PersonalData(BaseModel):
    property_class: str = Field("personal_data", pattern=r"^personal_data$")
    property_fields: PersonalDataProperties


class PersonalDataConstraints(BaseModel):
    age: Optional[IntConstraint] = None
    drivers_license: Optional[BoolConstraint] = None


class PersonalDataConstraint(BaseModel):
    constraint_class: str = Field("personal_data", pattern=r"^personal_data$")
    constraint_fields: PersonalDataConstraints
