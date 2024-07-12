from pydantic import BaseModel


class CapitalizeResponse(BaseModel):
    text: str
