from pydantic import BaseModel, Field


class IdentifiableSchema(BaseModel):
    id: int = Field(title="Identifier")
