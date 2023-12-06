from pydantic import BaseModel, Field
from typing import Union


class MinConstraintFeatures(BaseModel):
    min: int


class MinConstraint(BaseModel):
    constraint_type: str = Field("min", pattern=r"^min$")
    constraint_features: MinConstraintFeatures


class MaxConstraintFeatures(BaseModel):
    max: int


class MaxConstraint(BaseModel):
    constraint_type: str = Field("max", pattern=r"^max$")
    constraint_features: MaxConstraintFeatures


class MinMaxConstraintFeatures(BaseModel):
    min: int
    max: int


class MinMaxConstraint(BaseModel):
    constraint_type: str = Field("min_max", pattern=r"^min_max$")
    constraint_features: MinMaxConstraintFeatures


IntConstraint = Union[MinConstraint, MaxConstraint, MinMaxConstraint]
