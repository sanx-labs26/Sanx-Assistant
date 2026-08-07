import re
from datetime import datetime, timedelta


def parse_task_command(text):
    text = text.lower()

    task_title = None
    due_date = None
    due_time = None

    # Extract task title
    patterns = [
        r"remind me to (.+)",
        r"add task (.+)",
        r"i need to (.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            task_title = match.group(1)
            break

    # Extract date
    if "tomorrow" in text:
        due_date = (
            datetime.now() + timedelta(days=1)
        ).strftime("%Y-%m-%d")

    elif "today" in text:
        due_date = datetime.now().strftime("%Y-%m-%d")

    # Extract time
    time_match = re.search(
        r"(\d{1,2})\s*(am|pm)",
        text
    )

    if time_match:
        due_time = time_match.group(1) + time_match.group(2)

    return {
        "title": task_title,
        "due_date": due_date,
        "due_time": due_time
    }