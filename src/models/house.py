from pydantic import Field

from src.models.property import Property, PropertyFeatures
from src.models.constraint import MinConstraint, MaxConstraint


class HouseProperties(PropertyFeatures):
    roof_area: float
    house_age: int


class HousePropertyConstraints(PropertyFeatures):
    roof_area: MinConstraint
    house_age: MaxConstraint


class House(Property):
    property_type: str = Field("House", pattern=r"^House$")
    property_features: HouseProperties


class HouseConstraint(Property):
    property_type: str = "House"
    property_features: HousePropertyConstraints

