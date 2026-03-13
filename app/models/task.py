import uuid
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class TaskBase(SQLModel):
    header: str = Field(...)
    description: str | None = Field(nullable=True, default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: datetime | None = Field(default=None)


class Task(TaskBase, table=True):
    __table__ = "tasks"
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    owner_id: uuid.UUID = Field(foreign_key="users.id")
    owner: "User" = Relationship(back_populates="tasks")  # type: ignore  # noqa: F821
