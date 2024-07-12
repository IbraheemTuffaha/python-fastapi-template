from pydantic import BaseModel


class CapitalizeRequest(BaseModel):
    text: str
