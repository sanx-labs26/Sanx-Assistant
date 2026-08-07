from database import (
    add_task,
    get_tasks,
    complete_task,
    delete_task
)


def create_task(title, description="", due_date=""):
    add_task(title, description, due_date)
    return f"✅ Task '{title}' added successfully."


def list_tasks():
    tasks = get_tasks()

    if not tasks:
        return "📋 No tasks found."

    output = "\n📋 Your Tasks:\n"

    for task in tasks:
        task_id, title, description, due_date, due_time, status, created_at = task

        output += (
            f"\nID: {task_id}\n"
            f"Title: {title}\n"
            f"Description: {description}\n"
            f"Due: {due_date}\n"
            f"Due: {due_time}\n"
            f"Status: {status}\n"
            f"Created_at: {created_at}\n"
            "------------------------"
        )

    return output


def finish_task(task_id):
    complete_task(task_id)
    return f"✅ Task {task_id} marked as completed."


def remove_task(task_id):
    delete_task(task_id)
    return f"🗑️ Task {task_id} deleted successfully."