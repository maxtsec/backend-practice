from datetime import datetime, timezone

from task_tracker_cli import storage
from task_tracker_cli.model import Status, Task


class TaskError(Exception):
    """A request that breaks a business rule, e.g. an empty description."""


def add_task(description: str) -> Task:
    description = description.strip()
    if not description:
        raise TaskError("Description cannot be empty.")

    data = storage.load()
    now = datetime.now(timezone.utc)
    task = Task(
        id=data.next_id,
        description=description,
        status=Status.TODO,
        created_at=now,
        updated_at=now,
    )
    data.tasks.append(task)
    data.next_id += 1
    storage.save(data)
    return task



def list_tasks(status: Status | None = None) -> list[Task]:
    tasks = storage.load().tasks
    if status is None:
        return tasks
    return [task for task in tasks if task.status == status]