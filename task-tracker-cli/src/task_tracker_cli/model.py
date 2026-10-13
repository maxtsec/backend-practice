from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

class Status(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

@dataclass
class Task:
    id: int
    description: str
    status: Status
    created_at: datetime
    updated_at: datetime