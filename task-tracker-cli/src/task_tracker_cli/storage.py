import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from task_tracker_cli.model import Status, Task

FILE_NAME = "tasks.json"

@dataclass
class TaskData:
    next_id: int
    tasks: list[Task]

def load() -> TaskData:
    path = Path.cwd() / FILE_NAME
    if not path.exists():
        return TaskData(next_id=1, tasks=[])

    raw = json.loads(path.read_text(encoding="utf-8"))
    return TaskData(
        next_id=raw["next_id"],
        tasks=[_task_from_dict(item) for item in raw["tasks"]],
    )

def save(data: TaskData) -> None:
    path = Path.cwd() / FILE_NAME
    raw = {
        "next_id": data.next_id,
        "tasks": [_task_to_dict(task) for task in data.tasks],
    }
    path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

def _task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status.value,
        "createdAt": task.created_at.isoformat(),
        "updatedAt": task.updated_at.isoformat(),
    }

def _task_from_dict(data: dict) -> Task:
    return Task(
        id=data["id"],
        description=data["description"],
        status=Status(data["status"]),
        created_at=datetime.fromisoformat(data["createdAt"]),
        updated_at=datetime.fromisoformat(data["updatedAt"]),
    )