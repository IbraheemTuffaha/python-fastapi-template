from pydantic import BaseModel


class BaseCapitalize(BaseModel):
    text: str


class CapitalizeIn(BaseCapitalize): ...


class CapitalizeOut(BaseCapitalize): ...
