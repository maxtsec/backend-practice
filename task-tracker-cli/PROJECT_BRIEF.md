# Task Tracker CLI — Project Brief

Build a CLI app to track your tasks and manage your to-do list.

## Overview

Task Tracker is a simple command line interface (CLI) for tracking what you need to do, what you are currently working on, and what you have done.

Skills practised:

- Working with the filesystem
- Handling user inputs
- Building a simple CLI application

## Functional Requirements

The application runs from the command line, accepts user actions and inputs as arguments, and stores tasks in a JSON file.

The user should be able to:

- [ ] Add a task
- [ ] Update a task
- [ ] Delete a task
- [ ] Mark a task as in progress
- [ ] Mark a task as done
- [ ] List all tasks
- [ ] List all tasks that are done
- [ ] List all tasks that are not done
- [ ] List all tasks that are in progress

## Constraints

- Any programming language may be used (this project: **Python**).
- Use **positional arguments** on the command line to accept user inputs.
- Store tasks in a **JSON file in the current directory**.
- The JSON file must be **created if it does not exist**.
- Use the language's **native file system module** to interact with the JSON file.
- **No external libraries or frameworks.**
- Handle errors and edge cases gracefully.

## Commands

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

| Command | Arguments | Effect |
|---|---|---|
| `add` | `<description>` | Create a new task, print its ID |
| `update` | `<id> <description>` | Change a task's description |
| `delete` | `<id>` | Remove a task |
| `mark-in-progress` | `<id>` | Set status to `in-progress` |
| `mark-done` | `<id>` | Set status to `done` |
| `list` | *(none)* | Show all tasks |
| `list` | `done` \| `todo` \| `in-progress` | Show tasks with that status |

## Task Properties

| Property | Description |
|---|---|
| `id` | A unique identifier for the task |
| `description` | A short description of the task |
| `status` | One of `todo`, `in-progress`, `done` |
| `createdAt` | Date and time the task was created |
| `updatedAt` | Date and time the task was last updated |

All properties are written to the JSON file when a task is added, and `updatedAt` is refreshed whenever a task is updated.

## Getting Started

### 1. Set up the development environment

- Choose a programming language you are comfortable with.
- Have a code editor or IDE installed (e.g. VS Code).

### 2. Project initialization

- Create a new project directory for the Task Tracker CLI.
- Initialize a version control system (e.g. Git).

### 3. Implementing features

- Start with a basic CLI structure that handles user inputs.
- Implement features one at a time, testing each before moving on: add first, then list, then update, then marking status, and so on.

### 4. Testing and debugging

- Test each feature individually.
- Inspect the JSON file to verify tasks are stored correctly.
- Debug any issues that come up.

### 5. Finalizing the project

- Confirm all features are implemented and tested.
- Clean up the code and add comments where necessary.
- Write a good README explaining how to use the Task Tracker CLI.
