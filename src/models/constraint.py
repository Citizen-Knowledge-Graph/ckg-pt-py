from pydantic import BaseModel, Field
from typing import Union


class BaseIntConstraint(BaseModel):
    constraint_group: str = Field("int_constraint", pattern=r"^int_constraint")
    constraint_type: str
    constraint_features: dict


class MinConstraintFeatures(BaseModel):
    min: int


class MinConstraint(BaseIntConstraint):
    constraint_type: str = Field("min", pattern=r"^min$")
    constraint_features: MinConstraintFeatures


class MaxConstraintFeatures(BaseModel):
    max: int


class MaxConstraint(BaseIntConstraint):
    constraint_type: str = Field("max", pattern=r"^max$")
    constraint_features: MaxConstraintFeatures


class MinMaxConstraintFeatures(BaseModel):
    min: int
    max: int


class MinMaxConstraint(BaseIntConstraint):
    constraint_type: str = Field("min_max", pattern=r"^min_max$")
    constraint_features: MinMaxConstraintFeatures


IntConstraint = Union[MinConstraint, MaxConstraint, MinMaxConstraint]


class BaseStringConstraint(BaseModel):
    constraint_group: str = Field("string_constraint", pattern=r"^string_constraint")
    constraint_type: str
    constraint_features: dict


class ExactStringConstraintFeatures(BaseModel):
    exact: str


class ExactStringConstraint(BaseStringConstraint):
    constraint_type: str = Field("exact", pattern=r"^exact$")
    constraint_features: ExactStringConstraintFeatures


StringConstraint = Union[ExactStringConstraint]


class BaseBoolConstraint(BaseModel):
    constraint_group: str = Field("bool_constraint", pattern=r"^bool_constraint")
    constraint_type: str
    constraint_features: dict


class MatchBoolConstraintFeatures(BaseModel):
    match: bool


class MatchBoolConstraint(BaseBoolConstraint):
    constraint_type: str = Field("match", pattern=r"^match$")
    constraint_features: MatchBoolConstraintFeatures


BoolConstraint = Union[MatchBoolConstraint]
