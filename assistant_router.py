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


class AssistantRouter:

    def route(self, command: str):

        command = command.lower().strip()

        # ------------------------
        # Study Mode
        # ------------------------
        if (
            command.startswith("study ")
            or command.startswith("learn ")
            or command.startswith("teach me ")
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
            command.startswith("quiz ")
            or command.startswith("start quiz ")
            or command.startswith("test me ")
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
            command.startswith("interview ")
            or command.startswith("mock interview ")
            or command.startswith("practice interview ")
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

            response = ""

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
        return None