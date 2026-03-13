from sqlmodel import Field

from app.models.user import UserBase


class RegisterUser(UserBase):
    password: str = Field(nullable=False)


class ResponseUser(UserBase): ...
