from pydantic import BaseModel


class PropertyFeatures(BaseModel):
    pass


class Property(BaseModel):
    property_type: str
    property_features: PropertyFeatures
