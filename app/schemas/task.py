from sqlmodel import Field, SQLModel

from app.models.task import TaskBase


class CreateTask(SQLModel):
    header: str = Field(...)
    description: str | None = Field(nullable=True)


class ResponseTask(TaskBase): ...
