"""
Data transfer objects
"""

from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr


class CreateUserDto(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]


class UpdateUserDto(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe"
            }
        }


class UserDto(BaseModel):
    email: EmailStr
    name: str

    class Config:
        orm_mode = True
