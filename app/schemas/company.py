from pydantic import BaseModel

class Company(BaseModel):
    name: str
    city: str
    industry: str
    stage: str