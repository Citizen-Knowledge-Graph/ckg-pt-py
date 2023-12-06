from pydantic import conint, Field
from enum import Enum

from src.models.property import Property, PropertyFeatures


class CarType(Enum):
    ELECTRIC = "electric"
    GASOLINE = "gasoline"


class CarProperties(PropertyFeatures):
    car_age: conint(gt=0)
    car_type: CarType


class Car(Property):
    property_type: str = Field("Car", pattern=r"^Car$")
    property_features: CarProperties
