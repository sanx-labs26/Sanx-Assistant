from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


def get_current_date():
    now = datetime.now()
    return now.strftime("%d %B %Y")


def get_current_day():
    now = datetime.now()
    return now.strftime("%A")


def get_current_datetime():
    now = datetime.now()

    return (
        f"Today is {now.strftime('%A')}, "
        f"{now.strftime('%d %B %Y')}.\n"
        f"The current time is {now.strftime('%I:%M %p')}."
    )


def get_weather():
    """
    Placeholder weather function.
    Replace this later with a real weather API.
    """

    return (
        "Sorry Sanx, live weather is not configured yet.\n"
        "Connect a weather API to enable this feature."
    )