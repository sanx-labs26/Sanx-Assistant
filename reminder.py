from datetime import datetime
from database import get_tasks


def check_due_tasks():
    """
    Returns a list of tasks that are due today
    and are still pending.
    """

    today = datetime.now().strftime("%Y-%m-%d")

    tasks = get_tasks()
    reminders = []

    for task in tasks:
        task_id, title, description, due_date, due_time, status, created_at = task

        if (
            due_date
            and due_date == today
            and status.lower() == "pending"
        ):
            reminders.append({
                "id": task_id,
                "title": title,
                "description": description,
                "due_date": due_date,
                "due_time": due_time
            })

    return reminders


def print_reminders():
    reminders = check_due_tasks()

    if not reminders:
        print("✅ No reminders for today.")
        return "✅ No reminders for today."

    print("\n🔔 Today's Reminders:\n")

    for reminder in reminders:
        print(f"Task ID : {reminder['id']}")
        print(f"Title   : {reminder['title']}")
        print(f"Details : {reminder['description']}")
        print(f"Due Date: {reminder['due_date']}")
        print(f"Due Time: {reminder['due_time']}")
        print("-" * 35)

    return reminders