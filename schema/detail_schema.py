from pydantic import BaseModel


class BaseDetail(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    age:int

    