from study import study_mode
from quiz import get_quiz
from placement import interview_mode
from progress import save_progress, get_progress
from task_manager import (
    create_task,
    list_tasks,
    finish_task,
    remove_task,
)
from reminder import (
    print_reminders,
)
from knowledge_base import (
    search_knowledge,
)
from system_tools import(
     get_current_date,
     get_current_datetime,
     get_current_day,
     get_current_time,
     get_weather,
)
from desktop_control import open_application,close_application

from datetime import datetime

def router_log(message: str) -> None:
    """
    Prints router debug messages.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [ROUTER] {message}")

class AssistantRouter:

    def route(self, command: str):

        command = command.lower().strip()

        router_log(f"DEBUG COMMAND: [{command}]")

        # ------------------------
        # Study Mode
        # ------------------------
        if (
            command.startswith("quiz ")
            or command.startswith("start quiz ")
            or command.startswith("test me ")
        ):

            topic = (
                command.replace("study ", "")
                .replace("learn ", "")
                .replace("teach me ", "")
                .strip()
            )

            result = study_mode(topic)

            save_progress(
                topic=topic,
                status="Studied",
                score=10
            )

            return result

        # ------------------------
        # Quiz Mode
        # ------------------------
        elif (
            command.startswith("quiz ",
            "start quiz ",
            "test me ")
        ):

            subject = (
                command.replace("quiz ", "")
                .replace("start quiz ", "")
                .replace("test me ", "")
                .strip()
            )

            quiz = get_quiz(subject)

            save_progress(
                topic=subject,
                status="Quiz Attempted",
                score=0
            )

            return f"""
        📘 Quiz

        Question:
        {quiz['question']}

        Answer:
        {quiz['answer']}
        """

        

        # ------------------------
        # Interview Mode
        # ------------------------
        elif (
            command.startswith("interview ",
            "mock interview "
            "practice interview ")
        ):

            category = (
                command.replace("interview ", "")
                .replace("mock interview ", "")
                .replace("practice interview ", "")
                .strip()
            )

            return interview_mode(category)

        # ------------------------
        # Progress
        # ------------------------
        elif (
            command == "progress"
            or command == "show progress"
            or command == "study progress"
        ):

            rows = get_progress()

            if not rows:
                return "No study progress found."

            result = "📈 Study Progress\n\n"

            for row in rows:

                result += (
                    f"Topic : {row[0]}\n"
                    f"Status: {row[1]}\n"
                    f"Score : {row[2]}/10\n"
                    f"Date  : {row[3]}\n\n"
                )

            return result

        # ------------------------
        # Task Manager
        # ------------------------

        elif command.startswith("add task "):

            title = command.replace("add task ", "").strip()

            create_task(title)

            return f"✅ Task '{title}' added successfully."

        elif command in (
            "show tasks",
            "list tasks",
            "my tasks",
        ):

            return list_tasks()

        elif command.startswith("complete task "):

            try:
                task_id = int(
                    command.replace("complete task ", "")
                )

                return finish_task(task_id)

            except ValueError:
                return "Please provide a valid task ID."

        elif command.startswith("delete task "):

            try:
                task_id = int(
                    command.replace("delete task ", "")
                )

                return remove_task(task_id)

            except ValueError:
                return "Please provide a valid task ID."

        # ------------------------
        # Reminder
        # ------------------------

        elif command in (
            "reminders",
            "show reminders",
            "today reminders",
        ):

            print_reminders()

            return "Displayed today's reminders."

        # ------------------------
        # Knowledge Base
        # ------------------------

        elif command.startswith("search "):

            keyword = command.replace("search ", "").strip()

            results = search_knowledge(keyword)

            if not results:
                return "No knowledge found."

            response = "📚 Knowledge Search Results\n\n"

            for topic, content in results:

                response += (
                    f"\n📚 {topic}\n"
                    f"{content}\n"
                    "----------------------\n"
                )

            return response

        # ------------------------
        # Unknown Command
        # ------------------------

        # ------------------------
        # Time
        # ------------------------

        elif command in (
        "time",
        "current time",
        "what is the time",
        "tell me the time",
        ):

         return (
          f"The current time is "
          f"{get_current_time()}, Sanx."
        )


        # ------------------------
        # Date
        # ------------------------

        elif command in (
        "date",
        "today date",
        "today's date",
        "current date",
        ):

          return (
           f"Today's date is "
           f"{get_current_date()}, Sanx."
        )


        # ------------------------
        # Day
        # ------------------------

        elif command in (
        "day",
        "today",
        "what day is today",
        ):

          return (
            f"Today is "
            f"{get_current_day()}, Sanx."
        )


        # ------------------------
        # Date & Time
        # ------------------------

        elif command in (
        "date and time",
        "current date and time",
        ):

          return get_current_datetime()


        # ------------------------
        # Weather
        # ------------------------

        elif (
        command == "weather",
        "weather ",
        "weather today" in command
        ):

          return get_weather()

        
        # Command not handled by the router.
        return None