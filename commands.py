from task_manager import (
    create_task,
    list_tasks,
    complete_task,
    delete_task
)
from reminder import check_due_tasks

from command_parser import parse_task_command

from datetime import datetime

def command_log(message: str) -> None:
    """
    Prints command logs.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [COMMANDS] {message}")


def handle_task_command(command: str) -> str |None:
    command = command.lower()
    command_log(f"Command: {command}")

    # Add task
    if (
    "add task" in command
    or "create task" in command
    or "add a task" in command
    or "i need to" in command
):
        title = command.replace("add task", "").strip()

        if title:
            command_log(f"Creating task: {title}")
            create_task(
                title,
                "Added through SanX Assistant",
                None
            )
            return f"Done Sanx, I added your task: {title}"

        return "Sanx, please tell me the task name."

    # Show tasks
    elif (
        "show tasks" in command
        or "list tasks" in command
        or "my tasks" in command
    ):
        command_log("Showing all tasks")

        return list_tasks()


    # Complete task
    elif command.startswith("complete task"):
        try:
            task_id = int(command.replace("complete task", "").strip())
            command_log(f"Completing task {task_id}")
            complete_task(task_id)

            return f"Completed task {task_id}, Sanx."

        except ValueError:
            return "Sanx, please provide the task ID."


    # Delete task
    elif command.startswith("delete task"):
        try:
            task_id = int(command.replace("delete task", "").strip())
            command_log(f"Deleting task {task_id}")
            delete_task(task_id)

            return f"Deleted task {task_id}, Sanx."

        except ValueError:
            return "Sanx, please provide the task ID."

    # Show reminders
    elif (
    "show reminders" in command
    or "my reminders" in command
    or "reminders today" in command
):
        reminders = check_due_tasks()

        if not reminders:
            return "Sanx, you have no reminders for today."

        response = "Your reminders:\n"

        for reminder in reminders:
            response += (
                f"{reminder['id']}. "
                f"{reminder['title']} "
                f"at {reminder['due_time']}\n"
            )

        return response
    

    # Natural language task creation
    parsed = parse_task_command(command)

    if parsed["title"]:

        create_task(
            parsed["title"],
            "Created through SanX Assistant",
            parsed["due_date"],
            parsed["due_time"]
        )

        return (
            f"Okay Sanx, I added your task: "
            f"{parsed['title']}"
        )

    # Command not handled.
    return None