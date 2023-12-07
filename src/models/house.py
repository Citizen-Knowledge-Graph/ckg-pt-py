from pydantic import Field, BaseModel

from src.models.constraint import IntConstraint


class HouseProperties(BaseModel):
    roof_area: int
    house_age: int


class House(BaseModel):
    property_class: str = Field("house", pattern=r"^house")
    property_fields: HouseProperties


class HousePropertyConstraints(BaseModel):
    roof_area: IntConstraint
    house_age: IntConstraint


class HouseConstraint(BaseModel):
    constraint_class: str = Field("house", pattern=r"^house")
    constraint_fields: HousePropertyConstraints
