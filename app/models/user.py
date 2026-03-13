import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Relationship


class UserBase(SQLModel):
    first_name: str = Field(...)
    last_name: str | None = Field(nullable=True, default=None)
    email: EmailStr


class User(UserBase, table=True):
    __table__ = "users"
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    active: bool = Field(default=True)
    admin: bool = Field(default=False)
    tasks: list["Task"] = Relationship(back_populates="owner")  # type: ignore  # noqa: F821
