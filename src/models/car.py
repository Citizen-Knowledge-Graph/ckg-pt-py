from pydantic import conint, Field, BaseModel

from src.models.constraint import IntConstraint, StringConstraint


class CarProperties(BaseModel):
    car_age: conint(gt=0)
    car_type: str


class Car(BaseModel):
    property_class: str = Field("car", pattern=r"^car$")
    property_fields: CarProperties


class CarPropertyConstraints(BaseModel):
    car_age: IntConstraint
    car_type: StringConstraint


class CarConstraint(BaseModel):
    constraint_class: str = Field("car", pattern=r"^car$")
    constraint_fields: CarPropertyConstraints
