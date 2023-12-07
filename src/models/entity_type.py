from pydantic import Field, BaseModel

from src.models.constraint import StringConstraint


class EntityTypeProperties(BaseModel):
    value: str


class EntityType(BaseModel):
    property_class: str = Field("entity_type", pattern=r"^entity_type$")
    property_fields: EntityTypeProperties


class EntityTypeConstraints(BaseModel):
    value: StringConstraint


class EntityTypeConstraint(BaseModel):
    constraint_class: str = Field("entity_type", pattern=r"^entity_type")
    constraint_fields: EntityTypeConstraints
