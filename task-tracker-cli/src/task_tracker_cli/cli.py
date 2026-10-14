import argparse
import sys

from task_tracker_cli import service
from task_tracker_cli.model import Status, Task


def main() -> None:
    # Windows may default to a legacy encoding when output is piped or redirected.
    sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(prog="task-cli", description="Track your tasks.")
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="What needs to be done")
    add_parser.set_defaults(handler=handle_add)

    list_parser = commands.add_parser("list", help="List tasks, optionally by status")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=[status.value for status in Status],
        help="Only show tasks with this status",
    )
    list_parser.set_defaults(handler=handle_list)

    args = parser.parse_args()

    try:
        args.handler(args)
    except service.TaskError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


def handle_add(args: argparse.Namespace) -> None:
    task = service.add_task(args.description)
    print(f"Task added successfully (ID: {task.id})")


def handle_list(args: argparse.Namespace) -> None:
    status = Status(args.status) if args.status else None
    tasks = service.list_tasks(status)
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(format_task(task))


def format_task(task: Task) -> str:
    return f"[{task.id}] {task.status.value:<11}  {task.description}"