import os
import subprocess
import platform

from datetime import datetime

def file_log(message: str) -> None:
    """
    Prints file operation logs.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [FILES] {message}")


def find_and_open(name, search_path: str) -> str:
    """
    Find a file/folder by name and open it
    """
    try:
        for root, dirs, files in os.walk(search_path):

            for folder in dirs:
                folder_name = folder.lower().replace("-", " ").replace("_", " ")

                if name.lower() in folder_name:
                    path = os.path.join(root, folder)
                    os.startfile(path)
                    file_log(f"Opening folder: {path}")
                    os.startfile(path)
                    return f"Opened folder: {path}"

            for file in files:
                file_name = file.lower().replace("-", " ").replace("_", " ")

                if name.lower() in file_name:
                    path = os.path.join(root, file)
                    os.startfile(path)
                    file_log(f"Opening file: {path}")
                    os.startfile(path)
                    return f"Opened file: {path}"

        return "File or folder not found"

    except Exception as e:
        return f"Error: {e}"


def list_files(folder_path):
    """
    List files and folders inside a directory
    """
    try:
        files = os.listdir(folder_path)
        return files
    except Exception as e:
        return f"Error: {e}"


def open_file(file_path):
    """
    Open a file using default application
    """
    try:
        system = platform.system()

        if system == "Windows":
            file_log(f"Opening file: {file_path}")
            os.startfile(file_path)

        elif system == "Darwin":
            subprocess.call(["open", file_path])

        else:
            subprocess.call(["xdg-open", file_path])

        return f"Opened {file_path}"

    except Exception as e:
        return f"Error: {e}"


def create_folder(folder_path):
    """
    Create a new folder
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder created sucessfully:\n{folder_path}"

    except Exception as e:
        return f"Error: {e}"


def search_file(search_name, search_path):
    """
    Search for a file inside a folder
    """
    file_log(f"Searching for: {search_name}")

    results = []

    try:
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if search_name.lower() in file.lower():
                    results.append(os.path.join(root, file))

        if results:
            return results
        else:
            return "No file found"

    except Exception as e:
        return f"Error: {e}"


def read_text_file(file_path):
    """
    Read text files
    """
    try:
        file_log(f"Reading file: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            conent = file.read

            if not conent.strip():
                return"The file is empty."

            return conent

    except Exception as e:
        return f"Error: {e}"

def close_app(process_name):
    """
    Close an application by its process name.
    """
    file_log(f"Closing process: {process_name}")

    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", process_name],
            check=True,
            capture_output=True,
            text=True
        )

        return f"Closed {process_name}"

    except subprocess.CalledProcessError:
        return f"{process_name} is not running."

    except Exception as e:
        return f"Error: {e}"


def close_by_name(name):
    """
    Close common applications using a friendly name.
    """

    apps = {
    "notepad": "notepad.exe",
    "calculator": "CalculatorApp.exe",
    "chrome": "chrome.exe",
    "youtube":"chrome.exe",
    "google": "chrome.exe",
    "github": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "vscode": "Code.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    }

    process = apps.get(name.lower())

    if not process:
        return f"Unknown application: {name}"

    return close_app(process)