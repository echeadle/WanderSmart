from pydantic import BaseModel, Field
from typing import List, Optional

class TravelPackage(BaseModel):
    title: str
    link: str
    details: str

class Attraction(BaseModel):
    name: str
    type: str
    description: str
    entrance_fee: str

class TransportationOption(BaseModel):
    name: str
    type: str
    details: str
    cost: str

class Transportation(BaseModel):
    options: List[TransportationOption]

class CrewAIResponse(BaseModel):
    destination: str = Field(default="Destination not specified")
    budget: str = Field(default="Budget not specified")
    interests: List[str] = Field(default_factory=list)
    travel_packages: List[TravelPackage] = Field(default_factory=list)
    attractions: List[Attraction] = Field(default_factory=list)
    transportation: Optional[Transportation] = None
