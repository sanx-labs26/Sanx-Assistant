import subprocess
import webbrowser
import random

from datetime import datetime

APP_EXECUTABLES = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
    "cmd": "cmd.exe",
}

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
}


def desktop_log(message: str) -> None:
    """
    Prints desktop automation logs.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [DESKTOP] {message}")


def open_application(app_name: str) -> str:
    """
    Opens a supported desktop application or website.
    """
    app = app_name.lower().strip().strip(".,!?")

    desktop_log(f"Opening: {app}")

    try:

        if app == "chrome":
            subprocess.Popen(APP_EXECUTABLES["chrome"])
            return random.choice([
                "Opening Google Chrome, Sanx.",
                "Launching Chrome, Sanx.",
                "Chrome is opening.",
                "Done, opening Chrome."
            ])

        elif app == "notepad":
            subprocess.Popen(APP_EXECUTABLES["notepad"])
            return "Opening Notepad, Sanx."

        elif app == "calculator":
            subprocess.Popen(APP_EXECUTABLES["calculator"])
            return "Opening Calculator, Sanx."

        elif app == "paint":
            subprocess.Popen(APP_EXECUTABLES["paint"])
            return "Opening Paint, Sanx."

        elif app == "explorer":
            subprocess.Popen(APP_EXECUTABLES["explorer"])
            return "Opening File Explorer, Sanx."

        elif app == "cmd":
            subprocess.Popen(APP_EXECUTABLES["cmd"])
            return "Opening Command Prompt, Sanx."

        elif app == "youtube":
            webbrowser.open(WEBSITES["youtube"])
            return "Opening YouTube, Sanx."

        elif app == "google":
            webbrowser.open(WEBSITES["google"])
            return "Opening Google, Sanx."

        elif app == "github":
            webbrowser.open(WEBSITES["github"])
            return "Opening GitHub, Sanx."

        return f"Sorry Sanx, I couldn't find '{app_name}'."

    except Exception as e:
        desktop_log(f"Error opening {app}: {e}")
        return f"Sorry Sanx, I couldn't open {app_name}."
    

def close_application(app_name: str) -> str:
    """
    Closes a supported desktop application.
    """
    app = app_name.lower().strip().strip(".,!?")

    desktop_log(f"Closing: {app}")

    APPS = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
    }

    if app in ("explorer", "file explorer"):
        return "For safety, Sanx will not close Windows Explorer."

    if app not in APPS:
        return f"Sorry Sanx, I couldn't find '{app_name}'."

    try:
        result = subprocess.run(
            ["taskkill", "/F", "/IM", APPS[app]],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"Closing {app.title()}, Sanx."

        return f"{app.title()} is not running."

    except Exception as e:
        desktop_log(f"Error closing {app}: {e}")
        return f"Sorry Sanx, I couldn't close {app_name}."