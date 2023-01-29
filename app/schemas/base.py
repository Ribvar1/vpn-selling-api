from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        use_enum_values = True


class IdentifiableSchema(BaseSchema):
    id: int = Field(title="Identifier")
