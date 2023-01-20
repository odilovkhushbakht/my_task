from pydantic import BaseModel, EmailStr
from typing_extensions import TypedDict


class Address(TypedDict):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float
    lng: float


class Salary(TypedDict):
    custom_from: int
    to: int
    currency: str
    gross: bool


class Contacts(TypedDict):
    fullName: str
    phone: str
    email: EmailStr


class ModelEmployee(BaseModel):
    description: str
    employment: str
    allow_messages: bool = True
    billing_type: str = "packageOrSingle"
    business_area: int = 1
    html_tags: bool = True
    image_url: str = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    address: Address
    name: str
    salary: Salary
    contacts: Contacts
    experience: dict = {'id': 'noMatter'}
    schedule: dict = {'id': 'fullDay'}